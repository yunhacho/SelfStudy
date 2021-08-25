def solution(numbers):
    binarys=[]
    for n in numbers:
        b='0'+ bin(n)[2:]; i=len(b)-b[::-1].find('0')-1
        binarys.append('{}{}{}'.format(b[:i],'1' if len(b)-1==i else '10',b[i+2:]))   
    return [int(b, 2) for b in binarys]