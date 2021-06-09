#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
#Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475  "
pointpos = text.find(":") #encuentra la posición donde aparece por primera vex ":"
num = text[pointpos+1:]#asigna lo que hay desde una posición despues del ":" hasta el final
numnosp = num.strip()#elimina los espacios al principio y final
float(numnosp) #convierte la cadena en numero decimal
print(numnosp) #imprime el numero