from typing import List


def maxArea(height: List[int]) -> int:
	left = 0
	right = len(height) - 1
	max_area = 0

	while left < right:
		current_area = min(height[left], height[right]) * (right - left)
		max_area = max(max_area, current_area)

		if height[left] < height[right]:
			left += 1
		else:
			right -= 1

	return max_area


if __name__ == '__main__':
	assert maxArea(height=[1, 2, 3, 4, 5, 25, 24, 3, 4]) == 24
	assert maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
	assert maxArea(height=[1, 2, 3, 4, 5]) == 6
	assert maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
	assert maxArea(height=[1, 1]) == 1
