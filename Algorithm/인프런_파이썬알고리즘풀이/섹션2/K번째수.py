T=int(input())

result=[]
for _ in range(T):
    n,s,e,k=list(map(int, input().split()))
    result.append(sorted(list(map(int,input().split()))[s-1:e])[k-1])

for i, r in enumerate(result):
    print('#',i+1, ' ', r)