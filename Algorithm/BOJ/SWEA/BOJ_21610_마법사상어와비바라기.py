import sys
input=sys.stdin.readline

def move_cloud(d, s):
    new=[]
    direction=[None, (0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    for x,y in clouds:
        mx,my=direction[d][0]*s, direction[d][1]*s
        new.append([(x+mx)%n, (y+my)%n])
    return new

def increase_water_in_cloud(clouds):
    for x,y in clouds: maps[x][y]+=1

def waterbug_magic(clouds):
    diagonal=[(-1,-1),(-1,1),(1,-1),(1,1)]
    for x,y in clouds:
        count=0
        for dx, dy in diagonal:
             if 0<=x+dx<n and 0<=y+dy<n:
                 if maps[x+dx][y+dy]>0: count+=1
        maps[x][y]+=count
    return

def make_cloud(clouds):
    new=[]
    is_in_clouds=[[False]*n for _ in range(n)]
    for x,y in clouds: is_in_clouds[x][y]=True

    for i in range(n):
        for j in range(n):
            if not is_in_clouds[i][j] and maps[i][j]>=2: 
                new.append((i,j))
                maps[i][j]-=2
    return new

n,m=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(n)]
instruction=[list(map(int, input().split())) for _ in range(m)] # [[di,si]] 방향과 거리

clouds=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
for i in range(m):
    clouds=move_cloud(instruction[i][0], instruction[i][1])
    increase_water_in_cloud(clouds)
    waterbug_magic(clouds)
    clouds=make_cloud(clouds)

print(sum(maps[x][y] for x in range(n) for y in range(n)))