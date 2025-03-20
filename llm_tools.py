# import google.generativeai as genai

# # Set API Key directly (Not recommended for production)
# GEMINI_API_KEY = "AizaSyCoUEpZvaNBlnu59nN2o-OpULZufovAQwA"  # Replace with your actual key

# genai.configure(api_key=GEMINI_API_KEY)

# def identify_non_academic_authors(authors, affiliations):
#     """Uses Google Gemini to identify non-academic authors from affiliations."""
#     prompt = "Identify the non-academic authors based on the affiliations:\n\n"
#     for author, affiliation in zip(authors, affiliations):
#         prompt += f"Author: {author}\nAffiliation: {affiliation}\n\n"

#     try:
#         model = genai.GenerativeModel("gemini-pro")  # Use 'gemini-pro' model
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         print(f"Error calling Google Gemini API: {e}")
#         return "Error identifying non-academic authors"


import google.generativeai as genai

# Set API Key
GEMINI_API_KEY = "AizaSyCoUEpZvaNBlnu59nN2o-OpULZufovAQwA"  # Replace with actual key
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
        return response.text.strip()  # Process response accordingly
    except Exception as e:
        print(f"❌ LLM Error: {e}")
        return None
