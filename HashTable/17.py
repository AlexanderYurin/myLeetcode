from typing import List


def letterCombinations(digits: str) -> List[str]:
	result = []
	dict_letters = {
		"2": "abc", '3': "def", '4': "ghi", '5': "jkl",
		'6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
	}

	def get_letter_comb(nums, word=""):
		if not nums:
			return word
		for let in dict_letters[nums[0]]:
			word += let
			word = get_letter_comb(nums[1:], word) or word
			if len(word) == len(digits):
				result.append(word)
			word = word[:len(word)-1] or ""

	get_letter_comb(digits)
	return result


if __name__ == '__main__':
	assert letterCombinations("999") == ["www", "wwx", "wwy", "wwz", "wxw", "wxx", "wxy", "wxz", "wyw", "wyx", "wyy",
										 "wyz", "wzw", "wzx", "wzy", "wzz", "xww", "xwx", "xwy", "xwz", "xxw", "xxx",
										 "xxy", "xxz", "xyw", "xyx", "xyy", "xyz", "xzw", "xzx", "xzy", "xzz", "yww",
										 "ywx", "ywy", "ywz", "yxw", "yxx", "yxy", "yxz", "yyw", "yyx", "yyy", "yyz",
										 "yzw", "yzx", "yzy", "yzz", "zww", "zwx", "zwy", "zwz", "zxw", "zxx", "zxy",
										 "zxz", "zyw", "zyx", "zyy", "zyz", "zzw", "zzx", "zzy", "zzz"]
	assert letterCombinations("234") == ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh",
										 "bdi", "beg", "beh", "bei",
										 "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh",
										 "cfi"]
	assert letterCombinations(digits="22") == ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
	assert letterCombinations(digits="23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
	assert letterCombinations(digits="2") == ["a", "b", "c"]
