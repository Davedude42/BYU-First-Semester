import requests
import bs4
import sys


url = sys.argv[1]
tag = sys.argv[2]
attr = sys.argv[3]
output = sys.argv[4]

with open(output, 'w') as file:
		
		finalContent = None
		
		while finalContent is None:

			soup_object = bs4.BeautifulSoup(requests.get(url).content, features="html.parser")

			elements = soup_object.find_all(tag)

			for el in elements:
				if 'final' in el.attrs:
					finalContent = el.get('final')
					break
				if attr in el.attrs:
					url, tag, attr = el.get(attr).split(',')

		
		file.write(finalContent)