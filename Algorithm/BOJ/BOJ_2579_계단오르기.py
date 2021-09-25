
n=int(input())
stairs=[int(input()) for i in range(n)]
dp=[0]*n

dp[0]=stairs[0]

if n>1:
    dp[1]=max(dp[0]+stairs[1], stairs[1])
    if n>2:
        dp[2]=stairs[2]+max(stairs[0], stairs[1])
        if n>3:
            for floor in range(3, n):
                dp[floor]=stairs[floor]+max(dp[floor-2], dp[floor-3]+stairs[floor-1])

print(dp[n-1])