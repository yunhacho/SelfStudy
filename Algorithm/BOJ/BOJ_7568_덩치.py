#!/usr/bin/env python
# coding: utf-8

if __name__=="__main__":
    Bulks=[]
    n=int(input())
    for _ in range(n):
        kg, height=map(int, input().split())
        Bulks.append([kg, height])
    ranking=[1]*n 
    
    for i in range(n-1):
        kg, height=Bulks[i]
        for j in range(i+1, n):
            cmp_kg, cmp_hght=Bulks[j]
            if(kg>cmp_kg and height>cmp_hght):
                ranking[j]+=1
            elif(kg<cmp_kg and height<cmp_hght):
                ranking[i]+=1
    for rank in ranking:
        print(rank, end=' ')

