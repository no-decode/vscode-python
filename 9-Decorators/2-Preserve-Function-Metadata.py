import time
from functools import wraps
def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,end-start)
        return result
    return wrapper
@timethis
def countdown(n:int):
    while n > 0:
        n-=1
# countdown(1000000)
countdown.__name__


    