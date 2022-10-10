import random as r
from googletrans import Translator
from math import log2
import random 
rand = random.SystemRandom()

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

def EC(fn):
    lst = []
    for i in range(fn):
        if gcd(i,fn) == 1:
            lst.append(i)
    try:
        return lst[r.randint(0,len(lst)-1)]
    except: 
        return lst[0]
    
def DC(e,fn):
    return gcd_ext(e,fn)[1]

def encrypt(msg,data):
    return[easyPowering(i,data[0],data[1]) for i in msg]

def decrypt(msg,data):
    return[easyPowering(i,data[0],data[1]) for i in msg]

def create_e_d(fn,n):
    e = EC(fn)
    d = DC(e, fn)
    return e,d

def RSA(byte):  
    p = generate(byte)
    q = generate(byte)
    if q < p:
        p,q = q,p
    n = p*q
    fn = (q-1)*(p-1)
    with open("input.txt", "r") as inp:
        s = inp.read()
    sarray = []
    for i in range(len(s)):
        sarray.append(ord(s[i]))
    e,d = create_e_d(fn,n)
    while d == None:
        create_e_d(fn,n)
    enc_data = [e,n]
    dec_data = [d,n]
    encryptedMsg = encrypt(sarray,enc_data)
    encryptedMsg_string = str(encryptedMsg[:])
    with open("output_numbers.txt", "w") as out:
        out.write(encryptedMsg_string)
    decryptedMsg = decrypt(encryptedMsg,dec_data)
    check = True
    for i in range(len(decryptedMsg)):
        if decryptedMsg[i] > 122:
            check = False
            break
    if check:
        st = ""
        for i in range(len(decryptedMsg)):
            st+=chr(decryptedMsg[i])
        with open("output_text.txt", "w") as outt:
            outt.write(st)
        trs = Translator()
        final_output = trs.translate(st, src = "en", dest = "ru")
        with open("output_text_trs.txt", "w") as outtrs:
            outtrs.write(final_output.text)
        print("p:", p)
        print("q:", q)
        print("n:", n)
        print("fn:", fn)
        print("Public key:", e)
        print("Private key:", d)
        print(final_output.text,"\n")
    else:
        RSA(byte)
        
RSA(10)