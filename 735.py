from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for asteroid in asteroids:
        if len(stack) == 0:
            stack.append(asteroid)
            continue

        last_asteroid = stack.pop()

        if last_asteroid + asteroid == 0:
            continue

        if max(last_asteroid, asteroid) < last_asteroid + asteroid or min(last_asteroid,
                                                                          asteroid) > last_asteroid + asteroid:
            stack.append(last_asteroid)
            stack.append(asteroid)
            continue

        while 1:
            if last_asteroid < 0:
                if abs(last_asteroid) < asteroid:
                    stack.append(asteroid)
                    break
            else:
                if abs(asteroid) < last_asteroid:
                    stack.append(last_asteroid)
                    break
                else:
                    stack.append(asteroid)
                    break
            
    return stack


if __name__ == '__main__':
    # assert asteroidCollision(asteroids=[5, 10, -5]) == [5, 10]
    # assert asteroidCollision(asteroids=[5, -5]) == []
    assert asteroidCollision(asteroids=[10, 4, -11]) == [-11]
