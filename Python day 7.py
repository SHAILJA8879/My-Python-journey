# 1. Creating a dictionary with initial key-value pairs
user_profile = {
    "username": "coder123",
    "age": 25,
    "is_active": True,
    "skills": ["Python", "SQL"]
}

# 2. Accessing a value using its key
print(user_profile["username"])    # Output: coder123

# 3. Adding a new key-value pair
user_profile["location"] = "New York"

# 4. Modifying an existing value
user_profile["age"] = 26

# 5. Removing a key-value pair
del user_profile["is_active"]

# Print the final dictionary
print(user_profile)
# Output: {'username': 'coder123', 'age': 26, 'skills': ['Python', 'SQL'], 'location': 'New York'}
