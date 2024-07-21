n = int(input("Enter your n'th number :"))
sum = 0

for num in range(n + 1):
    if (num % 2 == 0):
        sum += num
    else:
        continue

print("Sum of even numbers is",sum)
