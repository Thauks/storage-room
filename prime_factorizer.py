# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 17:06:43 2021

@author: mestr
"""
from decimal import getcontext,Decimal

getcontext().prec = 100

def is_prime(p):
    if p == 0 or p == 1: return False
    if p > 1:
        for i in range(2, int(p/2)+1):
            if (p % i) == 0:
                return False
        return True

def find_primes(n, limit, max_primes):
    plist = []
    if limit < n:
        n *= -1
          
    while (n < limit and len(plist) < max_primes):
        if is_prime(abs(n)):
            plist.append(abs(n))
        n += 2
            
    return plist

def factorize_depth(n):
    th = int(Decimal(n).sqrt())
    if th%2 == 0:
        p = th+1
        q = th-1
    else:
        p = th+2
        q = th

    plist = find_primes(p, p+q, 1000)
   #print(plist)
    qlist = find_primes(q, 0, 1000)
    #print(qlist)
    
    for i in plist:
        for j in qlist:
            if i*j == n:
                 return i,j
    return None

def factorize_close(n):
    q = int(Decimal(n).sqrt())
    if q%2 == 0:
        q = q-1
    
    while (n%q != 0):
        q -= 2
    
    return int(n/q),q
 
#print(factorize_depth(2590591607))
print(factorize_close(2590591607))
print(factorize_close(123459259296296790129629703704567911111222220989329646370537655992609296463211544461111289984805767))