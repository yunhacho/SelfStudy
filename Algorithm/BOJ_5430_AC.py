from collections import deque

result=[]

for _ in range(int(input())):
    function=input(); n=int(input())
    if(n==0): input(); ary=[]
    else: ary=list(map(int, input().strip('[]').split(',')))
    queue=deque(ary)

    cntD=function.count('D')
    if n < cntD: result.append('error')
    elif n==cntD: result.append('[]')
    else:
        if n==0: result.append('[]')
        else:
            reverse=False
            for func in function:
                if func=='R': reverse=not reverse
                else: # func=='D'
                    if reverse: queue.pop()
                    else: queue.popleft()
            if reverse : queue.reverse()
            result.append('['+','.join(list(map(str, list(queue))))+']')
        
print(*result, sep='\n')
