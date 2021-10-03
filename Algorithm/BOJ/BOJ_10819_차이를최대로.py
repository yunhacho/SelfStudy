from itertools import permutations

n=int(input())
numbers=list(map(int,input().split()))
max_val=-int(1e9)
for p in permutations(numbers, n):
    max_val=max(max_val, sum(abs(p[i]-p[i+1]) for i in range(n-1)))
print(max_val)