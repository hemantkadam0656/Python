username = "Hemant"

def fun():
    username = "Karan"
    print(username)

fun()
print(username)


x = 99

def func(y):
    z = x + y
    return z
res = func(1)

print(res)


def fun1():
    x = 88
    def fun2():
        print(x)    
    return fun2

res = fun1()
res()

def fun1(num):
    def func2(x):
        return x**num
    return func2

res = fun1(2)
print(res(3))
print(res(4))
