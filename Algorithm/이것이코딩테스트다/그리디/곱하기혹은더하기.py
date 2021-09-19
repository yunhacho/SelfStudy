number=list(map(int, list(input())))
result=number[0]

for n in number[1:]:
    if result+n < result*n:
        result*=n
    else: result+=n

print(result)
