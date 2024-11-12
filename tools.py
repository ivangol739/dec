import datetime
import time


def time_check(old_func):
	def new_func(*args, **kwargs):
		start = datetime.datetime.now()
		result = old_func(*args, **kwargs)
		end = datetime.datetime.now()
		time = end - start
		print(f"Была вызвана функция {old_func.__name__}\n"
					f"с аргументами {args} и {kwargs}\n"
					f"результат {result}\n"
					f"Время работы {time}")
		return result
	return new_func


ATTEMPTS = 3
TIMEOUT = 1

def attempts(old_func):
	def new_func(*args, **kwargs):
		error = None
		for i in range(ATTEMPTS):
			try:
				result = old_func(*args, **kwargs)
				return result
			except Exception as err:
				print(f"Попытка {i + 1}. Ошибка {err}")
				time.sleep(TIMEOUT)
				error = err
		raise error
	return new_func

def attempts_2(attempts, timeout):
