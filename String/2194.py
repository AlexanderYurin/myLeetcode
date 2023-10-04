from typing import List


def cellsInRange(s: str) -> List[str]:
	from string import ascii_uppercase as au
	array = s.split(":")
	nums = list(range(int(array[0][1]), int(array[1][1]) + 1))
	letters = list(range(au.index(array[0][0]), au.index(array[1][0]) + 1))
	result = [f"{au[letter]}{num}" for letter in letters for num in nums]
	return result


assert cellsInRange(s="K1:L2") == ["K1", "K2", "L1", "L2"]
assert cellsInRange(s= "A1:F1") == ["A1","B1","C1", 'D1', "E1", "F1"]
