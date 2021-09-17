N, K = map(int, input().split())
count=0

while N>=K:
    N, r = divmod(N, K)
    count+=r+1
count+=N-1

print(count)