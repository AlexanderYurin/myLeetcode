from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    return max(map(sum, accounts))


if __name__ == '__main__':
    assert maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]) == 6
