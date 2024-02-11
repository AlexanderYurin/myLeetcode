# import functools
# import time
# from typing import Callable, Iterator, Generator, Iterable
#
#
# def timer(func: Callable) -> Callable:
# 	@functools.wraps(func)
# 	def wrapper(*args, **kwargs):
# 		start = time.perf_counter()
# 		result = func(*args, **kwargs)
# 		finish = time.perf_counter() - start
# 		print(f"{func.__name__} работала {finish:.4f}с")
# 		return result
#
# 	return wrapper
#
#
# @timer
# def example1():
# 	time.sleep(1)
#
#
# example1()
#
#
# class Timer:
# 	def __init__(self, func_name=None):
# 		self.func_name = func_name
#
# 	def __enter__(self):
# 		self.start = time.perf_counter()
#
# 	def __exit__(self, exc_type, exc_val, exc_tb):
# 		finish = time.perf_counter() - self.start
# 		print(f"{self.func_name} работала {finish:.4f}с")
# 		return False
#
#
# def example2():
# 	time.sleep(2)
#
#
# with Timer(example2.__name__):
# 	example2()
#
#
# class IteratorOddEvenNum(Iterator):
# 	def __init__(self, array, sign=None):
# 		self._array = array
# 		self.sign = sign
# 		self._nums = []
# 		self._index = 0
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		try:
# 			num = self._array[self._index]
# 			if not self.sign:
# 				self._nums.append(num)
# 			elif self.sign == "even":
# 				if num % 2 == 0:
# 					self._nums.append(num)
# 			else:
# 				if num % 2 != 0:
# 					self._nums.append(num)
# 			self._index += 1
# 		except IndexError:
# 			print(f"{self._nums}")
# 			raise StopIteration()
# 		# exit("Итерация закончена!")
#
#
# a = IteratorOddEvenNum([1, 2, 3, 4, 5], "odd")
# for i in a:
# 	next(a)
#
#
# def generator_odd_even_num(array, sign=None) -> Generator:
# 	nums = []
# 	for num in array:
# 		if not sign:
# 			nums.append(num)
# 		elif sign == "even":
# 			if num % 2 == 0:
# 				nums.append(num)
# 		else:
# 			if num % 2 != 0:
# 				nums.append(num)
# 		yield num
# 	print(nums)
# 	return
#
#
# a = generator_odd_even_num([1, 2, 3, 4, 5], "even")
# for i in a:
# 	next(a)



