#!/usr/bin/env python
# coding: utf-8

def is_VPS(input):
    stack=[]
    for char in input:
        if char=='(': stack.append(char)
        elif char==')':
            if len(stack)==0: return 'NO'
            stack.pop()
    if len(stack)==0: return 'YES'
    return 'NO'

if __name__=="__main__":
    result=[]
    for _ in range(int(input())): result.append(is_VPS(input()))
    print(*result)