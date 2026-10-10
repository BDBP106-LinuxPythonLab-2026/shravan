def count_calls(func):
   count = 0
   def wrapper():
        nonlocal count  #modify the count variable in the enclosing count_calls function scope rather than creating a new local variable.
        func()
        count+=1
        print("Call count",count)
   return wrapper

@count_calls
def say_hi():

    print("Hi!")
say_hi()
say_hi()
say_hi()
# The expected output is
# Hi!
# Call count: 1
# Hi!

# Call count: 2
# Hi!
# Call count: 3
# def before_after(func):
#    def wrapper():
#         print("Function is starting....")
#         func()
#         print("Function has finished!")
#    return wrapper
#
# @before_after
# def calculate():
#     print("Calculating...")
#
# calculate()

# def my_decorator(func):
#     # 'func' is the original function passed into the decorator
#
#     def wrapper(*args, **kwargs):
#         print("1. Action BEFORE calling the original function")
#
#         # Calling the original function inside the wrapper
#         result = func(*args, **kwargs)
#
#         print("2. Action AFTER calling the original function")
#         return result
#
#     return wrapper  # Returns the wrapper function object
#
#
# # Applying the decorator using @ syntax
# @my_decorator
# def greet(name):
#     print(f"Hello, {name}!")
# # Calling the decorated function
# greet("Alice")


# # Calling the decorated function
# greet("Alice")