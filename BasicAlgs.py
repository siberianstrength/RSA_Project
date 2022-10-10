import random as rand
from math import log2

def generate(n):
    n -=1
    while True:
        a = (rand.randrange(1 << n - 1, 1 << n) << 1) + 1
        if miller_rabin(a):
            return a
        
def miller_rabin(n):
    r = int(2*log2(n))
    for i in range(r):
        if test(n):
            return True
    return False
        
def test(n):
    a = rand.randrange(2, n - 1)
    d = n - 1
    while not d & 1:
        d >>= 1      
    if pow(a, d, n) == 1:
        return True
    while d < n - 1:
        if pow(a, d, n) == n - 1:
            return True
        d <<= 1
    return False

def easyPowering(a,b,n):
    array = []
    array.append(a)
    s = []
    while b > 0:
        s.append(str(b%2))
        b = b//2
    s.reverse()
    for i in range(len(s)-1):
        if s[i+1] == '0':
            array.append(array[i]**2%n)
        else:
            array.append(array[i]**2*a%n)
    return array[len(array)-1] 

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
def gcd_ext(a, b):
    if b == 0:
        return a, 1, 0
    j, d, s = gcd_ext(b, a % b)
    d, s = s, d - (a // b) * s
    return j, d, s
