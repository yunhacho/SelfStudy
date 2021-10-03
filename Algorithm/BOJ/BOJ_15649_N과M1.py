from itertools import permutations
n,m=map(int, input().split())

permutation=lambda n,m:print('\n'.join(list(map(' '.join,permutations(map(str, range(1,n+1)),m)))))

visited=[False]*(n+1)
def dfs(depth,sequence):
    if depth==m:
        print(*sequence, sep=' ')
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=True
            dfs(depth+1,sequence+[i])
            visited[i]=False
dfs(0,[])