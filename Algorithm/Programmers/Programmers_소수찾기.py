from itertools import permutations
import math

def solution(numbers):
    set_of_n=set()
    
    for i in range(len(numbers)):
        for number in permutations(numbers, i+1):
            set_of_n.add(int(''.join(list(number))))
    
    count=0
    for n in set_of_n: 
        if isPrime(n): count+=1
    return count

def isPrime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True