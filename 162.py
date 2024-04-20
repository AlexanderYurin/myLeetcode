from typing import List


def findPeakElement(nums: List[int]) -> int:
    def binary_search(left, right):
        mid = (left + right) // 2
        l = mid - 1 if mid - 1 >= 0 else 0
        r = mid + 1 if mid + 1 <= len(nums) - 1 else len(nums) - 1

        if nums[l] <= nums[mid] >= nums[r]:
            return mid
        if nums[l] > nums[mid]:
            return binary_search(left, mid)
        else:
            return binary_search(mid, right)


    return binary_search(0, len(nums))

if __name__ == '__main__':
    assert findPeakElement([2,3,4,3,2,1]) == 2
    assert findPeakElement([1,2,3,4,3,2]) == 3
    assert findPeakElement([1,3,2,1]) == 1
    assert findPeakElement([1]) == 0
    assert findPeakElement([1,2]) == 1
    assert  findPeakElement([1,2,3,1]) == 2
    assert findPeakElement([1,2,1,3,5,6,4]) == 5
    assert findPeakElement([3,2,1]) == 0
    assert findPeakElement([1,2,3]) == 2
