def solution(s):
    DicOfNum=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 
        'seven', 'eight', 'nine']
    for num, string in enumerate(DicOfNum): s=s.replace(string, str(num))
    return int(s)

if __name__=="__main__":
    print(solution(input()))