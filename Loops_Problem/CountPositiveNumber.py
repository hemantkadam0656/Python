number = [1,3,4,6,2,-4,-6,2,3,-9,5,-7,4]

Positive_num_count = 0

for num in number:
    if num > 0:
        Positive_num_count += 1
    else:
        continue

print("POsitive number count is:", Positive_num_count)

