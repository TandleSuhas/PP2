my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_items = []

for item in my_list:
    if item % 2 != 0:
        odd_items.append(item)
print("Odd items from the list:", odd_items)
