import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} function ran time is {end-start}")               
        return result
    return wrapper

@timer
def extrnal_func(n):
    time.sleep(n)

@timer
def sec_external_fun(m):
    time.sleep(m)


sec_external_fun(3)
extrnal_func(2)
