n=int(input())
all=sorted(map(int, input().split()))
m=int(input())
find=list(map(int, input().split()))

def binarysearch(all, f):
    left, right=0, len(all)-1
    while left<=right:
        mid=(left+right)//2
        if all[mid]==f: return True
        elif all[mid]>f: right=mid-1
        else: left=mid+1
    return False

for f in find:
    if binarysearch(all, f)==True: print('YES')
    else: print('No')