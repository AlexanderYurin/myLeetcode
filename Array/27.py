from typing import List


def removeElement(nums: List[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


if __name__ == '__main__':
    assert removeElement(val=2, nums=[0, 1, 2, 2, 3, 0, 4, 2]) == 5
