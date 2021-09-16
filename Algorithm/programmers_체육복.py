def solution(n, lost, reserve):
    only_reserve=set(reserve)-set(lost)
    only_lost=set(lost)-set(reserve)
    
    for r in only_reserve:
        if r-1 in only_lost: only_lost.remove(r-1)
        elif r+1 in only_lost: only_lost.remove(r+1)
    return n-len(only_lost)