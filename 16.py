from itertools import combinations
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    array = set(map(lambda x: sum(x), combinations(nums, 3)))
    l, r = target-1, target+1
    while 1:
        if target in array:
            return target
        if l in  array:
            return l
        if r in  array:
            return r
        l -= 1
        r += 1



if __name__ == '__main__':
    assert threeSumClosest(nums = [-1,2,1,-4], target = 1) == 2
    assert threeSumClosest(nums=[0,0,0], target=1) == 0
