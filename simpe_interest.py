# to calculate simple interest
print("to calculate simple interest")
a=input("Enter your principle amout = ")
a=int(a)
b=input("Enter the time period for which you have to calculate S.I.(in years) = ")
b=int(b)
c=input("Enter the rate of interest per annum = ")
c=float(c)
d=(a*b*c)/100
d=float(d)
print ("Your simple interest for ", a , "at",c ,"% for", b, "years is", d)
e=a+d
e=float(e)
print("The amount you will get after", b, "years is",e)
