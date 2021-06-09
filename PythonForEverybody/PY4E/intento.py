def computepay(h,r):
    h =float(h)
    r = float(r)
    if h > 40:
        extra = h - 40
        pay =40*r + extra*r*1.5
    else:
        pay = h*r
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print(p)
