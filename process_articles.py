import os
import json
import requests
import pathlib
import csv
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
API_KEY = os.getenv("GEMINI_API_KEY")
MARKDOWN_DIR = "Reading List 23fae7025b0f44f4bfa3c0789a2bd8fe"
CSV_FILE = "Reading List 23fae7025b0f44f4bfa3c0789a2bd8fe.csv"
OUTPUT_FILE = "article_data.json"
SNIPPET_LENGTH = 8000 # Max characters to send to Gemini for context

# --- Helper Functions ---

def clean_gemini_output(raw_text):
    """Removes markdown code blocks from Gemini's JSON output."""
    return raw_text.replace("```json", "").replace("```", "").strip()

def analyze_with_gemini(text):
    """Sends text to the Gemini API for analysis."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
    
    prompt = f"""
    Analyze the following article content.
    1.  Categorize it into one of three categories: "Health", "Wealth", or "Work".
    2.  Generate exactly 3 relevant tags. Each tag MUST be a single, lowercase word.
    3.  Create a concise, 5-word summary.

    Respond ONLY with a valid JSON object in the following format:
    {{"category": "...", "tags": ["...", "...", "..."], "summary": "..."}}

    Article Content:
    {text}
    """

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        json_response = response.json()
        
        raw_text = json_response['candidates'][0]['content']['parts'][0]['text']
        cleaned_json = clean_gemini_output(raw_text)
        return json.loads(cleaned_json)

    except requests.exceptions.RequestException as e:
        print(f"Error calling Gemini API: {e}")
        return None
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Error parsing Gemini response: {e}")
        print(f"Raw response was: {json_response}")
        return None

def clean_markdown_content(text):
    """Removes the metadata header from the markdown file."""
    lines = text.split('\n')
    content_start_index = 0
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('created on:'):
            content_start_index = i + 1
            break
    
    while content_start_index < len(lines) and not lines[content_start_index].strip():
        content_start_index += 1
        
    return '\n'.join(lines[content_start_index:])

# --- Main Script ---

def main():
    print("Starting article processing...")
    
    # 1. Read CSV to get a map of Name -> {URL, CreatedOn}
    csv_data = {}
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8-sig') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                csv_data[row['Name']] = {
                    "url": row['Column'],
                    "created_on": row['created on']
                }
    except FileNotFoundError:
        print(f"Error: CSV file not found at {CSV_FILE}")
        return

    # 2. Create a mapping from markdown filename to article name
    try:
        with open('file_mapping.json', 'r', encoding='utf-8') as f:
            file_mapping = json.load(f)
        # Create a map of { "markdown_filename.md": "Article Title" }
        filename_to_name_mapping = {
            os.path.basename(path): name for name, path in file_mapping.items()
        }
    except FileNotFoundError:
        print("Error: file_mapping.json not found. Please ensure it has been created.")
        return

    # Load already processed articles to avoid re-processing
    all_article_data = []
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            try:
                all_article_data = json.load(f)
            except json.JSONDecodeError:
                print("Warning: Could not parse existing output file. Starting fresh.")
                all_article_data = []
    
    processed_titles = {item['title'] for item in all_article_data}
    
    markdown_files = list(pathlib.Path(MARKDOWN_DIR).glob("*.md"))
    total_files = len(markdown_files)
    
    print(f"Found {total_files} markdown files. {len(processed_titles)} already processed.")

    for i, md_path in enumerate(markdown_files):
        md_filename = md_path.name
        
        article_name = filename_to_name_mapping.get(md_filename)
        if not article_name:
            print(f"Processing file {i+1}/{total_files}: {md_filename}... SKIPPING (not in mapping)")
            continue

        if article_name in processed_titles:
            print(f"Processing file {i+1}/{total_files}: {md_filename}... SKIPPING (already processed)")
            continue
            
        print(f"Processing file {i+1}/{total_files}: {md_filename}...")
            
        article_csv_info = csv_data.get(article_name)
        if not article_csv_info:
            print(f"  - Skipping, could not find CSV info for '{article_name}'")
            continue

        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                full_content = f.read()
            
            cleaned_content = clean_markdown_content(full_content)
            
            if len(cleaned_content) > SNIPPET_LENGTH:
                cleaned_content = cleaned_content[:SNIPPET_LENGTH] + "..."

            if not cleaned_content.strip():
                print("  - Skipping, no content after cleaning.")
                continue

            gemini_analysis = analyze_with_gemini(cleaned_content)
            
            if gemini_analysis:
                new_article = {
                    "title": article_name,
                    "url": article_csv_info["url"],
                    "created_on": article_csv_info["created_on"],
                    "markdown_file": str(md_path).replace('\\', '/'),
                    "category": gemini_analysis.get("category", "Uncategorized"),
                    "tags": gemini_analysis.get("tags", []),
                    "summary": gemini_analysis.get("summary", "No summary available.")
                }
                all_article_data.append(new_article)
                
                # Write to file after each successful processing
                with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                    json.dump(all_article_data, f, indent=2)
                
                print("  - Success. Data saved.")
            else:
                print("  - Failed to get analysis from Gemini.")

        except Exception as e:
            print(f"  - An error occurred: {e}")
        
    print(f"\nProcessing complete. All data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()