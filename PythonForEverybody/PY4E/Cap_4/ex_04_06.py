def computepay(h,r):
    h=float(h)
    r=float(r)
    if h<40:
        pay=h*r
    else:
        extra=h-40
        pay=(40*r)+(extra*r*1.5)
    return pay

hrs = input("Enter Hours: ")
rt=input("Enter Rate: ")
p = computepay(hrs,rt)
print(p)
