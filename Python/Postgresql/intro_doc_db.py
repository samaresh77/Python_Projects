# Database & PostgreSQL Fundamentals

# 1. What is a database?
# A database is a system for storing and managing data.

# ID    Name       Age
# 1     Samaresh   25
# 2     Rahul      24
# 3     Priya      22

# 2. What is PostgreSQL?
# PostgreSQL is a relational database management system (RDBMS).

# Database
#    ↓
# Tables
#    ↓
# Rows
#    ↓
# Columns

# 3. What is a table?
# A table is where related data is stored.

# | id | name     | age | email                                               |
# | -: | -------- | --: | --------------------------------------------------- |
# |  1 | Samaresh |  25 | [samaresh@example.com](mailto:samaresh@example.com) |
# |  2 | Rahul    |  24 | [rahul@example.com](mailto:rahul@example.com)       |
# |  3 | Priya    |  22 | [priya@example.com](mailto:priya@example.com)       |

# Row vs Column
# Column
# A column describes what type of information we're storing.

# id
# name
# age
# email
# Row

# A row represents one record.
# 1 | Samaresh | 25 | samaresh@example.com

# users
# ────────────────────────────────────
# id     name       age      email
# ────────────────────────────────────
# 1      Samaresh   25       ...
# 2      Rahul      24       ...
# 3      Priya      22       ...

# Primary Key

# This is extremely important.

# A primary key uniquely identifies each row.

# For our users:

# id
# We cannot have two users with the same primary-key ID.

# In SQL, we'd eventually have something conceptually like:

# id INTEGER PRIMARY KEY

# Foreign Key

# A foreign key connects one table to another.

# Suppose later we create:

# users

# and

# tasks

# A task could belong to a user:

# users
# ----------------
# id | name
# 1  | Samaresh
# 2  | Rahul

# tasks
# -------------------------
# id | title       | user_id
# 1  | Learn SQL   | 1
# 2  | Build API   | 1
# 3  | Learn React | 2

# Here:

# tasks.user_id

# references:

# users.id

# That's a foreign key.

# SQL

# PostgreSQL uses SQL (Structured Query Language).

# For example:

# Create table:

# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     age INTEGER
# );

# Insert
# INSERT INTO users (name, age)
# VALUES ('Samaresh', 25);

# Read
# SELECT * FROM users;

# Update
# UPDATE users
# SET age = 26
# WHERE id = 1;

# Delete
# DELETE FROM users
# WHERE id = 1;

# SQLAlchemy
# The architecture will become:

# FastAPI
#    ↓
# SQLAlchemy
#    ↓
# PostgreSQL

# You could write SQL directly inside FastAPI:

# cursor.execute(
#     "SELECT * FROM users"
# )

# SQLAlchemy is a Python SQL toolkit and ORM.

# ORM = Object Relational Mapper

# It allows us to work with database tables using Python objects/classes rather than writing SQL for every operation.

# For example, eventually we'll define something similar to:

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)

# Then Python/SQLAlchemy handles the database interaction.