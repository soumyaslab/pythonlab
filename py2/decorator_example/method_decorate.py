#### Decorating Methods
### In Python, methods are functions that expect their first 
### parameter to be a reference to the current object. We can 
### build decorators for methods the same way, while taking 
### self into consideration in the wrapper function.


def p_decorate(func):
    def function_wrapper(self):
        return "%{0}%".format(func(self))
    
    return function_wrapper

class Person(object):
    def __init__(self):
        self.name = "Soumya"
        self.surname = "Suansia"
    
    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.surname
    
my_name = Person()
print "My Name: " + my_name.get_fullname()



