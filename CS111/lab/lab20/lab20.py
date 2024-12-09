import requests
from urllib.parse import urlparse, urljoin


def get_domain(url):
	parsed = urlparse(url)

	if parsed.scheme != 'http' and parsed.scheme != 'https':
		return ''

	return parsed.scheme + '://' + parsed.netloc


def combine_paths(url, path):
	parsed = urlparse(url)

	return urljoin(get_domain(url), path)

def combine_urls(url1, url2):

	return urljoin(url1, url2)

def print_pages(url, paths, outputFile):
	txt = ''
	prevFolder = ''
	for path in paths:

		if path[0] == '/':
			combined = urljoin(get_domain(url), path)
			prevFolder = combined
		else:
			combined = urljoin(prevFolder, path)

		print(url, path, combined)

		txt += requests.get(combined).text + '\n'

	
	with open(outputFile, 'w') as file:
		file.write(txt)

