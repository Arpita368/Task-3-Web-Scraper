# 📰 Task 3: Web Scraper for News Headlines

## 🎯 Objective
Automate the collection of top news headlines from a public website and save them into a text file.

---

## 🛠 Tools & Libraries
- **Python 3**
- **requests** – For sending HTTP requests to fetch the HTML page  
- **BeautifulSoup (bs4)** – For parsing HTML and extracting headlines  

---

## 📂 Files in the Project
- `web_scraper.py` – Python script to scrape headlines  
- `headlines.txt` – Output file containing scraped headlines  

---

## 📜 How It Works
1. **Send Request** – The script sends a GET request to the BBC News website.  
2. **Parse HTML** – BeautifulSoup parses the HTML content.  
3. **Extract Headlines** – All `<h2>` tags (headlines) are collected.  
4. **Save to File** – Headlines are numbered and written into `headlines.txt`.  

---

## 💻 Code Example
```python
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
```
## Author
Created by Arpita Jitendra Sonparote

## Licence
This scipt is for educational purposes. You can use it or modify it as per your need.
