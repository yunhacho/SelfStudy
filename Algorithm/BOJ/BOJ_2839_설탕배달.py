n=int(input())
count=0
while n>-1:
    if n%5==0:
        count+=n//5
        print(count)
        break
    else:
        n-=3
        count+=1
else:
    print(-1)
