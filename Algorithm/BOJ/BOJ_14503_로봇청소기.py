n,m=map(int,input().split())
r,c,d=map(int,input().split())
# 0 북(서3) 1 동(북0) 2 남(동1) 3 서(남2) 방향전환 (i-1)%4
dxy=((-1,0),(0,1),(1,0),(0,-1))
# 후진 0(2), 1(3), 2(0), 3,(1)
maps=[list(map(int,input().split())) for _ in range(n)]

count=0
while True:
        if maps[r][c]==0:
            maps[r][c]=2
            count+=1

        cango=False
        for _ in range(4):
            nx,ny=r+dxy[(d-1)%4][0], c+dxy[(d-1)%4][1]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]==0:
                    r,c,d=nx,ny,(d-1)%4
                    cango=True
                    break
                else: d=(d-1)%4
        
        if not cango:
            back=2 if d<2 else -2
            bx,by=r+dxy[d+back][0], c+dxy[d+back][1]
            if 0<=bx<n and 0<=by<m:
                if maps[bx][by]==1:
                    break
                else:
                    r,c=bx,by

print(count)