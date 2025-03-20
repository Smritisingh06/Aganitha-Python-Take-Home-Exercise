def get_papers_data(query, max_results=10):
    """Fetch papers and their details"""
    from fetcher import fetch_papers_from_pubmed, fetch_paper_details 

    paper_ids = fetch_papers_from_pubmed(query, max_results)
    papers = [fetch_paper_details(p_id) for p_id in paper_ids]
    
    return papers  # ✅ This will now include new fields
