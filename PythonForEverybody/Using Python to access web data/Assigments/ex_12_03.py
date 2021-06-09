from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
num = list()

tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print(tag.get('class', None))
    num.append(float(tag.contents[0]))
    
print(sum(num))
    #print('Attrs:', tag.attrs)