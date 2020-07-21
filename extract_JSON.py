import urllib.request, urllib.parse, urllib.error
import json
import ssl

SUM = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
uh = urllib.request.urlopen(url, context=ctx).read()

data = uh.decode()

info = json.loads(data)

for item in info['comments']:
    SUM += item['count']
print(SUM)





