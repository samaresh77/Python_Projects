# What is pip?
# pip is Python's package manager.
# It allows you to install external Python libraries/packages.

# python -m pip install fastapi

# | Python                | JavaScript               |
# | --------------------- | ------------------------ |
# | `pip`                 | `npm`                    |
# | `pip install fastapi` | `npm install express`    |
# | `requirements.txt`    | `package.json`           |
# | virtual environment   | `node_modules` isolation |

# Installing a package
# python -m pip install requests fastapi uvicorn

# Uninstalling a package
# python -m pip uninstall requests

# See installed packages
# python -m pip list

# Installing from requirements.txt
# python -m pip install -r requirements.txt

# What is requirements.txt?

# requirements.txt is primarily a list of packages required to run/install a project.

# Example:

# fastapi==0.116.1
# uvicorn==0.35.0
# pydantic==2.11.7

# python -m pip install -r requirements.txt

# What is pyproject.toml?

# pyproject.toml is a standard configuration file for Python projects.

# It can describe things such as:

# project name
# project version
# Python version requirement
# dependencies
# build configuration
# tooling configuration
# formatting/linting configuration

# Example:

# [project]
# name = "my-fastapi-app"
# version = "1.0.0"
# description = "My FastAPI backend"
# requires-python = ">=3.12"

# dependencies = [
#     "fastapi",
#     "uvicorn",
#     "pydantic"
# ]

# | Feature                     | requirements.txt | pyproject.toml |
# | --------------------------- | ---------------- | -------------- |
# | List dependencies           | ✅                | ✅              |
# | Pin exact versions          | ✅                | ✅              |
# | Project metadata            | ❌                | ✅              |
# | Python version requirement  | ❌/limited        | ✅              |
# | Build configuration         | ❌                | ✅              |
# | Tool configuration          | ❌                | ✅              |
# | Modern Python standard      | Common           | ✅              |
# | Simple projects             | Excellent        | Excellent      |
# | Large/professional projects | Common           | ✅ Very useful  |
