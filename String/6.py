def convert(s: str, numRows: int) -> str:
	length_s = len(s)
	if numRows < 2:
		return s
	result = [[] for _ in range(numRows)]
	count = 0
	index = 0
	while index != length_s:
		if count == numRows:
			count = numRows - 2
			while count != 0:
				try:
					result[count].append(s[index])
					count -= 1
					index += 1
				except IndexError:
					break
		else:
			result[count].append(s[index])
			count += 1
			index += 1

	return "".join(map(lambda x: "".join(x), result))


assert convert(s="PAYPALISHIRING", numRows=4) == "PINALSIGYAHRPI"
assert convert(s="PAYPALISHIRING", numRows=3) == "PAHNAPLSIIGYIR"
assert convert(s="AB", numRows=1) == "AB"


# class Solution(object):
# 	def convert(self, s, numRows):
# 		if numRows == 1 or numRows >= len(s):
# 			return s
#
# 		rows = [[] for row in range(numRows)]
# 		index = 0
# 		step = -1
# 		for char in s:
# 			rows[index].append(char)
# 			if index == 0:
# 				step = 1
# 			elif index == numRows - 1:
# 				step = -1
# 			index += step
#
# 		for i in range(numRows):
# 			rows[i] = ''.join(rows[i])
# 		return ''.join(rows)