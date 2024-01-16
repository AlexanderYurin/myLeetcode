def numberOfMatches(n: int) -> int:
    matches = 0
    while n != 1:
        matches += n // 2
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n - 1) / 2 + 1
    return int(matches)


if __name__ == '__main__':
    assert numberOfMatches(7) == 6
