from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
	# min_word = min(strs, key=lambda x: len(x))
	# strs.remove(min_word)
	# if len(strs) == 0:
	# 	return min_word
	# pref = ""
	# for l in range(len(min_word)):
	# 	if all([min_word[l] == x[l] for x in strs]):
	# 		pref += min_word[l]
	# 	else:
	# 		return pref
	# return pref
	ans = ""
	# После сортировки в конец встало слово которое максимально отличается от первого
	v = sorted(strs)
	first = v[0]
	last = v[-1]
	for i in range(min(len(first), len(last))):
		if first[i] != last[i]:
			return ans
		ans += first[i]
	return ans




if __name__ == '__main__':
	assert longestCommonPrefix(strs=["ab", "a"]) == "a"
	assert longestCommonPrefix(strs=["a"]) == "a"
	assert longestCommonPrefix(strs=["flower", "flow", "flight"]) == "fl"
	assert longestCommonPrefix(strs=["reflower", "flow", "flight"]) == ""
	assert longestCommonPrefix(strs=["ab", "a"]) == "a"
