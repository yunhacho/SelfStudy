n,k=map(int, input().split())
a=sorted(map(int, input().split()))
b=sorted(map(int ,input().split()), reverse=True)

for i in range(k):
    a[i]=b[i]
print(sum(a))