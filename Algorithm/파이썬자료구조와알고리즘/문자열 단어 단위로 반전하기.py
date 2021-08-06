'''
'파이썬 알고리즘 정말 재미있다' -> '재미있다 정말 알고리즘 파이썬'
'''

def revert_by_word(str):
    return ' '.join(str.split()[::-1])

if __name__=="__main__":
    print(revert_by_word('파이썬 알고리즘 정말 재미있다'))
    str='파이썬 알고리즘 정말 재미있다'.split()
    print(reversed(str))