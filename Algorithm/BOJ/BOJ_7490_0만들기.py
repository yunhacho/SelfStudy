def dfs(depth, exp):
    if depth==n:
        if eval(exp.replace(' ', ''))==0:
            print(exp)
        return
    for op in sorted(['+','-',' ']):
        dfs(depth+1, exp+op+string[depth])
        
for _ in range(int(input())):
    n=int(input())
    string=''.join(map(str, range(1,n+1)))
    dfs(1,'1')
    print()
