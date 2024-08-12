from bs4 import BeautifulSoup
import requests
import pandas as pd

class WebScraper:
    def __init__(self):
        self.url = ""
        self.tags = []
        self.classes = []
        self.ids = []
        self.extensions = []

    def set_url(self, url):
        self.url = url

    def add_tag(self, tag):
        self.tags.append(tag)

    def add_class(self, class_):
        self.classes.append(class_)

    def add_id(self, id_):
        self.ids.append(id_)

    def add_extension(self, extension):
        self.extensions.append(extension)

    def scrape(self):
        try:
            # Send an HTTP GET request to the URL and get the HTML content
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Parse the HTML content with Beautiful Soup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all elements that match the specified criteria
            elements = []
            for tag in self.tags:
                for class_ in self.classes:
                    for id_ in self.ids:
                        elements.extend(soup.find_all(tag, class_=class_, id=id_))

            # Filter elements by file extension
            filtered_elements = []
            for element in elements:
                for extension in self.extensions:
                    if element['href'].endswith(extension):
                        filtered_elements.append(element)

            return filtered_elements

        except requests.exceptions.RequestException as e:
            print("Error fetching the page:", e)
            return []
        except Exception as e:
            print("Error:", e)
            return []

if __name__ == "__main__":
    scraper = WebScraper()

    url = input("Enter the URL to scrape: ")
    scraper.set_url(url)

    tags = input("Enter the HTML tags separated by commas (e.g., a, img): ").split(',')
    for tag in tags:
        scraper.add_tag(tag.strip())

    classes = input("Enter the classes separated by commas (leave blank for none): ").split(',')
    for class_ in classes:
        if class_.strip():
            scraper.add_class(class_.strip())

    ids = input("Enter the IDs separated by commas (leave blank for none): ").split(',')
    for id_ in ids:
        if id_.strip():
            scraper.add_id(id_.strip())

    extensions = input("Enter the file extensions separated by commas (e.g., pdf, jpg): ").split(',')
    for extension in extensions:
        scraper.add_extension(extension.strip())

    elements = scraper.scrape()
    for element in elements:
        print(element)