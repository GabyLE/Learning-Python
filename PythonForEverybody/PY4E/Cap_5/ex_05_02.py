largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        num = float(num) #la linea que causa el problema se pone en el try/except
    except:
        print("Invalid data")
        continue #vuelve al inicio del ciclo
    if largest is None:
        largest = num
        smallest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimun is", smallest)
