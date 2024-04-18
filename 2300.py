from collections import defaultdict
from math import ceil
from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    memory = defaultdict(int)
    result = []

    potions.sort()

    def binary_search(array, num, left, right):
        if array[-1] < num:
            return 0
        if left >= right:
            return len(array) - left
        mid = (left + right) // 2
        if array[mid] == num:
            while array[mid] == num:
                if mid == 0:
                    break
                mid -= 1
            else: mid += 1
            return len(array) - mid

        if array[mid] > num:
            return binary_search(array, num, left, mid)
        else:
            return binary_search(array, num, mid+1, right)

    for i in range(len(spells)):
        if spells[i] not in memory:
            min_potion = ceil(success / spells[i])
            memory[spells[i]] = binary_search(potions, min_potion, 0, len(potions))

        result.append(memory[spells[i]])

    return result



if __name__ == "__main__":
    assert successfulPairs([1], [1], 1) == [1]
    assert successfulPairs(
        spells=
        [22, 13, 21, 13, 11, 9, 13, 35, 7, 38, 10, 10, 38, 19, 3, 16, 13, 24, 16, 27, 20, 24, 32, 5, 16, 35, 24, 2, 25,
         32, 20, 22, 22, 3, 35, 39, 27, 26, 25, 21, 27, 40, 15, 17, 24, 40, 35, 27, 20, 40, 9, 35, 27, 19, 15, 34, 35,
         37, 17, 40, 8, 3, 33, 39, 29, 22, 30, 1, 37, 2, 16, 30, 32, 31, 24, 6, 34, 26, 36, 4, 21, 2, 29, 31, 3, 27, 6,
         24, 40, 18],
        potions=
        [33, 16, 35, 14, 26, 23, 23, 2, 37, 23, 15, 20, 25, 34, 23, 29, 4, 18, 26, 24, 16, 37, 15, 11, 33, 24, 12, 13,
         7, 24, 3, 26, 1, 3, 38, 33, 19, 3, 34, 22, 30, 39, 18, 7, 21, 4, 33, 18, 39, 5, 34, 14, 32, 5, 20, 22, 5, 25,
         15],
        success=533
    ) == [21,0,19,0,0,0,0,39,0,42,0,0,42,16,0,9,0,28,9,33,16,28,37,0,9,39,28,0,30,37,16,21,21,0,39,44,33,31,30,19,33,44,5,14,28,44,39,33,16,44,0,39,33,16,5,39,39,42,14,44,0,0,37,44,34,21,37,0,42,0,9,37,37,37,28,0,39,31,42,0,19,0,34,37,0,33,0,28,44,15]

    assert successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7) == [4,0,3]
    assert successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16) == [2,0,2]
