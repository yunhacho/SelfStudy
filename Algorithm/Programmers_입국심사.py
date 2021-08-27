def solution(n, times):
    left=1; right=max(times)*n; min_time=0
    while left <= right:
        mid=(left+right)//2
        if number_of_passed(mid, times) >=n: 
            right=mid-1
            min_time=mid
        else: left=mid+1
    return min_time

def number_of_passed(t, times):
    return sum([t//n for n in times])