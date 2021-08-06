'''
aaabbcccaa -> a3b2c3a2
'''
def compression(string: str) -> str:
    last=string[0]; count=1
    comp_list=[string[0]]

    for char in string[1:]:
        if last==char: count+=1
        else:
            comp_list.append(str(count))
            last=char; count=1
            comp_list.append(char)
    comp_list.append(str(count))
    return ''.join(comp_list)

if __name__=="__main__":
    string='aaabbcccaa'
    print(compression(string))