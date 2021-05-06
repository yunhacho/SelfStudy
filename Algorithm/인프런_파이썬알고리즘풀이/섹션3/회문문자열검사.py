N=int(input())
words=[input().upper() for _ in range(N)]
res=['NO']*N
for i, word in enumerate(words):
    if word==word[::-1]: res[i]='YES'
for i, r in enumerate(res):
    print('#%d %s' %(i+1, r))
