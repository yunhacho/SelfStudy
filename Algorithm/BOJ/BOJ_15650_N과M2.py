from itertools import combinations

n,m=map(int, input().split())
combination=lambda n,m: print('\n'.join(list(map(' '.join, combinations(map(str, range(1,n+1)),m)))))
combination(n,m)

def dfs(depth, sequence):
    if depth==m==len(sequence)-1:
        print(*sequence[1:], sep=' ')
        return
    for i in range(sequence[-1]+1, n+1):
        dfs(depth+1, sequence+[i])
dfs(0,[0])
