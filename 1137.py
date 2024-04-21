
memory = {0:0, 1:1, 2:1}
def tribonacci(n: int) -> int:
    if n in memory:
        return memory[n]
    memory[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    return memory[n]

if __name__ == '__main__':
    assert tribonacci(4) == 4
    assert tribonacci(3) == 2
