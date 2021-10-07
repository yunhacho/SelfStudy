def solution(n, results):
    # A 선수를 이긴 B선수는
    # A 선수가 이긴 모든 선수에 대해 이긴다.
    wins={i: set() for i in range(1,n+1)} # i가 이긴 선수 
    loses={i: set() for i in range(1,n+1)} # i를 이긴 선수
    
    for i in range(1,n+1):
        for win,lose in results:
            if win==i: wins[i].add(lose)
            elif lose==i: loses[i].add(win)
    
        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])
    
    cnt=0
    for i in range(1,n+1):
        if len(wins[i])+len(loses[i])==n-1: cnt+=1

    return cnt