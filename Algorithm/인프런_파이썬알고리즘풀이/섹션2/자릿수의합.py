def digit_sum(x):
    return sum(list(map(int,x)))

N=int(input())
nums=input().split()
maxs=0; number=0
for n in nums:
    s=digit_sum(n)
    if s>maxs: 
        maxs=s
        number=int(n)

print(number)
