#Open the file romeo.txt and read it line by line. For each 
#line, split the line into a list of words using the split()
#method. The program should build a list of words. For each 
#word on each line check to see if the word is already in 
#the list and if not append it to the list. When the program 
#completes, sort and print the resulting words in alphabetical 
#order.
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    wds = line.split()
#     if len(lst)<1:
#         lst = wds
#     else:
#         for i in wds:
#             var = 0
#             for x in lst:
#                if i == x:
#                    var = 1
#                    continue
#             if var == 0:
#                lst.append(i)
#    for i in wds:
#        var = 0
#        if i in lst:
#            var = 1
#            continue
#        if var == 0:
#            lst.append(i)
    for i in wds:
        if i not in lst:
            lst.append(i)
lst.sort()               
print(lst)

