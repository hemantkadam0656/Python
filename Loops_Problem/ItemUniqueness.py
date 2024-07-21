fruits = ["apple", "orange", "apple", "banana", "kiwi"]

unique_item = set()

for item in fruits:
    if item in unique_item:
        print("duplicate Item", item)
        break
    unique_item.add(item)
