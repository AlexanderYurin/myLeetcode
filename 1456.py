def maxVowels(s: str, k: int) -> int:
	vowels = {'a', 'e', 'i', 'o', 'u'}
	left = 0
	right = 0
	max_cur = 0
	cur = 0
	while left + k <= len(s):
		if max_cur == k:
			return k
		if s[right] in vowels:
			cur += 1
		right += 1
		max_cur = max(max_cur, cur)
		if right - left >= k:
			if s[left] in vowels:
				cur -= 1
			left += 1
	return max_cur


if __name__ == '__main__':
	assert maxVowels(s="aeiou", k=2) == 2
	assert maxVowels(s="weallloveyou", k=7) == 4
