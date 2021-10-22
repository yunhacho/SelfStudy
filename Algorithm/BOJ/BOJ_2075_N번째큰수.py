import sys
import heapq
input=sys.stdin.readline

n=int(input())
queue=list(map(int, input().split()))
heapq.heapify(queue)
for _ in range(n-1):
    for x in map(int, input().split()):
        heapq.heappushpop(queue, x)

print(heapq.heappop(queue))
