
#### Passing arguments to decorators

'''
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
@tags("q")
@tags("r")
def get_text(name):
    return "Hello "+name

print get_text("John")
'''

#### Debugging decorated functions

## At the end of the day decorators are just wrapping our 
## functions, in case of debugging that can be problematic 
## since the wrapper function does not carry the name, 
## module and docstring of the original function.

### Functools to the rescue
## Wraps is a decorator for updating the attributes of the 
## wrapping function(func_wrapper) to those of the original 
## function(get_text). This is as simple as decorating 
## func_wrapper by @wraps(func).


from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name

print get_text.__name__ # get_text
print get_text.__doc__ # returns some text
print get_text.__module__ # __main__




"""
# Where to use decorators ?

The examples in this post are pretty simple relative to how much 
you can do with decorators. They can give so much power and elegance 
to your program. In general, decorators are ideal for extending the 
behavior of functions that we don't want to modify. For a great list 
of useful decorators I suggest you check out the Python Decorator Library

## More help in : http://thecodeship.com/patterns/guide-to-python-function-decorators/

https://wiki.python.org/moin/PythonDecorators#What_is_a_Decorator
http://www.artima.com/weblogs/viewpost.jsp?thread=240808
http://www.artima.com/weblogs/viewpost.jsp?thread=240845
http://www.artima.com/weblogs/viewpost.jsp?thread=241209


"""




