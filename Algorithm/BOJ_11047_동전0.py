# 그리디 알고리즘

def greedy_ver1(N,K):
    coins=[]; count=0
    for i in range(N):
        coins.append(int(input()))
        if coins[i] <= K: idx=i

    while K>0 and idx>-1:
        count+=K//coins[idx]
        K%=coins[idx]
        idx-=1
    return count

def greedy_ver2(N,K):
    coins=[]; count=0
    for i in range(N): 
        coins.append(int(input()))
        if coins[i]<=K: idx=i
    
    for c in coins[idx::-1]:
        m, K = divmod(K, c)
        count+=m

    return count

if __name__=="__main__":
    N, K=list(map(int,input().split()))
    print(greedy_ver1(N,K))
    N, K=list(map(int,input().split()))
    print(greedy_ver2(N,K))