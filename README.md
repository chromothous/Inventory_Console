# Inventory Console

A lightweight Python command-line application for managing inventory data, built with a focus on clarity, validation, and reliable state management.

---

## Overview

Inventory Console is a small but complete CLI tool that demonstrates:

- Modular design and separation of concerns  
- Defensive input validation  
- Persistent application state using JSON  
- Clear, readable control flow  

The project is intentionally scoped to remain simple, maintainable, and easy to reason about.

---

## Features

- Interactive command-line interface  
- Add, update, and remove inventory items  
- Validation for item names and quantities  
- Inventory summary reporting  
- Automatic persistence via JSON storage  

---

---

## Requirements

- Python 3.9 or newer  
- No third-party dependencies  

---

## Running the Application

From the project directory:

```bash```
python main.py

If inventory.json exists, the inventory is loaded automatically.
Otherwise, the application starts with an empty inventory.

## Example

1.) Add Item
2.) Update Item
3.) Remove Item
4.) Summary
5.) Show
6.) Help
7.) Exit

Please enter name of item to add:
potion

Please enter in the count of that item:
3

Item added successfully.

Show:
potion: 3

Summary:
Items: 1
In Stock: 1
Out Of Stock: 0


