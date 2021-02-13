# newegg_scraper
This is a web scraper for pulling PC components and prices by component type from Newegg.com. This program has some simple command line functionality. You run ne_scrape.py the same way you would run any other python file from the console, with the addition of two arguments. You will specify the component type and the number of results you want returned. 
For example, this command in Windows will return the first 20 CPUs:

python3 ne_scrape.py cpu 20

The accepted component type commands are:

'cpu', 'gpu', 'mobo_intel', 'mobo_amd', 'memory', 'psu', 'hdd', 'ssd', 'cpu_fan', 'case_fan', 'case'

By default, the script takes the first 120 results and stores them in a list to pull your results from.
The script scrapes the first two pages ordered by best selling --> worst selling with 60 results per page.
If you want more than 120 results, you can easily increase the number of pages to be scraped by modifying
the num_pages variable on line 17 in get_ne_components.py. 

If you want to scrape every item of a specified component you can use the find_num_pages.py function
find_num_pages() to return the total amount of pages for that component, and then set num_pages to that
result. 
