# 구현, 문자열
import sys
import re
N, M = map(int, sys.stdin.readline().split())
bload=sys.stdin.readline().split()
flip=lambda x: sum(map(int, list(re.sub('1..','1',x))))

for _ in range(M):
    pain=list(map(int, sys.stdin.readline().split()))
    if not pain[0]: print(flip(''.join(bload)))
    else: bload[pain[1]]='1'
