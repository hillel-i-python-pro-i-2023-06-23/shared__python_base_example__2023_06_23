# You can access to item by index.
#   They numerated from zero (0).
#   Because this as "offset from start".

fruits = ["Kiwi", "Apple", "Lemon", "Pineapple"]
print(fruits)

# Get item by index:
item_by_index_from_zero = fruits[0]
print(fruits)
print(f"{item_by_index_from_zero=}")

item_by_index = fruits[2]
print(fruits)
print(f"{item_by_index=}")

# Add item by index.
fruits.insert(2, "Blueberry")
print(fruits)

# Add item by index.
fruits[2] = "Coconut"
print(fruits)

# Get and delete from list last by index
popped_by_index = fruits.pop(2)
print(fruits)
print(f"{popped_by_index=}")

sublist = fruits[1:3]
print(f"{sublist=}")

item_by_negative_index = fruits[-1]
print(f"{item_by_negative_index=}")
