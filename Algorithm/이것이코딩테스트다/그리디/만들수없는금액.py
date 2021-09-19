n=int(input())
coins=sorted(map(int, input().split()))

target=1
for c in coins:
    if target<c: break
    target+=c

print(target)