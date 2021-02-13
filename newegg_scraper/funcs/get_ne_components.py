from funcs import print_results, ne_urls
from bs4 import BeautifulSoup
import requests as req

# initialize empty list
links = []
results = []


# This function will do the scraping and store all returned results in a list
def get_ne_components(component, num_returns):

    url = ne_urls.urls[str(component.lower())]

    # the default number of pages we will scrape before stopping, returning 120 results at 60 per page
    # simply changing the value of num_pages will allow you to scrape more content
    num_pages = 2
    p1 = 0
    p2 = 1

    # I iterated through the pages by manually changing the url string and placing these urls in a list
    for page in range(num_pages):

        url = url.replace(f'Page-{p1}', f'Page-{p2}')
        links.append(url)

        p1 += 1
        p2 += 1

    index = 0
    num_links = len(links)

    for link in range(num_links):
        # Now we iterate through the list of links we created earlier and, using nested 'for' loops, scrape the data
        # that we want from each page
        ne_r = req.get(links[index])
        ne_source = ne_r.content
        ne_soup = BeautifulSoup(ne_source, 'html.parser')

        for item in ne_soup.find_all('div', {'class': 'item-container'}):

            names = []
            prices = []

            try:
                names.append(item.find('a', {'class': 'item-title'}).text.strip('\n').strip(' ').strip('\n'))
            except AttributeError:
                continue

            for price in item.find_all('li', {'class': 'price-current'}):

                try:
                    prices.append(''.join([price.strong.text.strip(), price.sup.text.strip()]))
                except AttributeError:
                    continue
            # zip our two lists together so that we can use enumerate
            items_prices = zip(prices, names)
            # formatting the string that will go into the final list
            for n, (price, name) in enumerate(items_prices):
                results.append('{n} : ${p}'.format(p=price, n=name))

        index += 1

    print_results.print_results(results, num_returns)