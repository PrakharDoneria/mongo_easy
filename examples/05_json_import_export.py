from mongo_easy.io.json_handler import import_json, export_json

# Import data from JSON
import_json("users", "users_data.json")
print("✔ Imported users data from JSON")

# Export data to JSON
export_json("users", "exported_users.json")
print("✔ Exported users data to JSON")
