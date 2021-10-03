
def dfs(depth, sequence):
    if depth==6:
        print(*[numbers[i]for i in sequence[1:]], sep=' ')
        return
    for i in range(sequence[-1]+1, n):
        dfs(depth+1, sequence+[i])

while True:
    n, *numbers=map(int, input().split())
    if n==0: break
    dfs(0,[-1])
    print()