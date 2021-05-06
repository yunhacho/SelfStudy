maze=[list(map(int, input().split())) for _ in range(7)]
count=0
for line in maze:
    for i in range(3):
        if i==0:
            if str(line[i:i+5])==str(line[i+4::-1]):
                count+=1
        elif str(line[i:i+5])==str(line[i+4:i-1:-1]):
            count+=1

for line in zip(*maze):
    line=list(line)
    for i in range(3):
        if i==0:
            if str(line[i:i+5])==str(line[i+4::-1]):
                count+=1
        elif str(line[i:i+5])==str(line[i+4:i-1:-1]):
            count+=1

print(count)

