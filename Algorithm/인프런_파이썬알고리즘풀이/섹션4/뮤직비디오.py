N, M=list(map(int, input().split()))
music=list(map(int, input().split()))

def can_sell(mid):
    group=1
    sums=0
    for t in music:
        if sums+t<=mid:
            sums+=t
        else:
            group+=1
            sums=t
    return group

left=1
right=sum(music)
maxm=max(music)
while left <= right:
    mid=(left+right)//2
    if mid>=maxm and can_sell(mid)<=M:
        res=mid
        right=mid-1
    else: left=mid+1
print(res)
