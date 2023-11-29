from typing import List


def maximumStrongPairXor(nums: List[int]) -> int:
    nums.sort()
    uniqXOR = set()
    for i_x in range(len(nums)):
        for i_y in range(i_x, len(nums)):
            if abs(nums[i_x]-nums[i_y]) <= min(nums[i_x], nums[i_y]):
                uniqXOR.add((nums[i_x] ^ nums[i_y]))
            else:
                break
    return max(uniqXOR)
    # return max((x ^ y for x, y in
    #             filter(lambda x: x[0] <= x[1] <= 2 * x[0],
    #                    permutations(nums, 2))), default=0)




if __name__ == '__main__':
    assert maximumStrongPairXor([1,1,10,3,9]) == 3
    assert maximumStrongPairXor(nums = [1,2,3,4,5]) == 7
    assert maximumStrongPairXor(nums = [10,100]) == 0
