import inventory

inv = inventory.load_inv()

menu_input = ""

while menu_input != "7":
    menu_input = input("1.) Add Item\n2.) Update Item\n3.) Remove Item\n4.) Summary\n5.) Show\n6.) Help\n7.) Exit\n\n")

    inventory.spacer()

    if menu_input == "1":
        new_item = input("Please enter name of item to add.\n\n")

        inventory.spacer()

        try:
            new_count = int(input("Please enter in the count of that item.\n\n"))
        except:
            new_count = "Invalid."

            inventory.spacer()

        if inventory.is_valid_item_name(new_item) == True and inventory.is_valid_qty(new_count) == True:
            inventory.add_item(inv, new_item, new_count)
            inventory.save_inv(inv)

            inventory.spacer()
    
    elif menu_input == "2":
        new_item = input("Please enter name of item to update.\n\n")

        try:
            new_count = int(input("Please enter in the count of that item to replace the old one.\n\n"))
        except:
            new_count = "Invalid."

            inventory.spacer()

        if inventory.is_valid_item_name(new_item) == True and inventory.is_valid_qty(new_count) == True:
            inventory.update_item(inv, new_item, new_count)
            inventory.save_inv(inv)
            
            inventory.spacer()

    elif menu_input == "3":
        item_to_remove = input("Please enter item to be removed.\n\n")

        inventory.spacer()

        if inventory.is_valid_item_name(item_to_remove) == True:
            inventory.remove_item(inv, item_to_remove)
            inventory.save_inv(inv)
            
            inventory.spacer()

    elif menu_input == "4":
        inventory.summarize(inv)

        inventory.spacer()

    elif menu_input == "5":
        inventory.show_inv(inv)

        inventory.spacer()

    elif menu_input == "6":
        print("To choose a selection, only put in the number.\n\n")

    elif menu_input == "7":
        print("Thank you for using my app. Take care. If you have any questions please email nrda1991@gmail.com.")

    else:
        print("Unknown command.\n\n")
