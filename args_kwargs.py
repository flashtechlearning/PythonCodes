
# The *args,**kwargs is used for passing any number of arguments
# args is for the arguments
# kwargs is for key word arguments
# key word arguments should be passed as key=arg as parameter to the function
# args can be passed separated by commas, else the whole string is considered as a tuple

def display(*args , **kwargs):

	for key , arg in kwargs.items():
		print('key : {} arg : {}'.format(key,arg))

	for item in args:
		print(item)

	print('Number of Parameters:{}'.format(len(args)))
	print('Number of Keyword Parameters:{}'.format(len(kwargs)))


#display('name middle_name', 'surname' , 'profession', gender='male' , age='26' , city='belgaum')

print('****************')


display('github code' , 'commit' , message='Understanding args and kwargs')
