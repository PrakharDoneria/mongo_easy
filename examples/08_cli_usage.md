# List all collections
python -m mongo_easy.cli list

# Find users aged 30 and above
python -m mongo_easy.cli find users --filter '{"age": {"$gte": 30}}'

# Insert a new user
python -m mongo_easy.cli insert users --data '{"name": "Charlie", "age": 29}'

# Export users collection to CSV
python -m mongo_easy.cli export-csv users users.csv
