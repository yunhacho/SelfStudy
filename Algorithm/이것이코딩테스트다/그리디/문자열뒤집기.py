word=input()

s=word[0]
d={'0':0, '1':0}
for w in word[1:]:
    if s==w: continue
    else:
        d[s]+=1
        s=w
print(sorted(d.items(), key=lambda x: x[1])[0][1])