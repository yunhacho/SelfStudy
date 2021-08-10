from sys import stdin

def can_make_sequence(sequence):
    stack=[]; pivot=1 
    for num in sequence:
        if not stack or stack[-1] < num:
            if num < pivot: return 'NO'
            stack.extend(range(pivot, num))
            operation.extend(['+']*(num-pivot+1))
            operation.append('-')
            pivot=num+1
        else:
            cnt=0
            while stack and stack[-1]>=num: stack.pop(); cnt+=1
            operation.extend(['-']*cnt)
    return '\n'.join(operation)
            
if __name__ =="__main__":
    seq=[]; operation=[]
    for _ in range(int(input())): seq.append(int(stdin.readline().strip()))
    print(can_make_sequence(seq))
