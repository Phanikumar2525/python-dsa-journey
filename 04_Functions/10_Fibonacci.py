def Fibonacci(n):
    a=0
    b=1
    list=[]
  
    for i in range(n):
        list.append(a)
        c=a+b
        a=b
        b=c
    return list
        
n=int(input("Enter n:"))
print(Fibonacci(n))    
