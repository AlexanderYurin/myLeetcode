from typing import List


class OrderedStream:
	def __init__(self, n: int):
		self.flow = [None for i in range(n)]
		self.count = 0

	def insert(self, idKey: int, value: str) -> List[str]:
		self.flow[idKey - 1] = value
		result = []
		while self.count != len(self.flow) and self.flow[self.count] is not None:
			result.append(self.flow[self.count])
			self.count += 1
		return result


if __name__ == '__main__':
	obj = OrderedStream(5)
	param_1 = obj.insert(3, "cccc")
	param_2 = obj.insert(1, "aaaa")
	param_3 = obj.insert(2, "bbbb")
	param_4 = obj.insert(5, "eeee")
	param_5 = obj.insert(4, "dddd")
	print(param_1 + param_2 + param_3 + param_4 + param_5)
	assert param_1 + param_2 + param_3 + param_4 + param_5 == ["aaaa", "bbbb", "cccc", "dddd", "eeee"]
