def differenceOfSums(n: int, m: int) -> int:
    result = 0
    for num in range(1, n+1):
        if num % m != 0:
            result += num
        else:
            result -= num
    return result


if __name__ == '__main__':
    assert differenceOfSums(10, 3) == 19
