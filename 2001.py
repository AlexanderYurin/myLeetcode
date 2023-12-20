from typing import List


def interchangeableRectangles(rectangles: List[List[int]]) -> int:
	count = 0
	for i_rectangle in range(len(rectangles)):
		for j_rectangle in range(i_rectangle + 1, len(rectangles)):
			if (rectangles[i_rectangle][0] * rectangles[j_rectangle][1]) \
				/ (rectangles[i_rectangle][1] * rectangles[j_rectangle][0]) == 1:
				count += 1

	return count


if __name__ == '__main__':
	assert interchangeableRectangles(rectangles=[[4, 8], [3, 6], [10, 20], [15, 30]]) == 6
	assert interchangeableRectangles(rectangles=[[4, 5], [7, 8]]) == 0
