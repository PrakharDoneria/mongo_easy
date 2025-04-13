from mongo_easy.io.csv_handler import import_csv, export_csv

# Import data from CSV
import_csv("users", "users_data.csv")
print("✔ Imported users data from CSV")

# Export data to CSV
export_csv("users", "exported_users.csv")
print("✔ Exported users data to CSV")
