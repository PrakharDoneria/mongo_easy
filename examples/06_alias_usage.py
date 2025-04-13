from mongo_easy.aliasing.registry import get_alias

# Get the alias function for inserting a user
add_user = get_alias("add_user")

# Add a user
add_user({"name": "Bob", "age": 25})
print("✔ Bob added!")

# Now you can use the alias instead of the standard `save()` function
