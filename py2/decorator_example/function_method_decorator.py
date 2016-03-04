### make our decorator useful for functions and methods alike. 
### This can be done by putting *args and **kwargs as parameters 
### for the wrapper, then it can accept any arbitrary number of 
### arguments and keyword arguments.

def p_decorator(func):
    def func_wrapper(*args,**kwargs):
        return "<p>{0}<p>".format(func(*args, **kwargs))
    return func_wrapper

class Person(object):
    def __init__(self):
        self.first = "Soumya"
        self.last = "Suansia"
        
    @p_decorator
    def get_fullname(self):
        return self.first + " " +self.last

my_name = Person()
print "My Full Name: " + my_name.get_fullname()

@p_decorator
def emp_full_name(name):
    return "Hi {0} !!!".format(name)

print "Greet the employee .. "+emp_full_name("Jhon Chamber")