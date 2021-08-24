def solution(p:str)->str:
    if not p: return p
    u,v = split(p)
    if is_proper(u): return u + solution(v)
    else: return '(' + solution(v) + ')' + reverse(u)

def split(string:str)->str:
    count=0
    for i,s in enumerate(string):
        count+= 1 if s=='(' else -1
        if count==0: break
    return string[:i+1], string[i+1:]

def is_proper(string:str)->bool:
    stack=[]
    for s in string:
        if s=='(': stack.append(s)
        elif not stack: return False
        else: stack.pop()
    return not stack

def reverse(string:str)->str:
    return ''.join([ '(' if s==')' else ')' for s in string[1:-1]])