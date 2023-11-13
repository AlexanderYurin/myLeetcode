from typing import List


def vowelStrings(words: List[str], left: int, right: int) -> int:
	count = 0
	for word in words[left:right+1]:
		if word[0] in "aeiou" and word[-1] in "aeiou":
			count += 1

	return count


if __name__ == '__main__':
	assert vowelStrings(words=["are", "amy", "u"], left=0, right=2) == 2
