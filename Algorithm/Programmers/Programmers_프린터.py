from collections import deque
def solution(priorities, location):
    count=1
    q=deque([(i,p) for i,p in enumerate(priorities)])
    
    max_val=max(q, key=lambda x: x[1])[1]

    while True:
        x=q.popleft()
        if x[1]<max_val: q.append(x)
        elif x[0]==location: return count
        else: 
            max_val=max(q, key=lambda x: x[1])[1]
            count+=1
    return count