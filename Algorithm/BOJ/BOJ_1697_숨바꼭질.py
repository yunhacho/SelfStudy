from collections import deque

N, K=list(map(int, input().split()))
MAX=10**5
queue=deque([N])
visit=[0]*(MAX+1)
move=[0]*(MAX+1)

while queue:
    curpos=queue.popleft()
    if curpos==K: break
    visit[curpos]=1
    for movedir in [-1,1,2]:
        nextpos=curpos+movedir if movedir!=2 else curpos*2
        if 0<=nextpos<=MAX and not visit[nextpos]:
            move[nextpos]=move[curpos]+1
            visit[nextpos]=1
            queue.append(nextpos)
            
print(move[curpos])