
def toPostOrder(inorder):
    postorder=''; stack=[]
    operand=('(',')','*','/','+','-')
    prior={'(':0,'+':1,'-':1, '*':2, '/':2}
    for char in inorder:
        if char not in operand: postorder+=char
        elif char=='(': stack.append(char)
        elif char==')': 
            while stack and stack[-1]!='(': postorder+=stack.pop()
            stack.pop()
        else: 
            while stack and prior[stack[-1]]>=prior[char]: postorder+=stack.pop()
            stack.append(char)
    if stack:   postorder+=''.join(stack[::-1])
    return postorder 
if __name__=="__main__":
    print(toPostOrder(input()))