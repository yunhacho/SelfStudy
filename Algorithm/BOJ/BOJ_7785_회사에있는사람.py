n=int(input())
log=set()

for _ in range(n):
    x,y=input().split()
    if y=='leave': log.remove(x)
    else: log.add(x)

print(*sorted(list(log), reverse=True), sep='\n')