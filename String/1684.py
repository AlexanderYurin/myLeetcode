from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
	count = 0
	for word in words:
		for letter in word:
			if letter not in allowed:
				break
		else:
			count += 1
	return count


if __name__ == '__main__':
	assert countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]) == 2
	assert countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7
