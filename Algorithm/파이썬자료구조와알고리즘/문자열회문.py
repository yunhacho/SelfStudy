'''
공백 무시하고 앞, 뒤에서 읽을 때 동일한 구
다시 합창합시다 -> 회문
'' -> 회문
hello -> 회문
'''

def is_equal(phrase: str) -> bool:
    without_space=''.join(phrase.split())
    return without_space == without_space[::-1]

if __name__ =="__main__":
    phrase='다시 합창합시다'
    print(is_equal(phrase))