from typing import List
from collections import Counter

def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    # items_dict = {}
    # for item in items1 + items2:
    #     items_dict.setdefault(item[0], 0)
    #     items_dict[item[0]] += item[1]
    # return [[k, v] for k, v in sorted(items_dict.items(), key=lambda x: x[0])]
    res = Counter(dict(items1))
    res += Counter(dict(items2))
    return sorted(res.items())




if __name__ == '__main__':
    assert mergeSimilarItems(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]) == [[1, 6], [3, 9], [4, 5]]
    assert mergeSimilarItems(items1=[[1, 1], [3, 2], [2, 3]], items2=[[2, 1], [3, 2], [1, 3]]) == [[1, 4], [2, 4],
                                                                                                   [3, 4]]
