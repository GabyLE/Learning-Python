sc = input("Enter Score: ")
try:
    score = float(sc)
except:
    print("Error, please enter a numeric input")
    quit()
if 0.0 <= score <= 1.0:
    if score >=0.9:
        print("A")
    elif score >=0.8:
        print("B")
    elif score >=0.7:
        print("C")
    elif score >=0.6:
        print("D")
    else:
        print("F")
else:
    print("Error, please enter a value between the range")
