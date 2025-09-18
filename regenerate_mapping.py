import csv
import json
import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
API_KEY = os.getenv("GEMINI_API_KEY")
CSV_FILE = "Reading List 23fae7025b0f44f4bfa3c0789a2bd8fe.csv"
MARKDOWN_DIR = "Reading List 23fae7025b0f44f4bfa3c0789a2bd8fe"
OUTPUT_FILE = "file_mapping.json"
MATCH_LENGTH = 50

def sanitize_title(title):
    """Removes special characters, converts to lowercase for matching."""
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    return sanitized.strip().lower()

def get_gemini_match(title, file_list):
    """Asks Gemini to find the best filename match for a given title."""
    if not API_KEY:
        print("Warning: GEMINI_API_KEY not found. Cannot perform AI matching.")
        return None

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    
    # Create a numbered list of files for the prompt
    file_options = "\n".join([f"{i+1}. {name}" for i, name in enumerate(file_list)])

    prompt = f"""
You are an expert file matching system. Your task is to find the single best filename from the provided list that matches the given article title.

Consider variations, special characters, and potential truncations. The correct filename is definitely in this list.

Article Title: "{title}"

Filename List:
{file_options}

Respond ONLY with the single, exact filename from the list that is the best match. Do not add any other text or explanation.
    """
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        json_response = response.json()
        match = json_response['candidates'][0]['content']['parts'][0]['text'].strip()
        # Final check to ensure Gemini returned a valid filename from the list
        if match in file_list:
            return match
        else:
            print(f"  - Gemini returned an invalid filename: '{match}'")
            return None
    except requests.exceptions.RequestException as e:
        print(f"  - Error calling Gemini API for matching: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"  - Error parsing Gemini matching response: {e}")
        return None


def main():
    print("Starting to regenerate file mapping with Gemini-assisted matching...")

    # 1. Read titles from CSV
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8-sig') as infile:
            reader = csv.DictReader(infile)
            article_titles = [row['Name'] for row in reader if row['Name']]
    except FileNotFoundError:
        print(f"Error: CSV file not found at {CSV_FILE}")
        return
    
    # 2. Get markdown filenames
    try:
        md_files = [f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')]
    except FileNotFoundError:
        print(f"Error: Markdown directory not found at {MARKDOWN_DIR}")
        return
        
    file_mapping = {}
    unmatched_titles = []
    available_files = set(md_files)

    # --- Pass 1: Direct Matching ---
    print("\n--- Pass 1: Attempting direct matching ---")
    for title in article_titles:
        sanitized = sanitize_title(title)[:MATCH_LENGTH]
        
        found_match = None
        for md_file in available_files:
            if md_file.lower().replace('.md', '').startswith(sanitized):
                found_match = md_file
                break
        
        if found_match:
            full_path = os.path.join(MARKDOWN_DIR, found_match).replace("\\", "/")
            file_mapping[title] = full_path
            available_files.remove(found_match) # Remove from pool
        else:
            unmatched_titles.append(title)
    
    print(f"Directly matched {len(file_mapping)} articles.")

    # --- Pass 2: Gemini Matching for remaining files ---
    if unmatched_titles and API_KEY:
        print(f"\n--- Pass 2: Using Gemini to match {len(unmatched_titles)} remaining titles ---")
        remaining_files = list(available_files)
        for i, title in enumerate(unmatched_titles):
            print(f"  - Matching '{title}' ({i+1}/{len(unmatched_titles)})...")
            gemini_match = get_gemini_match(title, remaining_files)
            
            if gemini_match:
                full_path = os.path.join(MARKDOWN_DIR, gemini_match).replace("\\", "/")
                file_mapping[title] = full_path
                remaining_files.remove(gemini_match) # Ensure it's not used again
                print(f"    -> Found: {gemini_match}")
            else:
                print("    -> No confident match found by Gemini.")

    # 4. Save the final mapping
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(file_mapping, f, indent=2)

    final_match_count = len(file_mapping)
    final_unmatched_count = len(article_titles) - final_match_count
    print(f"\nSuccessfully created new mapping for {final_match_count} articles.")
    print(f"Mapping saved to {OUTPUT_FILE}")
    if final_unmatched_count > 0:
        print(f"\nWarning: Still could not find a match for {final_unmatched_count} titles.")

if __name__ == "__main__":
    main()