# from typing import List
#
#
# def moveZeroes(nums: List[int]) -> None:
# 	"""
#     Do not return anything, modify nums in-place instead.
#     """
#
# 	# nums.sort(key=lambda x: x == 0)
# 	# return nums
# 	n = 0
# 	for i in range(len(nums)):
# 		if nums[i]:
# 			nums[n], nums[i] = nums[i], nums[n]
# 			n += 1
#
#
# if __name__ == '__main__':
# 	assert moveZeroes([0, 0, 1]) == [1, 0, 0]
from collections import Counter


def isSubsequence(s: str, t: str) -> bool:
    print(list(Counter("".join([let for let in t if let in s])).keys()) == list(Counter(s).keys()))
    return s in "".join([let for let in t if let in s])


isSubsequence("abc", "ahbgdc")
