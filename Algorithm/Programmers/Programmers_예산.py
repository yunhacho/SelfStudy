
def solution(d, budget):
    d.sort()
    cnt=0
    for i in d:
        budget-=i
        if(budget<0): break
        cnt+=1
    return cnt
'''
d, budget=input().split(', ')
d=list(map(int, d.strip('[]').split(','))); d.sort()
budget=int(budget)
count=0; n=len(d)

def dfs(pos, cursum):
    global d, budget, count, n

    if(pos==n-1): count+=1; return
    for i in range(pos, n-1):
        if(cursum+d[i+1]>budget):
            count+=1; return
        dfs(i+1, cursum+d[i+1])

dfs(0, d[0])
print(count)
'''
