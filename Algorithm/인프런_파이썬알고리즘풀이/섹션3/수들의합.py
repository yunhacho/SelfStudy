from itertools import combinations
N, M=list(map(int, input().split()))
A=list(map(int, input().split()))
count=0

for i in range(N):
    total=A[i]
    if total==M:
        count+=1
    else:
        for j in range(i+1, N):
            total+=A[j]
            if total==M:
                count+=1; 
                break
        
print(count)
    