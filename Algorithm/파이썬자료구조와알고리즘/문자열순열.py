from itertools import permutations

if __name__=="__main__":
    string="012"
    print(*[''.join(i) for i in permutations(string)], sep=' ')