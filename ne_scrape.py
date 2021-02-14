from funcs import get_ne_components
import sys
# command line functionality. From the terminal in the project directory, run 'ne_scrape.py' the way you would normally
# run a python file followed by two additional arguments: component type and the number of items you want returned

if __name__ == '__main__':
    try:
        if sys.argv[1] in get_ne_components.ne_urls.a_comp:
            get_ne_components.get_ne_components(sys.argv[1], int(sys.argv[2]))

        elif sys.argv[1] not in get_ne_components.ne_urls.a_comp:
            print('error: component type not found')

        elif sys.argv[2] is not int:
            print('Specify the number of results you want returned with an integer.')

    except IndexError:
        print('Please enter your query in the correct format: '
              '"python3 get_ne_components.py [component type] [num of items to return]"')
