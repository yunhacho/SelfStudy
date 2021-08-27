import sys
from typing import Iterable
def number_of_cases(total_value:int ,value_of_coins: Iterable) -> int:
    dp=[1]+[0]*(total_value+1); dp[0]=1
    for c in value_of_coins:
        for i in range(c,total_value+1):
            if dp[i-c]>0: dp[i]+=dp[i-c]
    return dp[total_value]

if __name__=="__main__":
    n,k=map(int,sys.stdin.readline().split())
    coins=map(lambda x: int(x.rstrip()), sys.stdin.readlines())
    print(number_of_cases(k,coins))