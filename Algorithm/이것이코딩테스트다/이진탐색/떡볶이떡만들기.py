n,m=map(int, input().split())
all=sorted(map(int, input().split()))

def get_rice(mid, all):
    count=0
    for a in all:
        count+=max(0,a-mid)
    return count 

left, right = 0, max(all)
while left<right:
    mid=(left+right)//2
    if get_rice(mid,all)>=m:
        answer=mid
        left=mid+1
    else: right=mid-1
print(answer)