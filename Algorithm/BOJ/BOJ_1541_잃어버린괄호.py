#그리디 알고리즘

exp=input()
stack=[]
n=''; result=0; mode=1

for e in exp:
    if e.isdigit(): n+=e
    else:
        if e=='+':
            stack.append(int(n))
        elif e=='-':
            result+=(int(n)+sum(stack))*mode
            mode=-1; stack=[]
        n=''

result+=(int(n)+sum(stack))*mode
print(result)