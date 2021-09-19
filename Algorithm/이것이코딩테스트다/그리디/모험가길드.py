n=int(input())
fears=sorted(map(int, input().split()))

count=0; result=0
for f in fears:
    count+=1
    if count>=f:
        result+=1
        count=0
print(result)

