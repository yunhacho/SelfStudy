string=input()
numbers=list('0123456789')
number=''
for s in string:
    if s in numbers: number+=s
number=int(number)
count=0
for i in range(1, number+1):
    if number%i==0:
        count+=1

print(number, count, sep='\n')
