from mongo_easy.io.backup import backup_database, restore_database

# Backup the database to a file
backup_database("backup.json")
print("✔ Database backed up!")

# Restore the database from the backup file
restore_database("backup.json")
print("✔ Database restored!")
