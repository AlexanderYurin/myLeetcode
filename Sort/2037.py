from typing import List


def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    seats.sort()
    students.sort()
    return sum(map(lambda x: abs(x[0] - x[1]), zip(seats, students)))


if __name__ == '__main__':
    assert minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]) == 4
    assert minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]) == 7
