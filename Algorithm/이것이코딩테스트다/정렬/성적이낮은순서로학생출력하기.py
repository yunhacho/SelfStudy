n=int(input())
students=[]
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))
students.sort(key=lambda x: x[1])
print(*[n for n,s in students], sep=' ')