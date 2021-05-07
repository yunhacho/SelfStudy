K, N=list(map(int,input().split()))
nums=[int(input()) for _ in range(K)]

def count(mid):
    cnt=0
    for n in nums:
        cnt+=(n//mid)
    return cnt

largest=max(nums)
left=1
right=largest

while left<=right:
    mid=(left+right)//2
    if count(mid)>=N:
        res=mid
        left=mid+1
    else: right=mid-1

print(res)
