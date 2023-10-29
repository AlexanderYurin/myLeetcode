from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	"""
    Do not return anything, modify nums1 in-place instead.
    """
	for i in nums2:
		nums1.append(i)
		nums1.remove(0)
	nums1.sort()




if __name__ == '__main__':
	nums1 = [1, 2, 3, 0, 0, 0]
	assert merge(nums1=nums1, m=3, nums2=[2, 5, 6], n=3) is None
	print(nums1)
