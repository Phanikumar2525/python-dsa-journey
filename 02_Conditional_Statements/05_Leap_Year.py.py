year=int(input("Enter a:"))

if year%400 ==0:
    print(year,"is leap year")
elif year%100==0:
    print(year,"is not a leap year")
elif year%4==0:
    print(year,"is leap year")  
else:
    print(year,"is not a leap year")  
