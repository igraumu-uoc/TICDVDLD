import cloudscraper
from bs4 import BeautifulSoup
import re
import time

URL = "https://www.filmaffinity.com/es/cat_new_th_es.html"

def obtenir_ids_cartellera(url):
    # Crea un scraper que imita un navegador real (executa JS i cookies)
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "mobile": False}
    )

    print(f"🔎 Accedint a {url} ...")
    response = scraper.get(url, timeout=15)
    print(f"Codi d’estat: {response.status_code}")

    if response.status_code != 200:
        print(f"Error {response.status_code} accedint a la pàgina")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar totes les etiquetes <a> amb classe poster-wrap
    links = soup.find_all("a", class_="poster-wrap")

    ids = []
    for link in links:
        href = link.get("href", "")
        match = re.search(r"film(\d+)\.html", href)
        if match:
            ids.append(match.group(1))

    print(f"S'han trobat {len(ids)} pel·lícules en cartellera.")
    return ids


if __name__ == "__main__":
    time.sleep(2)
    ids = obtenir_ids_cartellera(URL)
    print("IDs trobats:", ids)

