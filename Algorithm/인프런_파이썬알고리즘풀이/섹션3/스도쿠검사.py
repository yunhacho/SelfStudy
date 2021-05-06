sdoku=[list(map(int,input().split())) for _ in range(9)]
result=True

if not all(len(set(list(i)))==9 for i in zip(*sdoku)) or not all(len(set(i))==9 for i in sdoku):
    result=False

for i in range(3):
    for j in range(3):
        nums=[]
        for k in range(3):
            nums.extend(sdoku[i*3+k][j*3:(j*3)+3])
        if len(set(nums))!=9:
            result=False
            break
print('YES' if result else 'NO')