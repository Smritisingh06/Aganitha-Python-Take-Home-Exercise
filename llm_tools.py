import google.generativeai as genai

# API Key
GEMINI_API_KEY = "AizaSyCoUEpZvaNBlnu59nN2o-OpULZufovAQwA" 
genai.configure(api_key=GEMINI_API_KEY)

def classify_authors_and_companies(authors, affiliations):
    """Identifies non-academic authors, biotech/pharma companies, and emails using LLM."""
    
    prompt = """Analyze the following author affiliations:
    - Identify **non-academic authors**.
    - Extract **company names (pharmaceutical/biotech)**.
    - Find the **corresponding author email** if mentioned.
    
    Data:
    """
    for author, affiliation in zip(authors, affiliations):
        prompt += f"Author: {author}\nAffiliation: {affiliation}\n\n"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip()  
    except Exception as e:
        print(f"❌ LLM Error: {e}")
        return None
