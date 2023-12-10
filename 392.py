from collections import deque


def isSubsequences(s: str, t: str) -> bool:
	hash_s = set(s)
	deque_s = deque(s)
	t = (elem for elem in t if elem in hash_s)
	for elem in t:
		if len(deque_s) == 0:
			return True
		if elem == deque_s[0]:
			deque_s.popleft()
	return len(deque_s) == 0


if __name__ == '__main__':
	assert isSubsequences(s="abc", t="ahbgdc") is True
	assert isSubsequences(s="axc", t="ahbgdc") is False
	assert isSubsequences(s="acb", t="ahbgdc") is False
