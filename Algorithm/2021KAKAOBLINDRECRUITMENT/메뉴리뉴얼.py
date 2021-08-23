import itertools
from collections import Counter, defaultdict
def solution(orders, course):
    result=[]
    for count_size in course:
        order_combination=Counter()
        for order in orders:
            order_combination += Counter(map(lambda x: ''.join(sorted(x)), itertools.combinations(order,count_size)))
        most_orders = order_combination.most_common()
        result += [k for k,v in most_orders if v>=2 and v==most_orders[0][1]]
    return sorted(result)

if __name__ == "__main__":
    orders=["XYZ", "XWY", "WXA"]
    course=[2,3,4]
    print(solution(orders, course))