'''
Essentially, decorators work as wrappers, modifying the behavior 
of the code before and after a target function execution, without 
the need to modify the function itself, augmenting the original 
functionality, thus decorating it.
'''

'''
### Type # 1
### Assign functions to variables

def greet(name):
    return "Hello " + name + " .."

greet_someone = greet

print greet_someone("Soumya")

'''

'''
### Type # 2
### Define functions inside other functions

def greet(name):
    def getmessage():
        return "Hello "
    
    result = getmessage() + name
    return result

print greet("Soumya ..")

'''

'''
### Type # 3
### Functions can be passed as parameters to other functions

def greet(name):
    return "Hello " + name

def call_function (func):
    othername = "Ranjan"
    return func(othername)

print call_function(greet)

'''

'''
### Tyep # 4
### Functions can return other functions

def compose_greet_function():
    def greet(name):
        return "Hello " + name + " .."
    
    return greet

greet_someone = compose_greet_function()
print "Lets greet some one: " + greet_someone(str(raw_input("What your Name: ")))

'''

'''
### Type # 5
### Inner functions have access to the enclosing scope

def compose_greet_function(name):
    def get_message():
        return "Hello " + name + " !!!"
    
    return get_message

greet = compose_greet_function("Ranjan")
print greet()

'''
'''
##### Composition of DECORATORs
## Function decorators are simply wrappers to existing functions. 
## Putting the ideas mentioned above together,

def get_text(name):
    return "hay guys .. {0} is a number to our team ..".format(name)

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}<p>".format(func(name))
    return func_wrapper

my_get_text = p_decorate(get_text)
print my_get_text("Ranjan")

get_text = p_decorate(get_text)
print get_text("Soumya")

'''

### Python way of decorators


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}<p>".format(func(name))
    return func_wrapper

def q_decorate(func):
    def func_wrapper(name):
        return "<q>{0}<q>".format(func(name))
    return func_wrapper

def r_decorate(func):
    def func_wrapper(name):
        return "<r>{0}<r>".format(func(name))
    return func_wrapper

@p_decorate
@q_decorate
@r_decorate
def get_text(name):
    return "hay guys .. {0} is a number to our team ..".format(name)

print get_text("Ranjan")







