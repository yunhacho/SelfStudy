cards=list(range(21))
for i in range(10):
    ai, bi=list(map(int, input().split()))
    cards[ai:bi+1]=cards[bi:ai-1:-1]
print(*cards[1:], sep=' ')