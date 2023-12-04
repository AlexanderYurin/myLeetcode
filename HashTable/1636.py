from collections import Counter, defaultdict
from typing import List


def frequencySort(nums: List[int]) -> List[int]:
    # hash_map = {}
    # result = []
    # for num in set(nums):
    # 	num_count = nums.count(num)
    # 	hash_map.setdefault(num_count, [])
    # 	hash_map[num_count].append(num)
    # for n in sorted(hash_map):
    # 	result += sorted((elem for elem in hash_map[n] for _ in range(n)), reverse=True)
    # return result

    counts_dict = Counter(nums)
    return sorted(nums, key=lambda x: (counts_dict[x], -x))

if __name__ == '__main__':
    assert frequencySort(nums=[1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]
    assert frequencySort([2, 3, 1, 3, 2]) == [1, 3,3, 2, 2]
