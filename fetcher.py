# import requests
# import xml.etree.ElementTree as ET

# # Function to fetch PubMed paper IDs based on search query
# def fetch_papers_from_pubmed(query, max_results=10):
#     """Fetches a list of PubMed IDs matching the search query."""
#     base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
#     params = {
#         'db': 'pubmed',
#         'term': query,
#         'retmode': 'xml',
#         'retmax': max_results,  # Adjust the max number of papers
#     }

#     try:
#         response = requests.get(base_url, params=params)
#         response.raise_for_status()  # Raise an error for bad status codes
        
#         root = ET.fromstring(response.content)
#         pubmed_ids = [id_elem.text for id_elem in root.findall(".//Id")]

#         if not pubmed_ids:
#             print("⚠️ No PubMed IDs found for the given query.")
        
#         return pubmed_ids
#     except requests.RequestException as e:
#         print(f"❌ Error fetching PubMed data: {e}")
#         return []
import requests
import xml.etree.ElementTree as ET

def fetch_papers_from_pubmed(query, max_results=10):
    """Fetches papers from PubMed based on query"""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        'db': 'pubmed',
        'term': query,
        'retmode': 'xml',
        'retmax': max_results
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    paper_ids = [id_elem.text for id_elem in root.findall(".//Id")]
    return paper_ids

def fetch_paper_details(pubmed_id):
    """Fetch paper details from PubMed using PubMed ID"""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        'db': 'pubmed',
        'id': pubmed_id,
        'retmode': 'xml'
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    title = root.find(".//Item[@Name='Title']")
    pub_date = root.find(".//Item[@Name='PubDate']")

    # ✅ NEW: Fetch authors and affiliations (requires full-text API or alternative endpoints)
    authors = root.findall(".//Item[@Name='Author']")
    affiliations = root.findall(".//Item[@Name='Affiliation']")

    non_academic_authors = []
    company_affiliations = []
    corresponding_author_email = "N/A"  # Default if not found

    for author, aff in zip(authors, affiliations):
        if aff is not None:
            aff_text = aff.text.lower()
            if "university" not in aff_text and "college" not in aff_text:  # ✅ Non-academic filter
                non_academic_authors.append(author.text)
                company_affiliations.append(aff.text)
            if "@" in aff_text:
                corresponding_author_email = aff.text  # ✅ Extract email if available

    return {
        "PubmedID": pubmed_id,
        "Title": title.text if title is not None else "N/A",
        "Publication Date": pub_date.text if pub_date is not None else "N/A",
        "Non-academic Authors": ", ".join(non_academic_authors) if non_academic_authors else "N/A",  # ✅ NEW
        "Company Affiliations": ", ".join(company_affiliations) if company_affiliations else "N/A",  # ✅ NEW
        "Corresponding Author Email": corresponding_author_email  # ✅ NEW
    }
