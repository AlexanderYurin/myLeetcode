from collections import defaultdict
from typing import List


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    members_loser = defaultdict(int)
    members = set()
    for match in matches:
        members.add(match[0])
        members.add(match[1])
        members_loser[match[1]] += 1
    answer_1 = []
    answer_2 = []
    for member in members:
        if member not in members_loser:
            answer_1.append(member)
        else:
            if members_loser[member] == 1:
                answer_2.append(member)
    answer_1.sort()
    answer_2.sort()
    return [answer_1, answer_2]


if __name__ == '__main__':
    assert findWinners(matches=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]) == [
        [1, 2, 10], [4, 5, 7, 8]]
