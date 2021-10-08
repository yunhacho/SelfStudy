import sys
def dfs(depth, exp, used):
    global min_val, max_val, add, sub, mul, div
    if depth==n:
        value=eval(exp)
        min_val=min(min_val, value)
        max_val=max(max_val, value)
        return
    
    if used[0]<add:
        used[0]+=1
        dfs(depth+1, exp+'+'+str(number[depth]), used)
        used[0]-=1
    
    if used[1]<sub:
        used[1]+=1
        dfs(depth+1, exp+'-'+str(number[depth]), used)
        used[1]-=1

    if used[2]<mul:
        used[2]+=1
        dfs(depth+1, exp+'*'+str(number[depth]), used)
        used[2]-=1

    if used[3]<div:
        used[3]+=1
        dfs(depth+1, exp+'//'+str(number[depth]), used)
        used[3]-=1    

n=int(input())
number=list(map(int, sys.stdin.readline().split()))
add, sub, mul, div=map(int, sys.stdin.readline().split())
min_val, max_val = int(1e9), -int(1e9)

dfs(1,str(number[0]), [0,0,0,0])
print(max_val, min_val, sep='\n')