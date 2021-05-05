N=int(input())
answer=list(map(int,input().split()))
score=[0]*N
if answer[0]==1: score[0]=1
for i in range(1, N):
    if answer[i]==0:
        score[i]=0
    else:
        score[i]=score[i-1]+1

print(sum(score))