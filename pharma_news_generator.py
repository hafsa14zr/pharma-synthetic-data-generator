import json
import csv
import random
from datetime import datetime, timedelta
import os

# Configuration
TOTAL_ARTICLES = 1_000_000
OUTPUT_FOLDER = r"C:\Users\hafsa\OneDrive\Documents\PharmaNews_2025"

# Data Sources
DRUGS = ["NovoVax", "CureX-25", "ImmunoBlast", "NeuroRegen", "OncoShield"]
COMPANIES = ["Pfizer", "Novartis", "Johnson & Johnson", "Roche", "Merck"]
AUTHORS = ["Dr. Emily Zhang", "Dr. Michael Chen", "Dr. Sarah Johnson", "Dr. David Lee"]
TAG_CATEGORIES = ["FDA Approval", "Clinical Trial", "Breakthrough", "Biotech", "Research"]

def generate_article(article_id):
    """Generate one article with all required metadata"""
    drug = random.choice(DRUGS)
    company = random.choice(COMPANIES)
    pub_date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 364))
    
    return {
        "Title": f"{company}'s {drug} Shows Promise in New 2025 Study",
        "URL": f"https://pharmanews.com/{company.lower()}/{drug.lower()}-{article_id}",
        "Full content": (
            f"In a landmark 2025 study published in The New England Journal of Medicine, "
            f"{company}'s {drug} demonstrated {random.randint(75, 95)}% efficacy in "
            f"Phase {random.choice(['II', 'III'])} clinical trials. The {random.choice(['oral', 'injectable'])} "
            "formulation showed statistically significant results across "
            f"{random.randint(500, 5000)} patients worldwide."
        ),
        "Date of publication": pub_date.strftime("%Y-%m-%d"),
        "Tags or keywords": [
            drug,
            company,
            random.choice(TAG_CATEGORIES),
            f"2025 Innovation",
            random.choice(["Oncology", "Cardiology", "Neurology"])
        ],
        "Author": random.choice(AUTHORS)
    }

def generate_all_articles():
    """Generate and save all articles"""
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    json_path = os.path.join(OUTPUT_FOLDER, "pharma_articles_2025.json")
    csv_path = os.path.join(OUTPUT_FOLDER, "pharma_articles_2025.csv")
    
    print(f"Generating {TOTAL_ARTICLES:,} articles with full metadata...")
    
    with open(json_path, 'w') as json_file, open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        # Initialize JSON file
        json_file.write('[\n')
        
        # Initialize CSV writer
        csv_writer = None
        
        for i in range(TOTAL_ARTICLES):
            article = generate_article(i)
            
            # Write JSON
            if i > 0:
                json_file.write(',\n')
            json.dump(article, json_file, indent=2)
            
            # Write CSV
            if i == 0:
                csv_writer = csv.DictWriter(csv_file, fieldnames=article.keys())
                csv_writer.writeheader()
            csv_writer.writerow(article)
            
            # Progress update
            if (i + 1) % 100_000 == 0:
                print(f"Generated {i + 1:,} articles...")
        
        # Close JSON array
        json_file.write('\n]')
    
    print(f"\n✅ Done! Files saved to:\n{OUTPUT_FOLDER}")
    print("• pharma_articles_2025.json")
    print("• pharma_articles_2025.csv (Open in Excel)")

if __name__ == "__main__":
    generate_all_articles()