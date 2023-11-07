from typing import List

def letterCombinations(digits: str) -> List[str]:
	from collections import deque
	dict_letters = {
		"2": ["a", "b", "c"],
		"3": ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"]
	}
	result = []

	if len(digits) <= 1:
		return dict_letters.get(digits[:1], [])




















if __name__ == '__main__':
	assert letterCombinations(digits="") == []
	assert letterCombinations(digits="2") == ["a", "b", "c"]
