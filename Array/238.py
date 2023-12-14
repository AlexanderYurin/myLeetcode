from functools import reduce
from typing import List
from collections import deque, Counter


def productExceptSelf(nums: List[int]) -> List[int]:
	# queue = deque(nums)
	# total = reduce(lambda x, y: x * y, nums)
	# hash_map = {}
	# product_num = []
	# for _ in range(len(nums)):
	# 	num = queue.popleft()
	# 	hash_map.setdefault(num, reduce(lambda x, y: x * y, queue))
	# 	product_num.append(hash_map[num])
	# 	queue.append(num)
	# return product_num
	total = reduce(lambda x, y: x * y, nums)
	if total > 0:
		return [total // nums[i] for i in range(len(nums))]
	elif nums.count(0) > 1:
		return [0 for _ in range(len(nums))]
	else:
		index_zero = nums.index(0)
		nums.pop(index_zero)
		total_not_zero = reduce(lambda x, y: x * y, nums)
		nums.insert(index_zero, 0)
		return [total_not_zero if nums[i] == 0 else 0 for i in range(len(nums))]


if __name__ == '__main__':
	assert productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
	assert productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

