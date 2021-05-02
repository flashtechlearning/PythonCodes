class Person:
    
    def __init__(self, first , last):
        self.name = first
        self.surname = last
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.name , self.surname)
    
    @property
    def fullDetails(self):
        return '{} {}'.format(self.name , self.surname)
        
    @fullDetails.setter
    def fullDetails(self , name):
        first , last = name.split(' ')
        self.name = first
        self.surname = last
        
        

p1 = Person('Dhiraj' , 'Bennadi')

print(p1.name)
print(p1.surname)
print(p1.email)
print(p1.fullDetails)


#p1.fullDetails = 'Flash Tech'
#print(p1.name)
#print(p1.surname)
#print(p1.fullDetails)
#print(p1.email)