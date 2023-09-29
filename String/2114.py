from typing import List


def mostWordsFound(sentences: List[str]) -> int:
	return max([i.count(" ") + 1 for i in sentences])


assert mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]) == 6
