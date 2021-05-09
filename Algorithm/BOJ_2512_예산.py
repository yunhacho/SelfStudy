n=int(input())
budgets=list(map(int,input().split()))
country=int(input())

def Count(mid):
    total=0
    for budget in budgets:
        if budget <= mid: total+=budget
        else: total+=mid
    return total

if country >= sum(budgets): print(max(budgets))
else:
    left=1; right=max(budgets)
    while left <= right:
        mid=(left+right)//2
        if Count(mid) <= country:
            res=mid
            left=mid+1
        else: right=mid-1
    print(res)