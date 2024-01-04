from collections import Counter
from typing import List


# You are given two 0-indexed integer arrays nums1 and nums2 of sizes n and m, respectively.
#
# Consider calculating the following values:
#
# The number of indices i such that 0 <= i < n and nums1[i] occurs at least once in nums2.
# The number of indices i such that 0 <= i < m and nums2[i] occurs at least once in nums1.
# Return an integer array answer of size 2 containing the two values in the above order.
def findIntersectionValues(nums1: List[int], nums2: List[int]) -> List[int]:
	hash_nums1 = set(nums1)
	hash_nums2 = set(nums2)
	return [sum([1 for i in range(len(nums1)) if i < len(nums1) and nums1[i] in hash_nums2]),
			sum([1 for i in range(len(nums2)) if i < len(nums2) and nums2[i] in hash_nums1])]


if __name__ == '__main__':
	assert findIntersectionValues(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]) == [3, 4]
	assert findIntersectionValues(nums1=[3, 4, 2, 3], nums2=[1, 5]) == [0, 0]
