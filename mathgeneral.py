#This module includes miscellaneous classes and functions that involve general mathematics

class variable:
    name=''
    value=0
    def changevalue(self,value,new):
        value=new
        return None
    def changename(self,name,new):
        name=new
        return None

def root(root,base):
    return base**(1/root)

def consec(x,y,z):
    a=0
    for i in range(x,y+z,z):
        a+=i
    return a

def intersection(set1,set2):
    output=[]

    for i in range(0,len(set1)):
        for j in range (0,len(set2)):
            if set1[i]==set2[j]:
                output.append(set1[i])
    return output

def union(set1,set2):
    output=[]
    included=False

    for i in range(0,len(set1)):
        if not (set1[i] in output):
            output.append(set1[i] * set1.count(set1[i]))

    for i in range(0,len(set2)):
        if not (set2[i] in output):
            output.append(set2[i] * set2.count(set2[i]))
    return output

def isprime(n):
    for i in range (2,int(n/2)+1):
        if n/i==n//i:
            return False
    return True

#This function finds the lowest prime factor in a number
def prime_core(n):
    if isprime(n)==True:
        return n
    else:
        for i in range(2,int(n/2)+1):
            if n/i==n//i:
                return prime_core(i)

def prime_factor(n):
    x=[]
    while n>1:
        x.append(int(prime_core(n)))
        n=n/(prime_core(n))
    return x

def primelist(n,k):
    x=[]
    for i in range(n,k+1):
        if isprime(i)==True:
            x.append(i)
    return x


def factor(n):
    x=[]
    for i in range (2,int(n/2)+1):
        if n/i==int(n/i):
            x.append(i)
    return x

def isperfect(n):
    x=factor(n)
    a=1

    for i in range (0,len(x)):
        a=a+x[i]

    if a==n:
        return True
    else:
        return False

def perfectlist(n,k):
    x=[]
    for i in range(n,k+1):
        if isperfect(i)==True:
            x.append(i)
    return x

def lcm_core(a,b):
    list1=prime_factor(a)
    list2=prime_factor(b)
    grandlist=[]
    output=1

    for i in range (0,len(list1)):
        if grandlist.count(list1[i])<list1.count(list1[i]):
            grandlist.append(list1[i])

    for i in range (0,len(list2)):
        if grandlist.count(list2[i])<list2.count(list2[i]):
            grandlist.append(list2[i])

    for i in range (0,len(grandlist)):
        output=output*grandlist[i]

    return output

def isnumber(q):
    for i in range(0,len(q)):
        if not((ord(q[i])>=48 and ord(q[i])<=57) or q[i]=='.'):
            return False
    return True

def s_to_d(fraction):
    numerator=int(fraction[0:fraction.find('/')])
    denominator=int(fraction[fraction.find('/')+1:-1])
    output=numberator/denominator
    return output

def d_to_s(decimal):
    i=int('9'*99999)
    j=i
    while i>0:
        while j>0:
            if i/j==decimal:
                return str(i)+'/'+str(j)
            j=j-1
        i=i-1
    return False
