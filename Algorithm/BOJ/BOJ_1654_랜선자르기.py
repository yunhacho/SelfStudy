from sys import stdin
from types import LambdaType

def get_count_of_LAN(length_of_LAN: int)-> int:
    count=0
    for LAN in LANs: count+=LAN//length_of_LAN
    return count

def get_max_length_of_LAN(N: int) -> int:
    left, right = 1, max(LANs)
    max_length=0
    while left <= right:
        mid=(left+right)//2
        if get_count_of_LAN(mid)>=N:
            max_length=max(max_length,mid); left=mid+1
        else: right=mid-1
    return max_length
        
if __name__=="__main__":
    K, N = map(int, input().split())
    LANs = sorted(map(int, stdin.readlines()))
    print(get_max_length_of_LAN(N))