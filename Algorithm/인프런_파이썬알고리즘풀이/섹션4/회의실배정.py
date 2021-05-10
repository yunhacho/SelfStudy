n=int(input())
meetings=[list(map(int,input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

start, end=meetings[0][0], meetings[0][1]
count=1
for s,e in meetings[1:]:
    if s>=end:
        end=e
        count+=1

print(count)