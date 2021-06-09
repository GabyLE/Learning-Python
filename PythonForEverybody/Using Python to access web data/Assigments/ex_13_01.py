import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


count = list()

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
stuff = ET.fromstring(data) #lee el string
lst = stuff.findall('comments/comment')#acomoda las etiquetas en una lista. una lista de mini arboles
print('User count:', len(lst))

for item in lst: #loop within the list of tags
    #print('Name', item.find('name').text)
    count.append(int(item.find('count').text))
    #print('Attribute', item.get('x'))
print(sum(count))