import sys
input=sys.stdin.readline

def set_disjoint(student, likes):
    dx, dy=[-1,1,0,0], [0,0,1,-1]
    disjoint=[] # element: (disjoint cnt, empty cnt, row, col)
    for i in range(n):
        for j in range(n):
            if maps[i][j]==0:
                cnt_of_disjoint, cnt_of_empty=0,0
                for x,y in zip(dx,dy):
                    mx, my=x+i, y+j
                    if 0<=mx<n and 0<=my<n:
                        if maps[mx][my] in likes: cnt_of_disjoint+=1
                        elif maps[mx][my]==0: cnt_of_empty+=1
                disjoint.append((cnt_of_disjoint,cnt_of_empty, i, j))
    return sorted(disjoint, key=lambda e: (-e[0], -e[1], e[2], e[3]))[0][2:]

def get_likes(r,c):
    student=maps[r][c]
    dx,dy=[-1,1,0,0],[0,0,1,-1]
    count=0
    for i,j in zip(dx,dy):
        mx,my=r+i, c+j
        if 0<=mx<n and 0<=my<n and maps[mx][my] in likes[student]: count+=1
    return pow(10,count-1) if count>1 else count

n=int(input())
maps=[[0]*n for _ in range(n)]
sequence=[]
likes=[[] for _ in range((n**2)+1)]
for _ in range(n**2):
    student, *like=map(int, input().split())
    sequence.append(student)
    likes[student]=like
    
for student in sequence:
    x,y=set_disjoint(student, likes[student])
    maps[x][y]=student

total=sum(get_likes(i,j) for i in range(n) for j in range(n))
print(total)
