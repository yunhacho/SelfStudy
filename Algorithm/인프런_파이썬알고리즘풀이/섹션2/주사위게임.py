N=int(input())
dice=[list(map(int, input().split())) for _ in range(N)]
money=[]
for d in dice:
    if len(set(d))==3:
        money.append(max(d)*100)
    elif len(set(d))==2:
        for number in d:
            if d.count(number)==2:
                money.append(1000+(number*100))
    else: money.append(10000+(d[0]*1000))

print(max(money))