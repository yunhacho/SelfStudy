def dfs(depth, value):
    global min_val, max_val
    if depth==n:
        min_val=min(min_val, value)
        max_val=max(max_val, value)
        return
    if ops[0]>0:
        ops[0]-=1
        dfs(depth+1, value+numbers[depth])
        ops[0]+=1
    if ops[1]>0:
        ops[1]-=1
        dfs(depth+1, value-numbers[depth])
        ops[1]+=1
    if ops[2]>0:
        ops[2]-=1
        dfs(depth+1, value*numbers[depth])
        ops[2]+=1
    if ops[3]>0:
        ops[3]-=1
        pm=(-1 if value<0 else 1)
        dfs(depth+1, (pm*value//numbers[depth])*pm)
        ops[3]+=1

n=int(input())
numbers=list(map(int, input().split()))
ops=list(map(int, input().split()))

min_val, max_val = int(1e9), -int(1e9)
dfs(1,numbers[0])
print(max_val,min_val, sep='\n')