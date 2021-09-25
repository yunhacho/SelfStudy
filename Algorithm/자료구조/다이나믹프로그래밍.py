# 개미전사
def dp_1(N, K):
    dp=[0]*N; dp[0]=K[0]; dp[1]=max(K[:2])
    for i in range(2,N):dp[i]= max(dp[i-2]+K[i], dp[i-1])
    return dp[N-1]
print(dp_1(4,[1,3,1,5])) #8

# 1로 만들기
def dp_2(X):
    dp=[0]*(X+1)
    for x in range(2, X+1):
        if x%6==0: dp[x]=min(dp[x//3]+1,dp[x//2]+1, dp[x-1]+1)
        elif x%3==0: dp[x]=min(dp[x//3]+1, dp[x-1]+1)
        elif x%2==0: dp[x]=min(dp[x//2]+1, dp[x-1]+1)
        else: dp[x]=dp[x-1]+1
    return dp[X]
print(dp_2(10)) #3

#효율적인 화폐구성
def dp_3(N, M, coin):
    dp=[10001]*(M+1); dp[0]=0
    for c in coin:
        for i in range(c, M+1):
            dp[i]=min(dp[i], dp[i-c]+1)
    return dp[M] if dp[M]<10001 else -1
print(dp_3(2,15,[2,3])) #5
print(dp_3(3,4,[3,5,7])) #-1

#금광
def dp_4(n,m, golds):
    dp=[]
    pass
print(dp_4(3,4,[1,3,3,2,2,1,4,1,0,6,4,7]))
