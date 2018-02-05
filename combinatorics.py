def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

def choose(n,k):
    a=factorial(n)/(factorial(k)*factorial(n-k))
    return a

def permute(n,l):
    output=factorial(n)
    for i in range(0,len(l)):
        output=output/factorial(n-l[i])
    return int(output)

def gauss(n):
    if n==1:
        return 1
    else:
        return n+gauss(n-1)

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)
