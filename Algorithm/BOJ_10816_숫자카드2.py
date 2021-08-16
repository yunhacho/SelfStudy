from sys import stdin
from collections import Counter

if __name__=="__main__":
    N=int(input()); cards=Counter(map(int, stdin.readline().split()))
    M=int(input()); number=map(int, stdin.readline().split())
    print(cards.elements())  
    for n in number:
        print(cards.get(n, 0), end=' ')
