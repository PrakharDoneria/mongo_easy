# Mongo Easy FAQ

This document answers the most common questions about using **Mongo Easy**. If you're encountering issues or want to learn more about specific functionality, this guide is a great place to start.

## Table of Contents

- [General Questions](#general-questions)
- [Installation Issues](#installation-issues)
- [Usage](#usage)
  - [How do I connect to MongoDB?](#how-do-i-connect-to-mongodb)
  - [How do I perform CRUD operations?](#how-do-i-perform-crud-operations)
  - [How do I use the CLI?](#how-do-i-use-the-cli)
- [Troubleshooting](#troubleshooting)
  - [Why is my MongoDB not connecting?](#why-is-my-mongodb-not-connecting)
  - [Why are some commands not working?](#why-are-some-commands-not-working)
  - [How do I reset my database?](#how-do-i-reset-my-database)
- [Advanced Questions](#advanced-questions)
  - [How can I configure the database connection?](#how-can-i-configure-the-database-connection)
  - [How do I add custom aliases?](#how-do-i-add-custom-aliases)
- [Contributing](#contributing)

---

## General Questions

### What is Mongo Easy?

**Mongo Easy** is a simple Python library that simplifies working with MongoDB. It provides straightforward functions for performing CRUD operations, as well as utility functions to work with databases and collections without requiring deep knowledge of MongoDB's internal workings. The goal is to make MongoDB accessible to everyone, even those without coding experience.

### Is Mongo Easy open source?

Yes! Mongo Easy is an open-source project, and we encourage contributions. Feel free to fork the repository and submit pull requests.

---

## Installation Issues

### How do I install Mongo Easy?

To install **Mongo Easy**, you can use `pip`:

```bash
pip install mongo-easy
```

Alternatively, if you're developing or contributing to the project, you can clone the repository and install it locally:

```bash
git clone https://github.com/yourusername/mongo_easy.git
cd mongo_easy
pip install -e .
```

---

## Usage

### How do I connect to MongoDB?

Mongo Easy automatically connects to a local MongoDB instance by default. You can change the connection URI in `config.py`:

```python
MONGO_URI = "mongodb://localhost:27017"
```

For remote connections, update the URI with the appropriate credentials:

```python
MONGO_URI = "mongodb://username:password@remote_host:27017"
```

You can also set environment variables to configure the URI:

```bash
export MONGO_URI="mongodb://your_uri_here"
```

### How do I perform CRUD operations?

Mongo Easy simplifies CRUD operations using easy-to-use functions. Here’s how you can use them:

1. **Save a document**:

```python
from mongo_easy.core.crud import save

data = {"name": "Alice", "age": 30}
save("users", data)
```

2. **Find documents**:

```python
from mongo_easy.core.crud import find

users = find("users", {"age": {"$gte": 30}})
print(users)
```

3. **Update documents**:

```python
from mongo_easy.core.crud import update

update("users", {"name": "Alice"}, {"$set": {"age": 31}})
```

4. **Delete documents**:

```python
from mongo_easy.core.crud import delete

delete("users", {"name": "Alice"})
```

---

### How do I use the CLI?

Mongo Easy provides a powerful CLI to perform database operations directly from the terminal. Here are some common commands:

1. **List collections**:

```bash
python -m mongo_easy.cli list
```

2. **Find documents**:

```bash
python -m mongo_easy.cli find users --filter '{"age": {"$gte": 30}}'
```

3. **Insert documents**:

```bash
python -m mongo_easy.cli insert users --data '{"name": "Charlie", "age": 25}'
```

For more information on the CLI commands, check out the [CLI Guide](cli_guide.md).

---

## Troubleshooting

### Why is my MongoDB not connecting?

If you're having trouble connecting to MongoDB, consider the following:

1. **MongoDB is not running**: Make sure your MongoDB server is up and running. If you're using a local MongoDB instance, you can start it by running `mongod` in your terminal.

2. **Incorrect URI**: Double-check your `MONGO_URI` in `config.py` to ensure it’s correct. For remote databases, make sure your username, password, and host are correct.

3. **Firewall/Network issues**: If you're connecting remotely, ensure that your firewall allows connections on port 27017 (the default MongoDB port).

---

### Why are some commands not working?

1. **Missing arguments**: Make sure you’re passing all required arguments to the commands (e.g., `--filter`, `--data`).

2. **Database not selected**: Ensure that you’ve selected a database before running commands. If you don't specify a database, Mongo Easy defaults to `"test"`.

3. **Improper syntax**: Ensure that JSON filters and data are formatted correctly. For instance, make sure quotes are used properly in the filter arguments.

---

### How do I reset my database?

To reset your database, you can use the following:

```bash
python -m mongo_easy.cli drop-all
```

This will drop all collections from the database. Be careful as this action is irreversible.

---

## Advanced Questions

### How can I configure the database connection?

You can configure the database connection by updating the values in the `config.py` file:

```python
MONGO_URI = "mongodb://your_mongo_uri_here"
DEFAULT_DB = "your_default_db"
```

Alternatively, you can set environment variables for these configurations.

### How do I add custom aliases?

To add a custom alias, you can modify the alias registry in `mongo_easy/aliasing/registry.py`. Add a new function or alias mapping as follows:

```python
# Add a new alias for adding users
from mongo_easy.core.crud import save

def add_user(data):
    save("users", data)
```

This allows you to use `add_user()` as a shorthand for `save()` when inserting user documents.

---

## Contributing

If you'd like to contribute to Mongo Easy, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your fork locally and create a new branch.
3. Make your changes and add tests where applicable.
4. Push your changes and create a pull request.

We welcome contributions and suggestions for improving the project!
