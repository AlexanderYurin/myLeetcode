from typing import List
from collections import Counter


def repeatedNTimes(nums: List[int]) -> int:
    # dict_nums = Counter(nums)
    # return sorted(dict_nums.items(), key=lambda num: num[1])[-1][0]
    uniq_num = set()
    for num in iter(nums):
        if num in uniq_num:
            return num
        else:
            uniq_num.add(num)

if __name__ == '__main__':
    assert repeatedNTimes(nums=[1, 2, 3, 3]) == 3
    assert repeatedNTimes(nums=[2, 1, 2, 5, 3, 2]) == 2
    assert repeatedNTimes(nums=[5, 1, 5, 2, 5, 3, 5, 4]) == 5
