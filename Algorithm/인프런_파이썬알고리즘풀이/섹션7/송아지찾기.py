from collections import deque
S, E=list(map(int, input().split()))

visit=[0]*10001
moves=[0]*10001

queue=deque()
queue.append(S)

while queue:
    curpos=queue.popleft()
    visit[curpos]=1
    if curpos==E: break
    for move in [1,-1,5]:
        next=curpos+move
        if 1<=next<=10000 and visit[next]==0:
            visit[next]=1
            moves[next]=moves[curpos]+1
            if next==E: break
            queue.append(next)
    
print(moves[E])
