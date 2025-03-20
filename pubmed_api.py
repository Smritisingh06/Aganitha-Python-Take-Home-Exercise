import requests
import xml.etree.ElementTree as ET

# Fetches PubMed IDs for a given search query
def fetch_papers_from_pubmed(query, max_results=10):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {'db': 'pubmed', 'term': query, 'retmode': 'xml', 'retmax': max_results}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        return [id_elem.text for id_elem in root.findall(".//Id")]
    except requests.RequestException as e:
        print(f"❌ Error fetching PubMed data: {e}")
        return []

# Fetches details of a paper using its PubMed ID
def fetch_paper_details(pubmed_id):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {'db': 'pubmed', 'id': pubmed_id, 'retmode': 'xml'}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        root = ET.fromstring(response.content)

        return {
            "PubmedID": pubmed_id,
            "Title": root.find(".//Item[@Name='Title']").text or "N/A",
            "Publication Date": root.find(".//Item[@Name='PubDate']").text or "N/A",
            "DOI": root.find(".//Item[@Name='DOI']").text or "N/A",
            "Non-academic Authors": "N/A",  # Placeholder (Update extraction logic)
            "Company Affiliations": "N/A",  # Placeholder (Update extraction logic)
            "Corresponding Author Email": "N/A"  # Placeholder (Update extraction logic)
        }
    except requests.RequestException as e:
        print(f"❌ Error fetching paper details for {pubmed_id}: {e}")
        return None
