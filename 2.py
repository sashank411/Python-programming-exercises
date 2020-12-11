n=int(input("enter a natural number to find the factorial of:"))
def f(n):
    if n==1:
        return(1)
    else:
        return(n*f(n-1))

fact= f(n)
print(fact)
