import requests
url = 'http://facebook.com'
req = requests.get(url)
req_html = req.text
print(req_html)
