from collections import deque
N=int(input())
maps=[[0]*N for _ in range(N)]

# 사과가 있는 곳 1로 변경
for y,x in list(map(int, input().split())): maps[y-1][x-1]=1

# 머리가 동,서,남,북 방향에 있을 때 전진하는 좌표와 D, L 방향의 y,x 이동 좌표
dir={1:[(0,1),(-1,0),(1,0)], 2:[(0,-1),(-1,0),(1,0)], 3:[(1,0), (0,-1),(0,1)], 4:[(-1,0),(0,1),(0,-1)]} 
rotate=deque()
for t, d in range(int(input())):
    if d=='D': # 오른쪽으로 90도 회전
        rotate.append((t, 1))
    elif d=='L': # 왼쪽으로 90도 회전
        rotate.append((t, 2))

head=1 # 초기 뱀의 머리,꼬리는 오른쪽(동쪽) 방향에 있음
maps[0][0]=2; # 뱀이 있는 곳 2로 변경
cury=0; curx=0
taily=0; tailx=0
nexttaily=0; nexttailx=0
tic=0

while True:
    if rotate and tic==rotate[0][0]: 
        nextd=rotate[0][1]; rotate.popleft()
    else: nextd=0
    nexty, nextx=cury+dir[head][nextd][0], curx+dir[head][nextd][1]
    
    if nexty==0 or nexty==N-1 or nextx==0 or nextx==N-1 or maps[nexty][nextx]==2:
        break
    
    if maps[nexty][nextx]==1:
        maps[nexty][nextx]=2
    else:
        maps[taily][tailx]=0
        
    tic+=1
    cury, curx=nexty, nextx

    

