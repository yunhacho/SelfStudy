import re
from itertools import permutations

def solution(expression):
    exp=re.split(r'(\D)', expression)
    operator=re.sub('[0-9]', ' ', expression).split()
    for prior in permutations(set(operator), len(set(operator))):
        answer=max(answer, get_reward(exp, prior))
    return answer

def get_reward(exp, prior):
    operator=[]; operand=[]
    for item in exp:
        if item.isdigit(): operand.append(int(item))
        else:
            while operator and prior.index(item) >= prior.index(operator[-1]):
                n=operand[-2:]; del operand[-2:]
                operand.append(calculate(operator.pop(), *n))
            operator.append(item)
    while operator:
        n=operand[-2:]; del operand[-2:]
        operand.append(calculate(operator.pop(), *n))
    return abs(operand.pop())

def calculate(op, *operand):
    if op=='+': return operand[0]+operand[1]
    elif op=='-': return operand[0]-operand[1]
    elif op=='*': return operand[0]*operand[1]

# def get_reward(number, operator, prior):
#     ops=[]; nums=[]
#     for n, op in zip(number, operator):
#         nums.append(n)
#         while ops and prior.index(op) >= prior.index(ops[-1]):
#             operand, nums = nums[-2:], nums[:-2]
#             nums.append(calculate(ops.pop(), *operand))
#         ops.append(op)

#     nums.append(number[-1])
#     for i in range(len(nums)-1):
#         operand, nums = nums[-2:], nums[:-2]
#         nums.append(calculate(ops.pop(), *operand))

#     return abs(nums.pop())