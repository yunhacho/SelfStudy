import sys
input=sys.stdin.readline

def get_move_order(n):
    orders=[] # (r,c,d)
    direction=[(0,-1),(1,0),(0,1),(-1,0)]
    r,c,d=n//2,n//2,0
    for i in range(1,n):
        for _ in range(2):
            for j in range(i):
                mr,mc=r+direction[d%4][0], c+direction[d%4][1]
                orders.append((mr,mc,d%4))
                r,c=mr,mc
            d+=1
    for i in range(n-2,-1,-1):
        orders.append((0,i,d%4))
    return orders

def move_tornado(r,c,moves):
    global out_of_map
    diff_sum=0
    for x,y,rate in moves[:-1]:
        mx,my=r+x,c+y
        diff=int(maps[r][c]*rate)
        if 0<=mx<n and 0<=my<n: maps[mx][my]+=diff
        else: out_of_map+=diff
        diff_sum+=diff
    maps[r][c]-=diff_sum
    mx,my=r+moves[-1][0],c+moves[-1][1]
    if 0<=mx<n and 0<=my<n: maps[mx][my]+=maps[r][c]
    else: out_of_map+=maps[r][c]
    maps[r][c]=0

left=[(-1,-1,0.1),(1,-1,0.1),(-1,0,0.07),(1,0,0.07),(-1,1,0.01),(1,1,0.01),(0,-2,0.05),
      (-2,0,0.02),(2,0,0.02),(0,-1,0)]
right=[(-1,-1,0.01),(1,-1,0.01),(-1,0,0.07),(1,0,0.07),(-1,1,0.1),(1,1,0.1),(0,2,0.05),
       (-2,0,0.02),(2,0,0.02),(0,1,0)]
down=[(-1,-1,0.01),(-1,1,0.01),(2,0,0.05),(1,-1,0.1),(1,1,0.1),(0,-2,0.02),
      (0,2,0.02),(0,-1,0.07),(0,1,0.07),(1,0,0)]
up=[(-1,-1,0.1),(-1,1,0.1),(-2,0,0.05),(1,-1,0.01),(1,1,0.01),(0,-2,0.02),
    (0,2,0.02),(0,-1,0.07),(0,1,0.07),(-1,0,0)]
moving=[left,down,right,up]
out_of_map=0
n=int(input())
maps=[list(map(int,input().split())) for _ in range(n)]
orders=get_move_order(n)
for r,c,d in orders:
    move_tornado(r,c, moving[d])
print(out_of_map)