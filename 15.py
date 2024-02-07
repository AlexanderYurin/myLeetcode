from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    if len(nums) == 3:
        result = sum(nums)
        if result == 0:
            return [nums]
        return []
    result = []
    i, j = 0, 1
    hash_set = set()
    while i < len(nums) - 2:
        if j == len(nums):
            i += 1
            j = 0
        if nums[i] not in hash_set and nums[j] not in hash_set:
            k = -(nums[i] + nums[j])
            for i_num in range(len(nums)):
                if nums[i_num] == k and i_num != i and i_num != j:
                    result.append([nums[i], nums[j], k])
                    hash_set.add(nums[i])
                    hash_set.add(nums[j])
                    break
        j += 1
    return result


if __name__ == '__main__':
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
