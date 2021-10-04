import heapq
import sys

n,m=map(int, sys.stdin.readline().split())
q=list(map(int, sys.stdin.readline().split()))
heapq.heapify(q)

for _ in range(m):
    a,b=heapq.heappop(q), heapq.heappop(q)
    heapq.heappush(q, a+b)
    heapq.heappush(q, a+b)

print(sum(q))