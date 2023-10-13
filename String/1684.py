from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
	return len([i for i in words if allowed in i])


if __name__ == '__main__':
	assert countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]) == 2
	assert countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]) == 1
