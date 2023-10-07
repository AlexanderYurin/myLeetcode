from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
	return "".join(word1) == "".join(word2)


assert arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]) is True
