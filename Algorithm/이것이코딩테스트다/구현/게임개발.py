N, M = map(int, input().split())
curx, cury, direction = map(int, input().split())
game=[list(map(int, input().split())) for _ in range(N)]

visited=[[0]*M for _ in range(N)]
visited[curx][cury]=1

dx=[-1,0,1,0]; dy=[0,1,0,-1]

def turn_left():
    global direction
    direction-=1
    if direction == -1: direction=3

count=1
turn_time=0

while True:
    turn_left()
    nx=curx+dx[direction]
    ny=cury+dy[direction]
    
    if game[nx][ny]==0 and visited[nx][ny]==0:
        visited[nx][ny]=1
        curx, cury = nx, ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1

    if turn_time==4:
        nx=curx-dx[direction]
        ny=cury-dy[direction]
        if game[nx][ny]==0:
            curx, cury=nx,ny
        else:
            break
        turn_time=0

print(count)
