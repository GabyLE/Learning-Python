hrs=input("Enter Hours: ")
h=float(hrs)
rate=input("Enter Rate: ")
rt=float(rate)
if h<40:
    pay=h*rt
else:
    extra=h-40
    pay=(40*rt)+(extra*rt*1.5)
print(pay)
