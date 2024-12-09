import requests
from urllib.parse import urlparse, urljoin
import re

def get_domain(url):
	parsed = urlparse(url)

	if parsed.scheme != 'http' and parsed.scheme != 'https':
		return ''

	return parsed.scheme + '://' + parsed.netloc

class RequestGuard:
	def __init__(self, domain):
		self.domain = get_domain(domain)
		self.forbidden = self.parse_robots()

	def parse_robots(self):
		robots_url = urljoin(self.domain, '/robots.txt')
		response = requests.get(robots_url)
		disallowed = []
		
		for line in response.text.split('\n'):
			if line.startswith('Disallow:'):
				disallowed.append(line.split(':', 1)[1].strip())
		
		return disallowed

	def can_follow_link(self, link):
		parsed = urlparse(link)
		if get_domain(link) != self.domain:
			return False
		
		path = parsed.path
		
		for forbid in self.forbidden:
			if path.startswith(forbid):
				return False
		
		return True

	def make_get_request(self, url, use_stream=False):

		if not self.can_follow_link(url):
			return None
		
		return requests.get(url, stream=use_stream)