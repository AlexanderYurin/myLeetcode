from typing import List
from collections import defaultdict


def maximumNumberOfStringPairs(words: List[str]) -> int:
	# hash_set = set()
	# i, j = 0, 1
	# while i != len(words):
	# 	if j == len(words) or words[i] in hash_set:
	# 		i += 1
	# 		j = i + 1
	# 		continue
	# 	if words[i] == words[j][::-1]:
	# 		hash_set.add(words[j])
	# 		i += 1
	# 		j = i + 1
	# 		continue
	# 	else:
	# 		j += 1
	#
	# return len(hash_set)

	d = defaultdict(int)

	for word in words:
		d[min(word, word[::-1])] += 1

	return len(list(filter(lambda x: x == 2, d.values())))




if __name__ == '__main__':
	assert maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"]) == 2
	assert maximumNumberOfStringPairs(words=["aa", "wj", "zp", "df", "xb", "sa", "jw", "pz"]) == 2
