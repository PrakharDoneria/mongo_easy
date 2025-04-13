# Functions Reference for Mongo Easy

This document provides a detailed reference for all the functions available in the Mongo Easy library. Each function is categorized based on its purpose (CRUD operations, imports/exports, utilities, etc.) to make it easy for users to find the functionality they need.

## Table of Contents

- [CRUD Operations](#crud-operations)
  - [save()](#save)
  - [find()](#find)
  - [update()](#update)
  - [delete()](#delete)
- [Import/Export](#importexport)
  - [import_csv()](#import_csv)
  - [export_csv()](#export_csv)
  - [import_json()](#import_json)
  - [export_json()](#export_json)
- [Utilities](#utilities)
  - [get_db()](#get_db)
  - [connect()](#connect)
- [Alias System](#alias-system)
  - [get_alias()](#get_alias)
- [Backup/Restore](#backuprestore)
  - [backup_database()](#backup_database)
  - [restore_database()](#restore_database)

---

## CRUD Operations

### `save(collection, data)`

**Description**: Saves a new document to the specified collection in MongoDB.

**Parameters**:
- `collection` (str): The name of the collection where the document will be saved.
- `data` (dict): The document to insert. This should be a dictionary where the keys are the field names and the values are the corresponding data.

**Returns**: `None`

**Example**:
```python
from mongo_easy.core.crud import save

user_data = {"name": "Alice", "age": 30}
save("users", user_data)
```

---

### `find(collection, filter=None)`

**Description**: Finds documents in a specified collection that match the given filter. If no filter is provided, it will return all documents.

**Parameters**:
- `collection` (str): The name of the collection to search.
- `filter` (dict, optional): The filter query to apply (defaults to `None`). If no filter is provided, all documents are returned.

**Returns**: List of matching documents (each document is a dictionary).

**Example**:
```python
from mongo_easy.core.crud import find

filter = {"age": {"$gte": 30}}
users = find("users", filter)
print(users)
```

---

### `update(collection, filter, update)`

**Description**: Updates documents in a specified collection that match the filter. You provide the filter to identify the documents and the update query to modify them.

**Parameters**:
- `collection` (str): The name of the collection to update.
- `filter` (dict): The filter to identify the documents to update.
- `update` (dict): The update query to apply to the documents.

**Returns**: `None`

**Example**:
```python
from mongo_easy.core.crud import update

filter = {"name": "Alice"}
update_query = {"$set": {"age": 31}}
update("users", filter, update_query)
```

---

### `delete(collection, filter)`

**Description**: Deletes documents in a specified collection that match the given filter.

**Parameters**:
- `collection` (str): The name of the collection to delete from.
- `filter` (dict): The filter to identify the documents to delete.

**Returns**: `None`

**Example**:
```python
from mongo_easy.core.crud import delete

filter = {"name": "Alice"}
delete("users", filter)
```

---

## Import/Export

### `import_csv(collection, file_path)`

**Description**: Imports data from a CSV file into the specified collection.

**Parameters**:
- `collection` (str): The name of the collection to import data into.
- `file_path` (str): The path to the CSV file to import.

**Returns**: `None`

**Example**:
```python
from mongo_easy.io.csv_handler import import_csv

import_csv("users", "users_data.csv")
```

---

### `export_csv(collection, file_path)`

**Description**: Exports data from the specified collection into a CSV file.

**Parameters**:
- `collection` (str): The name of the collection to export data from.
- `file_path` (str): The path where the CSV file will be saved.

**Returns**: `None`

**Example**:
```python
from mongo_easy.io.csv_handler import export_csv

export_csv("users", "exported_users.csv")
```

---

### `import_json(collection, file_path)`

**Description**: Imports data from a JSON file into the specified collection.

**Parameters**:
- `collection` (str): The name of the collection to import data into.
- `file_path` (str): The path to the JSON file to import.

**Returns**: `None`

**Example**:
```python
from mongo_easy.io.json_handler import import_json

import_json("users", "users_data.json")
```

---

### `export_json(collection, file_path)`

**Description**: Exports data from the specified collection into a JSON file.

**Parameters**:
- `collection` (str): The name of the collection to export data from.
- `file_path` (str): The path where the JSON file will be saved.

**Returns**: `None`

**Example**:
```python
from mongo_easy.io.json_handler import export_json

export_json("users", "exported_users.json")
```

---

## Utilities

### `get_db()`

**Description**: Returns the current database object that is connected to MongoDB.

**Parameters**: None

**Returns**: The database object.

**Example**:
```python
from mongo_easy.core.connection import get_db

db = get_db()
print(db.name)  # Print the name of the current database
```

---

### `connect()`

**Description**: Establishes a connection to the MongoDB instance using the configuration in `config.py`.

**Parameters**: None

**Returns**: `None`

**Example**:
```python
from mongo_easy.core.connection import connect

connect()
```

---

## Alias System

### `get_alias(alias_name)`

**Description**: Retrieves the alias function for a specified alias name. Aliases are custom functions that simplify common operations (e.g., inserting a user).

**Parameters**:
- `alias_name` (str): The name of the alias function to retrieve.

**Returns**: The function corresponding to the alias.

**Example**:
```python
from mongo_easy.aliasing.registry import get_alias

# Retrieve the alias for adding a user
add_user = get_alias("add_user")

# Use the alias function
add_user({"name": "Bob", "age": 25})
```

---

## Backup/Restore

### `backup_database(file_path)`

**Description**: Creates a backup of the entire database and saves it to a file.

**Parameters**:
- `file_path` (str): The path where the backup file will be saved.

**Returns**: `None`

**Example**:
```python
from mongo_easy.io.backup import backup_database

backup_database("backup.json")
```

---

### `restore_database(file_path)`

**Description**: Restores the database from a backup file.

**Parameters**:
- `file_path` (str): The path to the backup file.

**Returns**: `None`

**Example**:
```python
from mongo_easy.io.backup import restore_database

restore_database("backup.json")
```