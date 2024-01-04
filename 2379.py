def minimumRecolors(blocks: str, k: int) -> int:
	start = right = count = 0
	min_count = float("inf")
	while right < len(blocks):
		if min_count == 0:
			return 0
		if right - start < k:
			if blocks[right] == "W":
				count += 1
			right += 1
		if right - start == k:
			min_count = min(min_count, count)
			if blocks[start] == "W":
				count -= 1
			start += 1

	return min_count


if __name__ == '__main__':
	assert minimumRecolors(blocks="WBBB", k=3) == 0
	assert minimumRecolors(blocks="WBBWWBBWBW", k=7) == 3
	assert minimumRecolors(blocks="WBWBBBW", k=2) == 0
