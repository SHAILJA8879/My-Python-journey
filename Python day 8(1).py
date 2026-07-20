# 1. Arithmetic Operations
a = 10
b = 3

print("--- Arithmetic Operations ---")
print("Addition (10 + 3):", a + b)
print("Subtraction (10 - 3):", a - b)
print("Multiplication (10 * 3):", a * b)
print("Division (10 / 3):", a / b)            # Returns float
print("Floor Division (10 // 3):", a // b)      # Returns rounded down whole number
print("Modulus / Remainder (10 % 3):", a % b)
print("Exponentiation (10 ** 3):", a ** b)    # 10^3


# 2. Tuples (Immutable sequences)
# Tuples are like lists, but once created, their elements cannot be changed.
my_tuple = (1, 2, "apple", 3.14, 2)

print("\n--- Tuple Operations ---")
print("Full Tuple:", my_tuple)
print("Access 3rd element:", my_tuple[2])       # Index starts at 0
print("Count how many times '2' appears:", my_tuple.count(2))
print("Find index of 'apple':", my_tuple.index("apple"))

# Tuples are immutable, so this would throw an error:
# my_tuple[0] = 10 


# 3. Other Core Concepts
print("\n--- Lists (Mutable) ---")
my_list = [10, 20, 30]
my_list.append(40) # Add an item
print("Modified List:", my_list)

print("\n--- Dictionaries (Key-Value pairs) ---")
my_dict = {"name": "Alice", "age": 25}
print("Dictionary:", my_dict)
print("Age:", my_dict["age"])

print("\n--- Control Flow ---")
if a > b:
    print(f"Condition Check: {a} is greater than {b}")
else:
    print(f"{a} is not greater than {b}")
