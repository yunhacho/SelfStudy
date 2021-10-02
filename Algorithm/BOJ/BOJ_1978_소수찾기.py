import math
def isPrime(n):
    if n==1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def Prime(numbers):
    max_num=max(numbers)
    prime=[True]*(max_num+1)
    prime[0], prime[1] = False, False

    for i in range(2, int(math.sqrt(max_num))+1):
        if prime[i]:
            for j in range(i+i, max_num+1, i):
                prime[j]=False
    return sum(prime[n] for n in numbers if prime[n]==True)

n=int(input())
numbers=list(map(int, input().split()))
count=0
for i in numbers:
    if isPrime(i): count+=1
print(count)
print(Prime(numbers))
