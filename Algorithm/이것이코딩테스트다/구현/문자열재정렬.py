string=input()
alpha=[]
num=0

for s in string:
    if s.isdigit(): num+=int(s)
    else: alpha.append(s)

print(''.join(sorted(alpha))+str(num))
