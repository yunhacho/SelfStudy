dist=[[(i-1)//3, (i-1)%3] for i in range(1,10)]
dist.insert(0, [3,1])
print(*dist)