a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

if a>b and a >c: #there is no && because python is english like lan
    print(a,"is larger")
elif b>a and b>c:
    print(b,"is larger")
else:
    print(c,"is larger")
