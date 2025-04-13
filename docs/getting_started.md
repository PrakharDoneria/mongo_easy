# Getting Started with Mongo Easy

Welcome to **Mongo Easy**! This guide will help you quickly get up and running with Mongo Easy, a Python library designed to simplify working with MongoDB. Whether you're a beginner or a seasoned developer, this guide will help you connect to your MongoDB instance and start performing CRUD operations in no time.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Basic Usage](#basic-usage)
4. [Using the CLI](#using-the-cli)
5. [Additional Configuration](#additional-configuration)
6. [Next Steps](#next-steps)

---

## Prerequisites

Before you begin, make sure you have the following:

- **Python 3.6+**: Mongo Easy is built for Python 3.6 and higher. If you don’t have Python installed, you can download it from [python.org](https://www.python.org/downloads/).
  
- **MongoDB**: You need a running MongoDB instance. You can use a local instance or a remote database. To get MongoDB running locally, you can download it from [mongodb.com](https://www.mongodb.com/try/download/community) or use a cloud-based service like [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

- **Pip**: The `pip` package manager to install Mongo Easy.

---

## Installation

1. **Install Mongo Easy via pip**:

   Open your terminal and run the following command to install Mongo Easy from the Python Package Index (PyPI):

   ```bash
   pip install mongo-easy
   ```

2. **Install from Source (optional)**:

   If you'd like to contribute or work on the development version, you can clone the repository and install it locally:

   ```bash
   git clone https://github.com/yourusername/mongo_easy.git
   cd mongo_easy
   pip install -e .
   ```

3. **Install MongoDB (if not installed)**:

   If you don’t have MongoDB installed, follow the instructions on the [MongoDB installation page](https://www.mongodb.com/try/download/community) or use a cloud database like MongoDB Atlas.

---

## Basic Usage

Now that Mongo Easy is installed, you can begin using it to interact with MongoDB. Here’s a simple example of how to get started.

1. **Connect to MongoDB**:

   By default, Mongo Easy connects to a local MongoDB instance. You can change the connection settings in `config.py` if you want to connect to a remote database.

   ```python
   from mongo_easy.core.connection import connect

   connect()  # This connects to the MongoDB server
   ```

2. **Perform CRUD Operations**:

   Mongo Easy provides simple functions to perform basic CRUD (Create, Read, Update, Delete) operations.

   - **Create (Insert)**:

     Use the `save` function to insert a new document into a collection.

     ```python
     from mongo_easy.core.crud import save

     user_data = {"name": "Alice", "age": 30}
     save("users", user_data)
     ```

   - **Read (Find)**:

     Use the `find` function to query documents in a collection.

     ```python
     from mongo_easy.core.crud import find

     filter = {"age": {"$gte": 30}}
     users = find("users", filter)
     print(users)
     ```

   - **Update**:

     Use the `update` function to modify existing documents.

     ```python
     from mongo_easy.core.crud import update

     filter = {"name": "Alice"}
     update_query = {"$set": {"age": 31}}
     update("users", filter, update_query)
     ```

   - **Delete**:

     Use the `delete` function to remove documents from a collection.

     ```python
     from mongo_easy.core.crud import delete

     filter = {"name": "Alice"}
     delete("users", filter)
     ```

---

## Using the CLI

Mongo Easy also provides a **Command-Line Interface (CLI)** to perform database operations directly from the terminal.

1. **List Collections**:

   To list all collections in the current database:

   ```bash
   python -m mongo_easy.cli list
   ```

2. **Find Documents**:

   You can search for documents in a collection using the `find` command:

   ```bash
   python -m mongo_easy.cli find users --filter '{"age": {"$gte": 30}}'
   ```

3. **Insert Documents**:

   To insert documents from the command line:

   ```bash
   python -m mongo_easy.cli insert users --data '{"name": "Bob", "age": 25}'
   ```

For more commands, check the [CLI Guide](cli_guide.md).

---

## Additional Configuration

You can configure the MongoDB connection and other settings in the `config.py` file.

### MongoDB URI

The default URI connects to a local MongoDB instance. To change this, open `config.py` and modify the `MONGO_URI` setting:

```python
MONGO_URI = "mongodb://your_mongo_uri_here"
```

### Database Name

You can also change the default database that Mongo Easy connects to by modifying the `DEFAULT_DB` setting in `config.py`:

```python
DEFAULT_DB = "your_database_name"
```

---

## Next Steps

Now that you’ve installed and set up Mongo Easy, you can explore more advanced features:

1. **Explore the Functions Reference**: Learn about more functions and their usage by checking the [Functions Reference](functions_reference.md).

2. **Read the FAQ**: If you run into any issues or have questions, check out the [FAQ](faq.md) for solutions to common problems.

3. **Contribute**: If you'd like to contribute to Mongo Easy, check out the [Contributing Guide](contributing.md) for instructions on how to submit bug fixes and new features.

4. **Dive Deeper**: Check out the full documentation for advanced usage and configuration details.