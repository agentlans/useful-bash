from bs4 import BeautifulSoup
import sys
import requests

# Prints hyperlinks in the HTML files
def ahref(html_file, print_filename=False):
    try:
        with open(html_file) as f:
            html_doc = f.read()
    except:
        # Treat it like an URL
        r = requests.get(html_file)
        html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    for link in soup.find_all('a'):
        h = link.get('href')
        if h:
            if print_filename:
                print("{}\t{}".format(html_file, h))
            else:
                print(h)

if len(sys.argv) == 1:
    print("Parses HTML files and prints their hyperlinks")
    print("Usage: python print_links.py [html_files...]")

# Whether we need to print which file the links are from
many_files = False
if len(sys.argv) > 2:
    many_files = True

for f in sys.argv[1:]:
    try:
        ahref(f, many_files)
    except:
        eprint("Couldn't open {}.".format(f))

