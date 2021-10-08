n,m=map(int, input().split())

def dfs(depth, seq):
    if depth==m:
        print(*seq, sep=' ')
        return

    for i in range(1,n+1):
        dfs(depth+1, seq+[i])

dfs(0,[])