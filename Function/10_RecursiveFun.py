n = int(input())

def facNum(num):
    if num == 0:
        return 1
    else:
        return (num * facNum(num - 1))

res = facNum(n)
print("factorial of n:", res)
    