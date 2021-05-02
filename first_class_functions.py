################
# First class functions allow us to treat functions as any other variables or objects
# Closures are functions that are local inner functions within outer functions that remember the arguments passed to the outer functions
#################


def square(x):
	return x*x

def my_map_function(func , arg_list):
    result = []
    
    for item in arg_list:
        result.append(func(item))
    
    
    return result


int_array = [1,2,3,4,5]

f = my_map_function(square , int_array)

#print(f)
#print(my_map_function(square , int_array))

def logger(msg):
    
    def log_message():
        print('Log:' , msg)
    
    return log_message
    

log_hi = logger('Hi')
log_hi()


#Closure Example

def my_log(msg):
    
    def logging(*args):
        print('Log Message {} , Logging Message {} '.format(msg , args))
    
    return logging


log_hi = my_log('Console 1')
log_hi('Hi')
