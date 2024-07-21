import time

def catche(func):
    catche_value = {}        
    def wrapper(*args):        
        if args in catche_value:
            return catche_value[args]
        result= func(*args)
        catche_value[args] = result
        return result
    return wrapper

@catche
def sumoftwonum(a, b):
    time.sleep(4)
    return a + b 

print(sumoftwonum(3,4))
print(sumoftwonum(3,4))
