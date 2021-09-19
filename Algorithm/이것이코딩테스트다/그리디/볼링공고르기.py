n,m=map(int, input().split())
balls=list(map(int, input().split()))

result=0
for i in range(1,m+1):
    result+=balls.count(i)*(len(balls)-balls.count(i))
    balls=[b for b in balls if b!=i]

print(result)