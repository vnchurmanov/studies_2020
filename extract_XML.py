import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

SUM = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
uh = urllib.request.urlopen(url, context=ctx).read()

data = uh.decode()
tree = ET.fromstring(data)

counts = tree.findall('.//comment')

for count in counts:
    m = int(count.find('count').text)
    SUM += m

print(SUM)
