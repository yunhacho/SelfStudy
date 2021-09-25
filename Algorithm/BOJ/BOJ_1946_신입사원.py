result=[]
for t in range(int(input())):
    count=1
    people=[list(map(int,input().split())) for _ in range(int(input()))]
    people.sort(key=lambda x:x[0])
    compy=people[0][1]
    for x,y in people[1:]:
        if compy <= y: continue
        compy=y
        count+=1
    result.append(count)
print(*result, sep='\n')
