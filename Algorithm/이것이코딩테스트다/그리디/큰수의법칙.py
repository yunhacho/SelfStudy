N, M, K = map(int, input().split())
number=sorted(map(int, input().split()))

r, m=divmod(M, K+1)
print(number[-1]*(r*K+m)+number[-2]*r)

