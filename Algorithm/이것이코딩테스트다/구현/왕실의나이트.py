P=input()
curx=ord(P[0])-97
cury=int(P[1])

posx=[-2,-2,2,2,1,-1,1,-1]
posy=[1,-1,1,-1,2,2,-2,-2]

count=0
for i in range(len(posx)):
    x=curx+posx[i]
    y=cury+posy[i]
    if 0<x<9 and 0<y<9: count+=1

print(count)