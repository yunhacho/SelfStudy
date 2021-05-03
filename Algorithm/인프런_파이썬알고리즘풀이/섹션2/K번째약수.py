N, K=list(map(int, input().split()))
cnt=0
for i in range(N, 0, -1):
    if N%i==0:
        cnt+=1
        if cnt==K:
            print(N//i); exit(0)

print(-1)
