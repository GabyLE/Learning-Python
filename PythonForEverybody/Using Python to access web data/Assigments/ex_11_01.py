import re
#The sum for the sample text above is 27486. The numbers can appear anywhere in the line. 
# There can be any number of numbers in each line (including none).
#Handling The Data
#The basic outline of this problem is to read the file, look for integers using the re.findall(), 
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and 
#summing up the integers.
num = list()
file = input("Enter file name:")
if len(file) < 1 : file = "regex_sum_42.txt"
handle = open(file)
for line in handle:
    line = line.rstrip()
    varios = re.findall("[0-9]+",line)
    for i in varios:
        num.append(float(i))
print(sum(num))


