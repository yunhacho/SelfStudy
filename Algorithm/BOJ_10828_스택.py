import sys
stack=[]
func={
        'push': lambda x: stack.append(int(x)),
        'pop': lambda : -1 if not stack else stack.pop(),
        'empty': lambda : 1 if not stack else 0, 
        'size': lambda : len(stack),
        'top': lambda : -1 if not stack else stack[-1]
    }
for _ in range(int(input())):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push': func[cmd[0]](cmd[1])
    else: print(func[cmd[0]]())