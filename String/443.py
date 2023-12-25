from typing import List


def compress(chars: List[str]) -> int:
	chars.append(" ")
	i, c = 1, 1
	while i < len(chars):
		if chars[i] == chars[i - 1]:
			chars.pop(i)
			c += 1
		else:
			if c == 1:
				i += 1
			else:
				for j in str(c):
					chars.insert(i, j)
					i += 1
				i += 1
				c = 1
	chars.pop()
	return len(chars)


if __name__ == '__main__':
	# char = ["a", "a", "b", "b", "c", "c", "c"]
	# assert compress(char) == 6
	assert compress(chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c"]) == 5
