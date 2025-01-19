import requests
from bs4 import BeautifulSoup

def scrape_and_search(url, search_term):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        return f"Failed to fetch the webpage. Error: {e}"

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    elements = soup.find_all(text=lambda text: text and search_term.lower() in text.lower())
    
    for element in elements:
        parent = element.parent
        if parent.name == 'a' and parent.has_attr('href'):
            results.append(f"Link: {element.strip()} (URL: {parent['href']})")
        else:
            results.append(f"{parent.name.capitalize()}: {element.strip()}")

    return '\n'.join(results) if results else "No relevant information found."
