from typing import List
import collections


def uniqueOccurrences(arr: List[int]) -> bool:
    hash_map = collections.Counter(arr)
    return len(hash_map) == len(set(hash_map.values()))



if __name__ == '__main__':
    assert uniqueOccurrences(arr = [1,2,2,1,1,3]) is True
    assert uniqueOccurrences(arr=[1, 2, 1, 1, 3]) is False
