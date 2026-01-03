import json

def is_valid_item_name(name) -> bool:
    if type(name) == str and name.strip() != "":
        return True
    else:
        return False

def is_valid_qty(qty) -> bool:
    if type(qty) == int and qty >= 0:
        return True
    else:
        return False

def add_item(inv, name, qty) -> None:
    if is_valid_item_name(name) == False or is_valid_qty(qty) == False:
        print("Invalid input.")
    else:
        inv[f"{name}"] = qty
        print("Item added successfully.")

def update_item(inv, name, new_v) -> None:
    if is_valid_item_name(name) == False or is_valid_qty(new_v) == False:
        print("Invalid input.")
    elif name not in inv:
        print("Item not found.")
    else:
        inv[f"{name}"] = new_v
        print("Item updated successfully.")

def remove_item(inv, name) -> None:
    if name not in inv:
        print("Item not found.")
    else:
        del inv[f"{name}"]
        print("Item successfully deleted.")

def summarize(inv) -> None:
    items = len(inv)
    in_stock = 0
    out_of_stock = 0

    for key, value in inv.items():
        if value > 0:
            in_stock += 1
        else:
            out_of_stock += 1

    print(f"Items: {items}")
    print(f"In Stock: {in_stock}")
    print(f"Out Of Stock: {out_of_stock}")

def show_inv(inv) -> None:
    if len(inv) == 0:
        print("Inventory empty.")
        return

    for key, value in inv.items():
        print(f"{key}: {value}")

def save_inv(inv) -> None:
    with open("inventory.json", "w", encoding="utf-8") as f:
        json.dump(inv, f, indent=4)

def load_inv() -> dict:
    try:
        with open("inventory.json", "r", encoding="utf-8") as f:
            inv = json.load(f)
            return inv
    except:
        return {}

def spacer() -> None:
    print("\n\n")
