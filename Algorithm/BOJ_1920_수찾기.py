from sys import stdin

def Does_Number_Exist_in_Sequence(N: int) -> bool:
    left, right = 0, len(sequence)-1
    while left <= right:
            mid=(left+right)//2
            if sequence[mid]==N: return True
            elif sequence[mid]>N: right=mid-1
            else: left=mid+1
    return False

if __name__=="__main__":
    N=int(input())
    sequence=list(map(int, stdin.readline().split()))
    sequence.sort()
    M=int(input())
    for num in map(int, stdin.readline().split()):
        print(int(Does_Number_Exist_in_Sequence(num)))