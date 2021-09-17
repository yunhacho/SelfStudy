N, M = map(int, input().split())
answer=1
for _ in range(N):
    line=map(int, input().split())
    answer=max(answer, min(line))
print(answer)