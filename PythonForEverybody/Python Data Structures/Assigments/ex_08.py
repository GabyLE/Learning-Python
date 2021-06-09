han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    #print("Line:", line) para revisar
    wds = line.split()
    #print("Words:",wds) para revisar
    #Patron guardian mejor
    #if len(wds) < 3:
        #continue
    #Guardian in a compound statement
    if len(wds) < 3 or wds[0] != "From":
        #print("Ignore") para revisar
        continue
    print(wds[2])