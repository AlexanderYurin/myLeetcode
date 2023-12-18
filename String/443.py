from typing import List


def compress(chars: List[str]) -> int:
	i, j, c = 0, 1, 1
	while j < len(chars):
		if chars[i] == chars[j]:
			c += 1
			chars.pop(j)
		else:
			if c > 1:
				chars.insert(j, *list(str(c)))
				c = 1
				i = j + 1
				j += 2
			else:
				i = j
				j += 1
	if c > 1:
		chars.insert(j, *list(str(c)))
	return len(chars)



if __name__ == '__main__':
	char = ["a", "a", "b", "b", "c", "c", "c"]
	assert compress(char) == 6
	print(char)
	assert compress(chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 5
