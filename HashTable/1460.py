from collections import Counter
from typing import List


def canBeEqual(target: List[int], arr: List[int]) -> bool:
	return len(Counter(target) - Counter(arr)) == 0