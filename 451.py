from collections import Counter


def frequencySort(s: str) -> str:
    return "".join(array[0] * array[1] for array in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True))


if __name__ == '__main__':
    assert frequencySort("tree") == "eetr"
