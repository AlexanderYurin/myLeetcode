from typing import List


def maximumNumberOfStringPairs(words: List[str]) -> int:
	result = []
	for i in range(len(words)):
		for j in range(i+1, len(words)):
			if not words[i] in result:
				if words[i] == words[j][::-1]:
					result.append(words[j])
					break

	return len(result)


if __name__ == '__main__':
	assert maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"]) == 2
