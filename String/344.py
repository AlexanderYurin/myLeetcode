from typing import List


def reverseString(s: List[str]) -> None:
	length_s = len(s) // 2
	i, j = 0, -1
	while i < length_s:
		s[i], s[j] = s[j], s[i]
		i += 1
		j -= 1
	return s
# либо  s.reverse()


if __name__ == '__main__':
	s = ["h", "e", "l", "l", "o"]
	assert reverseString(s=s) == ["o", "l", "l", "e", "h"]
	assert reverseString(s=["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]
	print(s)
