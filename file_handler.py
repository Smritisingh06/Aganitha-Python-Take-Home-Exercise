import csv
import os
from pathlib import Path

def save_to_csv(papers, filename="papers.csv"):
    """
    Save paper data to a CSV file directly in the Downloads folder (Windows).
    """

    # ✅ Automatically get the Windows "Downloads" folder
    downloads_folder = Path.home() / "Downloads"
    save_path = downloads_folder / filename

    headers = [
        "PubmedID", "Title", "Publication Date",
        "Non-academic Authors",
        "Company Affiliations",
        "Corresponding Author Email"
    ]

    try:
        # ✅ Check if file is open in Excel
        if os.path.exists(save_path):
            try:
                os.rename(save_path, save_path)  # Test if file is locked
            except PermissionError:
                print("❌ The file is open in another program! Close it and try again.")
                return

        # ✅ Save the CSV file
        with open(save_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

            for paper in papers:
                writer.writerow({key: paper.get(key, "N/A") for key in headers})

        print(f"✅ Data successfully saved to: {save_path}")

    except PermissionError:
        print("❌ Permission denied! Try saving in another location.")

