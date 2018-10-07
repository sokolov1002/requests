import requests


def get_request(url):
	r = requests.request('GET', url)
	return r
