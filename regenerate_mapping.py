import csv
import json
import os
from thefuzz import process

# --- Configuration ---
CSV_FILE = "Reading List 23fae7025b0f44f4bfa3c0789a2bd8fe.csv"
MARKDOWN_DIR = "Reading List 23fae7025b0f44f4bfa3c0789a2bd8fe"
OUTPUT_FILE = "file_mapping.json"

def main():
    print("Starting to regenerate the file mapping...")

    # 1. Read all article titles from the CSV
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8-sig') as infile:
            reader = csv.DictReader(infile)
            article_titles = [row['Name'] for row in reader if row['Name']]
    except FileNotFoundError:
        print(f"Error: CSV file not found at {CSV_FILE}")
        return
    
    print(f"Found {len(article_titles)} articles in the CSV.")

    # 2. Get all markdown filenames
    try:
        md_files = [f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')]
    except FileNotFoundError:
        print(f"Error: Markdown directory not found at {MARKDOWN_DIR}")
        return
        
    print(f"Found {len(md_files)} markdown files in the directory.")

    # 3. Intelligently match titles to filenames
    file_mapping = {}
    unmatched_titles = []

    for title in article_titles:
        # The process.extractOne function finds the best string match from a list
        # It returns a tuple: (best_match, score)
        match, score = process.extractOne(title, md_files)
        
        # We'll consider it a good match if the score is > 80
        if score > 80:
            # Construct the full path for the value in the mapping
            full_path = os.path.join(MARKDOWN_DIR, match).replace("\\", "/")
            file_mapping[title] = full_path
        else:
            unmatched_titles.append((title, match, score))

    # 4. Save the new mapping to a file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(file_mapping, f, indent=2)

    print(f"\nSuccessfully created new mapping for {len(file_mapping)} articles.")
    print(f"Mapping saved to {OUTPUT_FILE}")

    if unmatched_titles:
        print(f"\nWarning: Could not find a confident match for {len(unmatched_titles)} titles.")
        # for title, match, score in unmatched_titles:
        #     print(f"  - Title: '{title}' | Closest Match: '{match}' (Score: {score})")


if __name__ == "__main__":
    main()
