n=int(input())
num=[int(input()) for _ in range(n)]
num.sort(reverse=True)
print(*num, sep=' ')