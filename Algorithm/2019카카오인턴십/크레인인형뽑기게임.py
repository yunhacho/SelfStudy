def solution(board, moves):
    stack=[0]
    b=[list(filter(lambda y: y!=0, c)) for c in zip(*board[::-1])] 
    
    count=0
    for m in moves:
        if b[m-1]:
            n=b[m-1].pop()
            if n==stack[-1]:
                stack.pop(); count+=2
            else: stack.append(n)
    return count