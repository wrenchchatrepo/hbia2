#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def debug_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("Available selectors:")
    print("\n1. Main content areas:")
    for tag in soup.find_all(['main', 'article']):
        print(f"- {tag.name}")
        if tag.get('class'):
            print(f"  Classes: {tag.get('class')}")
    
    print("\n2. Content divs:")
    for div in soup.find_all('div', class_=True):
        print(f"- {div.get('class')}")
    
    print("\n3. Article body:")
    article_body = soup.find('div', class_='devsite-article-body')
    if article_body:
        print("Found devsite-article-body")
        print("First few elements:")
        for elem in article_body.find_all(recursive=False)[:5]:
            print(f"- {elem.name}: {elem.get('class', 'no class')}")

if __name__ == "__main__":
    url = "https://cloud.google.com/looker/docs/"
    debug_page(url) 