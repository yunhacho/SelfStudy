X=int(input())
dp=[0]*(X+1)
for x in range(2, X+1):
    if x%6==0: dp[x]=min(dp[x//3]+1,dp[x//2]+1, dp[x-1]+1)
    elif x%3==0: dp[x]=min(dp[x//3]+1, dp[x-1]+1)
    elif x%2==0: dp[x]=min(dp[x//2]+1, dp[x-1]+1)
    else: dp[x]=dp[x-1]+1
print(dp[X])