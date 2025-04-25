
# default parameter 
# default parameter iska use tab karte he jab agar agrument nahi di to ye use karega

def func(fname,lname="Rehman"):
    print(fname,lname)
    
func("muneeb","ur rehman")


# *args
# iska use parameter me karte he aur iska use isliye karte he agar argument ek se zada ho to vo sab *args me ajayenge ye unlimitted argument leta he

#  **kwargs
# iska use bhi parameter me karte he aur iska use isliye karte he agar argument key value me ho to vo sab isme ajayenge 


# decorator in deep 

# basically kisi function ke uper agar decorator lagate he to jab function call hota he to phele decorator wala chalta he fir vo function chalta he
# ye ek toll ki tarah kaam karta he phele toll me jane ke baad hi function call hoga



# ques1 calculate time of function execute.Write a decorator that measures the time a function takes to execute

import time

def timer(fun):
    def wrapper(*args):         # ye function call chalta he isse example_function(2)
        start=time.time()
        result=fun(*args)
        end=time.time()
        print(f"{fun.__name__} takes time {end-start} to exucute")
        return result
    return wrapper              # is function ko return hi padta hi nahi to nahi chalta 



@timer
def example_function(*args,**kwargs):    # ye function decorator ke parameter me chale jata he fir usse call hota he
    time.sleep(args[0])





# example_function(2)



# ques2 debugging function calls.Create a decorator to print the function name and the values of the argument

def debug(fun):
    def wrapper(*args,**kwargs):
        args_value=",".join(arg  for arg in args)
        kwargs_value=",".join(f"{kwarg}={v}" for kwarg,v in kwargs.items() )
        print(f"calling {fun.__name__} with args {args_value} and {kwargs_value}")
        return fun(*args,**kwargs)
    return wrapper


@debug
def hello():
    print("hello")


@debug
def greet(name,greeting="hello"):
    print(f"{greeting},{name}")


greet("muneeb","hellow")


hello()






#  ques3 cache return values.Implement a decorator that caches the return values of a function so that when its called
#    with the same argument,the cached value is returned instead of re-executing the function





# def cache(fun):
#     cache_value={}                     # ye ek baar chalne ke baad fir nahi chalta
#     name="muneeb ur rehman"
#     print(name)
#     print(cache_value)
#     def wrapper(*args):
#         result=fun(*args)
#         cache_value[args]=result
#         print(cache_value)
#         print("muneeb")
#         return result
#     return wrapper
        








# @cache
# def long_running_funtion(a,b):
#     time.sleep(4)
#     return a+b




# print(long_running_funtion(2,2))
# print(long_running_funtion(3,4))
# print(long_running_funtion(5,6))
# print(long_running_funtion(2,2))




