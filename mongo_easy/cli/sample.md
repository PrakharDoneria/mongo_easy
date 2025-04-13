# List collections
python -m mongo_easy.cli list

# Find documents
python -m mongo_easy.cli find users --filter '{"age": {"$gt": 25}}'

# Insert a user
python -m mongo_easy.cli insert users --data '{"name": "Charlie", "age": 29}'

# Import from CSV
python -m mongo_easy.cli import-csv users users.csv
