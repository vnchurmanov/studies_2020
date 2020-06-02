# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input('Enter count:'))
pos = int(input ('Enter position:'))
url = input('Enter URL - ')
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    x = 0
    for tag in tags:
        if x == pos - 1:
            print('Retreiving: ', tag.get('href', None))
            url = tag.get('href', None)
            break
        else:
            x += 1
            continue
