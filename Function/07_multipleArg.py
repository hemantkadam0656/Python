def fun(*arg):
    for i in arg:
        print(i)
    return max(arg)

# print(fun(1,2))
print(fun(1,2,3,4,5,6,7))