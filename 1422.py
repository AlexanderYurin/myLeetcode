def maxScore(s: str) -> int:
	i, j, k = 0, 0, 0
	n = [0 for _ in range(len(s) - 1)]
	while i < len(s) - 1:
		if s[i] == "0":
			j += 1
		n[i] += j
		i += 1
		if s[-i] == "1":
			k += 1
		n[-i] += k
	return max(n)


if __name__ == '__main__':
	assert maxScore(s="011101") == 5
	assert maxScore(s="1111") == 3
