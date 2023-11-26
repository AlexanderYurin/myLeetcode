from itertools import zip_longest


def mergeAlternately(word1: str, word2: str) -> str:
	# return "".join(elem[0]+elem[1] for elem in (zip_longest(word1, word2, fillvalue="")))
	i = 0
	result = ""
	while i != len(word1) and i != len(word2):
		result += word1[i] + word2[i]
		i += 1

	result += word1[i:] + word2[i:]

	return result


if __name__ == '__main__':
	assert mergeAlternately(word1="abcds", word2="pq") == "apbqcrd"
