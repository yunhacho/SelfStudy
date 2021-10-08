import sys
from itertools import combinations
n=int(input())
capacity=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_value=int(1e9)
for comb in combinations(range(n), n//2):
    team_a=sum(capacity[x][y] for x in comb for y in comb)
    b=set(range(n))-set(comb)
    team_b=sum(capacity[x][y] for x in b for y in b)
    min_value=min(min_value, abs(team_a-team_b))

print(min_value)