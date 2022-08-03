from functools import wraps

def my_decorator(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		"""wrapper docstring"""
		print("Calling decorated function")
		return f(*args, **kwargs)
	return wrapper


@my_decorator
def example():
	"""Docstring"""
	print("Called example func")


if __name__ == '__main__':
	example()
	print(example.__name__)
	print(example.__doc__)


# readme:
# 主要是利用functools.wraps來觸發到update_wrapper()，藉此來讓decorator不干涉到使用decorator的func中的name、doc
# 可以把上例中@wraps(f)註解起來觀察輸出結果

# 有@wraps(f)
# Calling decorated function
# Called example func
# example
# Docstring

# 沒@wraps(f)
# Calling decorated function
# Called example func
# wrapper
# wrapper docstring
