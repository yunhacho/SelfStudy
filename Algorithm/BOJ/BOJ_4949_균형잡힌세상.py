import sys
def isBalanced(sentence):
    stack=[]
    for char in sentence:
        if char in '([': stack.append(char)
        elif char==')':
            if not stack or stack.pop()!='(': return 'no'
        elif char==']':
            if not stack or stack.pop()!='[': return 'no'
    return 'no' if stack else 'yes'
        
if __name__=="__main__":
    inputs=sys.stdin.readlines()
    inputs.pop()
    print(*list(map(isBalanced, inputs)), sep='\n')