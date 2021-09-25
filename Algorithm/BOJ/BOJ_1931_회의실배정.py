N=int(input())
meetings=[list(map(int,input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

count=1
endtime=meetings[0][1]
for start, end in meetings[1:]:
    if endtime > start: continue
    endtime=end
    count+=1
print(count)