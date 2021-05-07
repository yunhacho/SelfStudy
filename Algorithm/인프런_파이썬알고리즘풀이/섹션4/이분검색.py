N, M=list(map(int, input().split()))
nums=list(map(int, input().split()))
nums.sort()

left=0
right=N-1

while left <= right:
    mid=(left+right)//2
    if nums[mid]==M:
        break
    elif nums[mid]<M:
        left=mid+1
    else: right=mid-1
    
print(mid+1)