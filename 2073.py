from typing import List

def timeRequiredToBuy(tickets: List[int], k: int) -> int:
	count = 0
	while tickets[k] != 0:
		for i in range(len(tickets)):
			if tickets[i] != 0:
				tickets[i] -= 1
				count += 1
			if tickets[k] == 0:
				break
	return count


