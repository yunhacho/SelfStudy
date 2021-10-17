import sys
import math
input=sys.stdin.readline

def move_fireball():
    direct=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    while fireballs:
        r,c,m,s,d=fireballs.pop()
        mr,mc=(r+s*direct[d][0])%n,(c+s*direct[d][1])%n
        maps[mr][mc].append([m,s,d])

def do_at_least_two():
    for r in range(n):
        for c in range(n):
            if len(maps[r][c])>1:
                sum_m, sum_s, cur_d, check = maps[r][c][0][0], maps[r][c][0][1], maps[r][c][0][2]%2, True
                for m,s,d in maps[r][c][1:]:
                    sum_m+=m; sum_s+=s
                    if check and d%2!=cur_d: check=False
                if sum_m//5>0:
                    fin_m, fin_s = sum_m//5, sum_s//len(maps[r][c])
                    fin_d=[0,2,4,6] if check else [1,3,5,7]
                    for d in fin_d: fireballs.append([r,c, fin_m, fin_s, d])

            elif len(maps[r][c])==1:
                fireballs.append([r,c]+maps[r][c][0])
            maps[r][c]=[]

n,m,k=map(int, input().split())
maps=[[[] for j in range(n)] for i in range(n)]
fireballs=[]
for _ in range(m):
    r,c,m,s,d=map(int, input().split())
    fireballs.append((r-1,c-1,m,s,d))

for _ in range(k):
    move_fireball()
    do_at_least_two()

result=0
for r,c,m,s,d in fireballs: result+=m
print(result)