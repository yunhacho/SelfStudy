from collections import deque

def Josephus(N: int, K: int) -> str:
    circle=deque(range(K, N+1)); result=[]
    if K>1: circle.extend(range(1, K))
    while circle:
        result.append(circle.popleft())
        circle.rotate(-(K-1))
    return ', '.join(map(str,result))

if __name__=="__main__":
    N, K = map(int, input().split())
    print("<"+Josephus(N,K)+">")
