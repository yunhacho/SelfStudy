from collections import deque

F, S, G, U, D = list(map(int, input().split()))

able=False
dist=[0]*(F+1)
visit=[0]*(F+1)

queue=deque([S])
while queue:
    curpos=queue.popleft()
    if curpos==G:
        able=True
        break
    visit[curpos]=1
    for nextpos in [curpos+U, curpos-D]:
        if 1<=nextpos<=F and not visit[nextpos]:
            visit[nextpos]=1
            dist[nextpos]=dist[curpos]+1
            queue.append(nextpos)

print(dist[curpos] if able else 'use the stairs')