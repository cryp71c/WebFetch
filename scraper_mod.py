from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.DataFrame(columns=["Text", "URL"])

# URL to fetch HTML from
url = "https://archive.org/details/practical-electronics-for-inventors-4th-edition-by-paul-scherz-simon-monk-z-lib.org"

try:
    # Send an HTTP GET request to the URL and get the HTML content
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    # Parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> elements with the specified class
    links = soup.find_all('a', class_='format-summary download-pill')

    print(links)

    # Iterate over the found links
    for link in links:
        row = {'Text' : link.get_text(), 'URL': link['href']}
        df = df.append(row, ignore_index=True)

except requests.exceptions.RequestException as e:
    print("Error fetching the page:", e)
except Exception as e:
    print("Error:", e)

#df['URL'] = df['URL'].str.removeprefix("/download")
df = df.loc[df['URL'].str.contains("pdf") | df['URL'].str.contains('PDF')]
pdfs = df['URL'].to_list()

with open("url_file.txt", 'w') as f:
    for i in pdfs:
        f.write(i+"\n")

f.close()