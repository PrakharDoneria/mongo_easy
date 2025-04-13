from mongo_easy.core.connection import connect, get_db
from mongo_easy.core.crud import save, find, update, delete

# Connect to MongoDB
connect()

# Define a collection
collection = "users"

# Insert a document
user_data = {"name": "Alice", "age": 30}
save(collection, user_data)
print("✔ Alice inserted!")

# Find a document
users = find(collection, {"name": "Alice"})
print("Found users:", users)

# Update a document
update(collection, {"name": "Alice"}, {"age": 31})
print("✔ Alice's age updated!")

# Delete a document
delete(collection, {"name": "Alice"})
print("✔ Alice deleted!")
