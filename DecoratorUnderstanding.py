#Understanding of Decorators
#*args , **kwargs

from functools import wraps

def decorator_function(function_to_be_executed):

    @wraps(function_to_be_executed)
    def wrapper_function(*args , **kwargs):
        print('Wrapper function executed before {} '.format(function_to_be_executed.__name__))
        return function_to_be_executed(*args , **kwargs)
    
    return wrapper_function
	

#@decorator_function
def function1():
	print('Function to be executed')
	

#function1()


#The above code is equivalent to Note: Comment the @decorator_function above the function while executing the below code

var = decorator_function(function1)

print('Var is assigned to : {}'.format(var.__name__))
var()



##################
# To use multiple decorators
# from functools import wraps
# and add @wraps(function_to_be_executed) before wrapper_function
##################
