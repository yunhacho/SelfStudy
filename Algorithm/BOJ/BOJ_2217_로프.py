weights=[int(input()) for _ in range(int(input()))]
weights.sort(reverse=True)

max_val=0
for i, v in enumerate(weights): max_val=max(max_val, (i+1)*v)
print(max_val)