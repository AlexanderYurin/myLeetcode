def removeTrailingZeros(num: str) -> str:
	# for i in range(len(num)-1, -1, -1):
	# 	if num[i] == "0":
	# 		continue
	# 	else:
	# 		return num[:i+1]
	return num.strip('0')


if __name__ == '__main__':
	assert removeTrailingZeros(num="51230100") == "512301"
	assert removeTrailingZeros(num="123") == "123"
	assert removeTrailingZeros(num="1") == "1"
