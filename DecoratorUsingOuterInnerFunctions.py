#Decorator Understanding Using Outer and Inner Functions

def OuterFunction(msg):
    
    def inner_function():
        print(msg)
    return inner_function
    
def OuterFunctionMethod2(msg):
    
    def inner_function():
        print(msg)
    return inner_function()
    
def main():
    
    call_outer_function = OuterFunction("Hi")
    
    call_outer_function()
    
def main2():
    OuterFunctionMethod2("Hi")
    
if __name__ == "__main__":
    main2()