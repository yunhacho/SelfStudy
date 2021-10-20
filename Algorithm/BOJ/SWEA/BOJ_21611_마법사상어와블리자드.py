import sys
input=sys.stdin.readline

def destroy_balls(d,s):
    blanks=[]
    move=[None,(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(1,s+1):
        mx,my=mid_r+(i*move[d][0]), mid_c+(i*move[d][1])
        if 0<=mx<n and 0<=my<n:
            maps[mx][my]=0
            blanks.append([numbers[mx][my]])
    return blanks

def move_balls(blanks):
    after_explode= True if len(blanks[0])>1 else False

    if after_explode:
        prev_start, prev_end=blanks[0]
        for i in range(1,len(blanks)):
            next_start, next_end=blanks[i]
            for j in range(prev_end+1, next_start):
                r,c=orders[j]
                to_r,to_c=orders[j-(prev_end-prev_start+1)]
                maps[to_r][to_c]=maps[r][c]
                maps[r][c]=0
            prev_start, prev_end= next_start-(prev_end-prev_start+1), next_end
        next_start=(n*n)-2
        for j in range(prev_end+1, next_start):
            r,c=orders[j]
            to_r,to_c=orders[j-(prev_end-prev_start+1)]
            maps[to_r][to_c]=maps[r][c]
            maps[r][c]=0

    else:
        for i in range(len(blanks)-1,-1,-1):
            blank_number=blanks[i][0]
            b_r,b_c=orders[blank_number]
            for j in range(blank_number+1,(n*n)-1):
                m_r,m_c=orders[j]
                maps[b_r][b_c]=maps[m_r][m_c]
                b_r,b_c=m_r,m_c
            maps[b_r][b_c]=0  #[TODO] maps[0][0] 옮기기        


def explode_balls():
    explodes=[]
    ball_number=maps[orders[0][0]][orders[0][1]]
    ball_count=1
    map_number=0
    for i in range(1,(n*n)-1):
        if ball_number==0: break
        mx,my=orders[i]
        if maps[mx][my]==ball_number:
            ball_count+=1
        else:
            if ball_count>=4:
                total_explodes[ball_number-1]+=ball_count
                explodes.append([map_number,i-1])
            map_number=i
            ball_number=maps[mx][my]
            ball_count=1

    if ball_count>=4:
        total_explodes[ball_number-1]+=ball_count
        explodes.append([map_number,i])
        
    for start, end in explodes:
        for i in range(start, end+1):
            r,c=orders[i]
            maps[r][c]=0

    return explodes

def group_balls():
    new_map=[[0]*n for _ in range(n)]
    ball_number=maps[orders[0][0]][orders[0][1]]
    ball_count=1
    map_number=0
    for i in range(1,(n*n)-1):
        if map_number>(n*n)-3: break
        mx,my=orders[i]
        if maps[mx][my]==ball_number:
            ball_count+=1
        else:
            start_r, start_c=orders[map_number]
            end_r,end_c=orders[map_number+1]
            new_map[start_r][start_c]=ball_count
            new_map[end_r][end_c]=ball_number
            map_number+=2

            ball_number=maps[mx][my]
            ball_count=1
    for i in range(n):
        maps[i]=new_map[i][:]

def order_of_map():
    orders=[]
    numbers=[[-1]*n for _ in range(n)]
    move=[(0,-1),(1,0),(0,1),(-1,0)]
    cur_x,cur_y,cur_d=mid_r,mid_c,0
    count=0
    for i in range(1,n):
        for _ in range(2):
            for j in range(i):
                mx=cur_x+move[cur_d%4][0]
                my=cur_y+move[cur_d%4][1]
                if 0<=mx<n and 0<=my<n:
                    orders.append((mx,my))
                    numbers[mx][my]=count
                cur_x,cur_y=mx,my
                count+=1
            cur_d+=1
    for j in range(n-2,-1,-1):
        orders.append((0,j))
        numbers[0][j]=count
        count+=1
    return orders, numbers

n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
operation=[list(map(int,input().split())) for _ in range(m)]

mid_r,mid_c=n//2, n//2
orders, numbers=order_of_map()
total_explodes=[0,0,0]
for d, s in operation:
    blanks=destroy_balls(d,s)
    move_balls(blanks)
    now_explodes=explode_balls()
    while now_explodes:
        move_balls(now_explodes)
        now_explodes=explode_balls()
    group_balls()
print(sum((i+1)*count for i,count in enumerate(total_explodes)))
