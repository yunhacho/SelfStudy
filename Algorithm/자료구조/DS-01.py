import itertools
import random
#1
def sumAry1D_f(array):
    return sum(array)

#2
def sumAry2D_f1(array):
    answer=0
    for ary in array: answer+=sum(ary)
    return answer

def sumAry2D_f2(array):
    return sum(sum(array,[]))

def sumAry2D_f3(array):
    return sum(itertools.chain(*array))
#3
def sumAry3D_f(array):
    return sum(itertools.chain(*[sum(ary2d, []) for ary2d in array]))

#5 
def isXinAry():
    array=[random.randint(0,999) for _ in range(int(input()))]
    selectionSort(array)
    status, index= binarysearch(int(input()), array)
    print(array)
    print(index if status else -1)

def selectionSort(array):
    for i in range(len(array)-1):
        minidx=i
        for j in range(i+1, len(array)):
            if array[j] < array[minidx]: minidx=j
        array[i], array[minidx] = array[minidx], array[i]

def binarysearch(x, array):
    left=0; right=len(array)-1
    status=False
    while left<=right:
        mid=(left+right)//2
        if x==array[mid]: status=True; break
        elif x>array[mid]: left=mid+1
        elif x<array[mid]: right=mid-1
    return status, mid

isXinAry()