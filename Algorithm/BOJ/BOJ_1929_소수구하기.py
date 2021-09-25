import math
M,N=map(int, input().split())
prime=[False]*2+[True]*(N-1)
for i in range(2, int(math.sqrt(N))+1):
    if prime[i]: 
        for j in range(i*i, N+1, i): prime[j]=False
print("\n".join(map(str, [i for i in range(M,N+1) if prime[i]])))