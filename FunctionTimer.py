

def my_timer(original_function):
    import time
    def wrapper_function():
        t1 = time.time()
        result = original_function()
        t2 = time.time() - t1
        
        print('{} ran for {} ms'.format(original_function.__name__ , t2))
        
        return result
    
    return wrapper_function
    
@my_timer
def func1():
    import time
    
    time.sleep(2)
    
    
func1()