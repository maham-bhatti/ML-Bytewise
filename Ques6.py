def update_inventory(invent_dict, item, quantity):
    if item in invent_dict:
        invent_dict[item] = max(0, invent_dict[item] + quantity)
    else:
        if quantity > 0:
            invent_dict[item] = quantity
        else:
            invent_dict[item] = 0
    return invent_dict

inventory = {
    'bread': 10,
    'eggs': 23,
    'oranges': 16,
    'grapes': 15,
    'papaya': 13,
}

print("Initial inventory:", inventory)

for _ in range(3):
    item = input("Enter the item name to update: ")
    quantity = int(input("Enter the quantity to add/remove for" + item + "use negative values for removal: "))
    inventory = update_inventory(inventory, item, quantity)

print("\nUpdated inventory:", inventory)
