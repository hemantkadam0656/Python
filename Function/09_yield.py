def evenNum(limit):
    for i in range(2,limit+1,2):
        yield i

for num in evenNum(10):
    print(num)
