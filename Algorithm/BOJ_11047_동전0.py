# 그리디 알고리즘
N, K=list(map(int,input().split()))
coins=[]; count=0
for i in range(N):
    coins.append(int(input()))
    if coins[i] <= K: idx=i

while K>0 and idx>-1:
    count+=K//coins[idx]
    K%=coins[idx]
    idx-=1
print(count)