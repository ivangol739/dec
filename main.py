import datetime
import random

from tools import time_check, attempts


# def foo(*args, **kwargs):
# 	print(args)
# 	print(kwargs)
#
# foo(1, 3, "py", None, a=12, sf="regrgerv")


# def foo(a, b, c , d='dssdvv'):
# 	print(f'{a=}')
# 	print(f'{b=}')
# 	print(f'{c=}')
# 	print(f'{d=}')
#
# some_turple = (1,2,3)
# some_dict = {'d': 'wdsdvsvfsvfv'}
#
# foo(*some_turple, **some_dict)

# def wrapper(func, *args, **kwargs):
# 	print(f"Вызвали функцию {func} с аргументами {args} и {kwargs}")
# 	print(f"Время: {datetime.datetime.now()}")
# 	result = func(*args, **kwargs)
# 	print(f"Результат работы = {result}")
# 	return result
#
#
# # print(sum([1,2,3,4,5]))
# result = wrapper(sum, [1,2,3,4,5])
# print(result)

# def foo():
# 	return sum
#
# print(foo())

def decorator(old_func):
	def new_func(*args, **kwargs):
		print(f"Вызвали функцию {old_func} с аргументами {args} и {kwargs}")
		print(f"Время: {datetime.datetime.now()}")
		result = old_func(*args, **kwargs)
		print(f"Результат работы = {result}")
		return result
	return new_func

# decored_func = decorator(sum)
# print(decored_func([1,2,3,4,5]))

@decorator
def sum(a, b, c):
	return a + b + c

print(sum(1, 2, 3))


# @time_check
# def generate_max_number(iterations):
# 	max_ = 0
# 	for _ in range(iterations):
# 		num = random.randint(0, 1_000_000_000)
# 		if num > max_:
# 			max_ = num
# 	return max_
#
# print(generate_max_number(10_000_000))


@attempts
def divide_(a, b):
	return a / b

print(divide_(10, 0))
