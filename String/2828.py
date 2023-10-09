from typing import List


def isAcronym(words: List[str], s: str) -> bool:
	return "".join(map(lambda x: x[0], words)) == s






assert isAcronym(words = ["alice","bob","charlie"], s = "abc") is True
assert isAcronym(words = ["an","apple"], s = "a") is False