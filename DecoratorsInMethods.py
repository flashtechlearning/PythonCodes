

def calculator_function(operation_function):
	
	def wrapper_function(*args , **kwargs):
		print('Wrapper functin executed before {}'.format(operation_function.__name__))
		return operation_function(*args , **kwargs)
	return wrapper_function
	


@calculator_function
def add():
	print('Add function called')
    

@calculator_function
def add_two_numbers(a , b):
	print('Add for 2 numbers called')


add()
add_two_numbers(1,2)