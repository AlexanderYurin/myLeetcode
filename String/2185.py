from typing import List


def prefixCount(words: List[str], pref: str) -> int:
	return len(list(filter(lambda word: word.startswith(pref), words)))


if __name__ == '__main__':
	assert prefixCount(words=["pay", "attention", "practice", "attend"], pref="at") == 2
	assert prefixCount(words=["leetcode", "win", "loops", "success"], pref="code") == 0
