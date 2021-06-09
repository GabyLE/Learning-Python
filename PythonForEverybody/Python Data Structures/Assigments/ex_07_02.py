#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an 
# output as shown below. Do not use the sum() function or a variable named sum in your solution.
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
valSum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pointpos = line.find(":") #encuentra la posición donde aparece por primera vex ":"
    num = line[pointpos+1:]#asigna lo que hay desde una posición despues del ":" hasta el final
    num = num.strip()#elimina los espacios al principio y final
    val = float(num) #convierte la cadena en numero decimal
    valSum = val + valSum
    count = count + 1
valProm = valSum/count
print("Average spam confidence:", valProm)