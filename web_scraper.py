import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2")
    file = open("headlines.txt", "w", encoding="utf-8")

    numbering = 1
    for headline in headlines:
        text = headline.get_text().strip()
        if text:
            file.write(str(numbering) + ". " + text + "\n")
            numbering += 1

    file.close()
    print("Headlines saved to 'headlines.txt'")
else:
    print("Failed to fetch the page.")
