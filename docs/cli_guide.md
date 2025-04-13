# CLI Guide for Mongo Easy

This guide provides you with detailed instructions on how to use the **Mongo Easy CLI** to interact with your MongoDB database directly from the command line.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Commands](#commands)
  - [list](#list)
  - [find](#find)
  - [insert](#insert)
  - [update](#update)
  - [delete](#delete)
  - [export-csv](#export-csv)
  - [import-csv](#import-csv)
  - [export-json](#export-json)
  - [import-json](#import-json)
  - [backup](#backup)
  - [restore](#restore)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

---

## Overview

Mongo Easy provides a simple and intuitive command-line interface (CLI) that lets you interact with your MongoDB database without writing Python code. You can perform basic operations such as **listing collections**, **finding documents**, **inserting new data**, **updating**, **deleting**, and more — all directly from the terminal.

---

## Requirements

Before using the Mongo Easy CLI, ensure that you have:

1. Python 3.x installed on your system.
2. Mongo Easy installed and set up in your project directory.
3. A MongoDB instance running locally or remotely.

---

## Commands

### `list`

**Description**: List all collections in the currently selected database.

```bash
python -m mongo_easy.cli list
```

### `find`

**Description**: Find documents in a specified collection. You can pass a filter in JSON format.

```bash
python -m mongo_easy.cli find <collection> --filter '{"age": {"$gte": 30}}'
```

**Options**:
- `<collection>`: The name of the collection you want to query.
- `--filter`: The filter query in JSON format to match specific documents.

Example:
```bash
python -m mongo_easy.cli find users --filter '{"age": {"$gte": 30}}'
```

### `insert`

**Description**: Insert a document into the specified collection.

```bash
python -m mongo_easy.cli insert <collection> --data '{"name": "Charlie", "age": 29}'
```

**Options**:
- `<collection>`: The name of the collection where the document will be inserted.
- `--data`: The document data to insert (in JSON format).

Example:
```bash
python -m mongo_easy.cli insert users --data '{"name": "Charlie", "age": 29}'
```

### `update`

**Description**: Update documents in a specified collection. You need to provide a filter and update query.

```bash
python -m mongo_easy.cli update <collection> --filter '{"name": "Charlie"}' --update '{"age": 30}'
```

**Options**:
- `<collection>`: The name of the collection where you want to perform the update.
- `--filter`: The filter to identify documents to update.
- `--update`: The update query in JSON format.

Example:
```bash
python -m mongo_easy.cli update users --filter '{"name": "Charlie"}' --update '{"age": 30}'
```

### `delete`

**Description**: Delete documents from a specified collection based on a filter.

```bash
python -m mongo_easy.cli delete <collection> --filter '{"name": "Charlie"}'
```

**Options**:
- `<collection>`: The name of the collection from which to delete documents.
- `--filter`: The filter to match documents to delete.

Example:
```bash
python -m mongo_easy.cli delete users --filter '{"name": "Charlie"}'
```

### `export-csv`

**Description**: Export the data from a collection to a CSV file.

```bash
python -m mongo_easy.cli export-csv <collection> <filepath>
```

**Options**:
- `<collection>`: The name of the collection to export.
- `<filepath>`: The path where the CSV file will be saved.

Example:
```bash
python -m mongo_easy.cli export-csv users users.csv
```

### `import-csv`

**Description**: Import data from a CSV file into a specified collection.

```bash
python -m mongo_easy.cli import-csv <collection> <filepath>
```

**Options**:
- `<collection>`: The name of the collection where the data will be imported.
- `<filepath>`: The path to the CSV file to import.

Example:
```bash
python -m mongo_easy.cli import-csv users users_data.csv
```

### `export-json`

**Description**: Export the data from a collection to a JSON file.

```bash
python -m mongo_easy.cli export-json <collection> <filepath>
```

**Options**:
- `<collection>`: The name of the collection to export.
- `<filepath>`: The path where the JSON file will be saved.

Example:
```bash
python -m mongo_easy.cli export-json users users.json
```

### `import-json`

**Description**: Import data from a JSON file into a specified collection.

```bash
python -m mongo_easy.cli import-json <collection> <filepath>
```

**Options**:
- `<collection>`: The name of the collection where the data will be imported.
- `<filepath>`: The path to the JSON file to import.

Example:
```bash
python -m mongo_easy.cli import-json users users_data.json
```

### `backup`

**Description**: Backup the entire database to a JSON file.

```bash
python -m mongo_easy.cli backup <filepath>
```

**Options**:
- `<filepath>`: The path where the backup file will be saved.

Example:
```bash
python -m mongo_easy.cli backup backup.json
```

### `restore`

**Description**: Restore the database from a backup file.

```bash
python -m mongo_easy.cli restore <filepath>
```

**Options**:
- `<filepath>`: The path to the backup file.

Example:
```bash
python -m mongo_easy.cli restore backup.json
```

---

## Examples

- **List collections**:
  ```bash
  python -m mongo_easy.cli list
  ```

- **Find users aged 30 and above**:
  ```bash
  python -m mongo_easy.cli find users --filter '{"age": {"$gte": 30}}'
  ```

- **Insert a new user**:
  ```bash
  python -m mongo_easy.cli insert users --data '{"name": "Charlie", "age": 29}'
  ```

- **Export users collection to CSV**:
  ```bash
  python -m mongo_easy.cli export-csv users users.csv
  ```

- **Backup the database**:
  ```bash
  python -m mongo_easy.cli backup backup.json
  ```

---

## Troubleshooting

- **MongoDB Connection Error**: Ensure MongoDB is running locally or remotely and that the URI is correctly set in the `config.py` file.
- **Invalid JSON**: Ensure that any filter or data passed in commands is properly formatted as valid JSON.
