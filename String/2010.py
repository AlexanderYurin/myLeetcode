from typing import List


def finalValueAfterOperations(operations: List[str]) -> int:
	result = 0
	for i in operations:
		if i == "++X" or i == "X++":
			result += 1
			continue
		result -= 1
	return result


assert finalValueAfterOperations(["++X", "X++", "--X", "X--"]) == 0
assert finalValueAfterOperations(["++X", "X++", "--X"]) == 1
