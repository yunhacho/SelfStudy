from itertools import permutations

n, k = int(input()), int(input())
makes=set()
numbers=[input() for _ in range(n)]

for p in permutations(numbers, k):
    makes.add(int(''.join(p)))
print(len(makes))