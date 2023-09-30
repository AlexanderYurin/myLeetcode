from typing import List


def restoreString(s: str, indices: List[int]) -> str:
	hashmap = dict(zip(indices, s))
	sort_array = [hashmap[i] for i in sorted(hashmap.keys())]
	return "".join(sort_array)


assert restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"
