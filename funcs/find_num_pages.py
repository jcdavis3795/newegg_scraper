# this script locates the total number of returned pages for the specified component type search
# you can use this to set the value of num_pages in get_ne_components.py to the value of page_count to scrape all pages for a
# given component type

from funcs import ne_urls
from bs4 import BeautifulSoup
import requests as req


def find_num_pages(component):

    url = ne_urls.urls[str(component)]

    r = req.get(url)
    source = r.content
    soup = BeautifulSoup(source, 'html.parser')

    page_text = soup.find('span', {'class': 'list-tool-pagination-text'}).text
    page_count = int(page_text.split('/')[1])

    print('scraping ', page_count, ' pages...')


find_num_pages('gpu')