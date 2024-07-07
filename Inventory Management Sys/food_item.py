from datetime import datetime

class Fooditem:
    def __init__(self, name, category, quantity, barcode, expiry_date):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")

    def __return__(self):
        return f"Fooditem name: {self.name}, category: {self.category},quantity: {self.quantity}, barcode: {self.barcode}, expiry_date: {datetime.strptime(self.expiry_date, "%Y-%m-%d")}"


#from food_item import Fooditem
class Inventory:
    def __init__(self):
        self.items = []
    def addition(self, items):
        self.items.append(items)
    def edit_items(self, barcode, **kwargs):
        for item in self.food_items:
            if item.barcode == barcode:
                for key, value in kwargs.items():
                    setattr(item, key, value)
                return
        print("Item not found")
    def delete_item(self, barcode):
        for item in self.items:
            if item.barcode == barcode:
                self.items.remove(item)
                return
        print("Item not found")

    def search_item(self, **kwargs):
        result = self.items
        for item in self.items():
            if all(getattr(item, key) == value for key, value in kwargs.items()):
                result.append(item)
        return result
    def get_near_expiry(self, days = 7):
        near_expiry = []
        for item in self.items:
            if (item.expiry_date - datetime.now()).days <= days:
                near_expiry.append(item)
        return near_expiry

    