import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #crea un handle como con open() para abrin un archivo

#for line in fhand:
#    print(line.decode().strip()) #decode() devuelve un string
# las web page pueden manejarse como archivos
lst = list()
for line in fhand:
    line = line.decode().rstrip() #no olvidar el decode()
    wds = line.split()
    for i in wds:
        if i not in lst:
            lst.append(i)
lst.sort()               
print(lst)
