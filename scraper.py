import requests
from bs4 import BeautifulSoup

# Step 1: Website URL
url = "https://www.bbc.com/news"

# Step 2: Send GET request
response = requests.get(url)

# Step 3: Check if request successful
if response.status_code == 200:
    print("Website fetched successfully!")
else:
    print("Failed to fetch website")
    exit()

# Step 4: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Find all headlines (h2 tags)
headlines = soup.find_all("h2")

# Step 6: Save headlines into txt file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for idx, h in enumerate(headlines, start=1):
        title = h.text.strip()
        if title:   # avoid empty lines
            file.write(f"{idx}. {title}\n")

print("Headlines saved in headlines.txt file ✅")
