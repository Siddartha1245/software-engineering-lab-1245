a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
d=(b*b)-(4*a*c)
if d>=0:
    r1=(-b+d**0.5)/(2*a)
    r2=(-b-d**0.5)/(2*a)
    print("The roots are:",r1,r2)
else:
    print("No real roots")