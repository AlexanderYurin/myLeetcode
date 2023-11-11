def generateTheString(n: int) -> str:
    if n % 2 != 0:
        return "a" * n
    return "a" * (n - 1) + "b" * 1


if __name__ == '__main__':
    assert generateTheString(3) == "aaa"
