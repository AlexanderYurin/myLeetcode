def numberOfSteps(num: int) -> int:
    if num == 0:
        return 0
    if num % 2 == 0:
        return 1 + numberOfSteps(num // 2)
    return 1 + numberOfSteps(num - 1)


if __name__ == '__main__':
    assert numberOfSteps(num = 14) == 6
