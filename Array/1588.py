from typing import List


def sumOddLengthSubarrays(arr: List[int]) -> int:
    result = 0

    for i in range(len(arr)):
        try:
            for j in range(1, len(arr) + 1, 2):
                new_arr = arr[i:j + i]
                if len(new_arr) == j:
                    result += sum(new_arr)
                else:
                    raise ValueError
        except ValueError:
            continue
    return result


if __name__ == '__main__':
    assert sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3]) == 58
    assert sumOddLengthSubarrays(arr=[1, 2]) == 3
    assert sumOddLengthSubarrays(arr=[10, 11, 12]) == 66
