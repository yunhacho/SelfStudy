N=int(input())
plan=input().split()
move={'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
curx, cury = 1 , 1

for p in plan:
    x=curx+move[p][0]
    y=cury+move[p][1]
    if 0<x<N+1 and 0<y<N+1:
        curx=x; cury=y

print(curx, cury)