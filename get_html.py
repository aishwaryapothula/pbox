#AishwaryaPothula
#To get Html code of websites

import requests
import BeautifulSoup
url = 'http://facebook.com'
req = requests.get(url)
req_html = req.text
print(req_html)

soup = BeautifulSoup(r_html)
title = soup.find('span', 'articletitle').string
print(soup)

#req_html has the html code of facebook in a string format
#BeautifulSoup convert it into a hierarchical format
