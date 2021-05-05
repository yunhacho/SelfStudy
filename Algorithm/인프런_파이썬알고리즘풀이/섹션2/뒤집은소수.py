def reverse(x):
    return int(x[::-1])
def isPrime(x):
    isprime=True
    for i in range(2, x):
        if x%i==0:
            isprime=False
            break
    return isprime if x>1 else False

N=int(input())
numbers=input().split()
res=[]
for n in numbers:
    if isPrime(reverse(n)): res.append(reverse(n))
print(*res, sep=' ')