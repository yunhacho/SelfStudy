import re
from bisect import bisect_left
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    SQL=MySQL(info)
    return [SQL.Query(q) for q in query]

class MySQL:
    def __init__(self, info: list):
        self.createTable(info)

    def createTable(self, info:list):
        self.table=defaultdict(list)
        for applicant in info:
            *ablities, score = applicant.split()
            for i in range(5):
                for comb in combinations(ablities, i):
                    self.table[''.join(comb)].append(int(score))
        for ability in self.table.keys(): self.table[ability].sort()    
        # self.table={ ability:[] for ability in ['cpp','java','python','backend', 'frontend', 'junior','senior', 'chicken', 'pizza']}
        # self.score=[]
        # for idx, applicant in enumerate(info):
        #     *abilities, score = applicant.split()
        #     for ability in abilities: self.table[ability].append(idx)
        #     self.score.append(int(score))

    def Query(self, query: str) -> int:
        *abilites, score = re.sub('and|-','', query).split()
        return len(self.table[''.join(abilites)]) - bisect_left(self.table[''.join(abilites)], int(score))
        # *abilites, score =re.sub('and|-', '', query).split()
        # if not abilites: return len(self.score) - bisect_left(sorted(self.score), int(score))
        # else: 
        #     eligible=set(self.table[abilites[0]])
        #     for ability in abilites[1:]: eligible.intersection_update(self.table[ability])
        #     return len(eligible) - bisect_left(sorted([self.score[idx] for idx in eligible]), int(score))
            

if __name__=="__main__":
    info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))
