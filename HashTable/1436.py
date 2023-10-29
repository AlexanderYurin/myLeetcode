from typing import List


def destCity(paths: List[List[str]]) -> str:
	citys = {city[0]: city[1] for city in paths}

	for c in citys:
		if citys.get(citys[c]) is None:
			return citys[c]




if __name__ == '__main__':
	assert destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]) == "Sao Paulo"
