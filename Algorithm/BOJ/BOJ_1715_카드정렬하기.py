import heapq
import sys

n, *q= map(int, sys.stdin.readlines())
heapq.heapify(q)

if n==1: print(0)
else:
    count=0
    while len(q)>1:
        t1,t2=heapq.heappop(q), heapq.heappop(q)
        count+=t1+t2
        heapq.heappush(q,(t1+t2))
    print(count)