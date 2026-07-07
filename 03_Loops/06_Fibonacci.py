#Using Two Variables-method-1

n=int(input("Enter n:"))
a=0 #initial values
b=1
for i in range(n):
    print(a)
    c=a+b #next = previous + current
    a=b #previous = current
    b=c #current = next1
    
# Using a List
n = int(input("Enter the number of terms: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib)
    
