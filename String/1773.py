from typing import List


def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
	dict_key = dict(type=0, color=1, name=2)
	return len(list(filter(lambda x: x[dict_key[ruleKey]] == ruleValue, items)))


assert countMatches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
					 ["phone", "gold", "iphone"]], ruleKey="color", ruleValue="silver") == 1
