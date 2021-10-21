import sys
from collections import deque
input=sys.stdin.readline

CanRobotMove=lambda r: robots[r] and not robots[r+1] and conveir[r+1]>0

n,k=map(int,input().split())
conveir=deque(list(map(int,input().split())))
robots=deque([False]*n)
step=1
while True:
    conveir.rotate(1)
    robots.rotate(1)
    robots[-1]=0
    if any(robots):
        for i in range(n-2,-1,-1):
            if CanRobotMove(i):
                robots[i], robots[i+1] = False, True
                conveir[i+1]-=1
    robots[-1]=False
    if conveir[0]>0 and not robots[0]:
        robots[0]=True
        conveir[0]-=1
    if conveir.count(0)>=k:
        break
    step+=1

print(step)


