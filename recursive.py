#This file contains work done on recursive functions
#For the prime_core(n) function, which is highly useful, see the mathgeneral module

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

def gauss(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

def fib(n):
    if n==1 or n==0:
        return n
    else:
        return fib(n-1)+fib(n-2)

def palindrome(word):
    if word[0]==word[-1]:
        if len(word)==2 or len(word)==3:
            return True
        else:
            word=word.lstrip(1)
            word=word.rstrip(1)
            return palindrome(word)
    else:
        return False
