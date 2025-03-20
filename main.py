from data_processing import get_papers_data
from file_handler import save_to_csv

if __name__ == "__main__":
    query = input("Enter search query: ")
    papers = get_papers_data(query, max_results=10)

    if papers:
        print("\n🔹 Fetching paper details...\n")
        for paper in papers:
            print(paper)

        # Save results to CSV
        save_to_csv(papers)
    else:
        print("⚠️ No results found.")
