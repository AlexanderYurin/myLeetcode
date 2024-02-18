from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
	route_asteroids = []
	for i in range(len(asteroids)):
		if len(route_asteroids) == 0:
			route_asteroids.append(asteroids[i])
			continue
		left_asteroid = route_asteroids.pop()
		asteroid = asteroids[i]
		if left_asteroid > 0 > asteroid:
			while left_asteroid and asteroid:
				if abs(left_asteroid) > abs(asteroid):
					asteroid = None
				elif abs(left_asteroid) < abs(asteroid):
					if len(route_asteroids) > 0:
						left_asteroid = route_asteroids.pop()
						if left_asteroid < 0 > asteroid or left_asteroid > 0 < asteroid:
							route_asteroids += [left_asteroid, asteroid]
							break
					else:
						left_asteroid = None
				else:
					left_asteroid = asteroid = None
					break

			else:
				route_asteroids.append(left_asteroid or asteroid)
		else:
			route_asteroids += [left_asteroid, asteroid]
	return route_asteroids


if __name__ == '__main__':
	assert asteroidCollision([1, -1, -2, -2]) == [-2, -2]
	assert asteroidCollision([-2, -2, 1, -2]) == [-2, -2, -2]
	assert asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
	assert asteroidCollision(asteroids=[5, 10, -5]) == [5, 10]
	assert asteroidCollision(asteroids=[5, -5]) == []
	assert asteroidCollision(asteroids=[10, 4, -11]) == [-11]
