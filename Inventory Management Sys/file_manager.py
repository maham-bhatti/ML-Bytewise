import csv
from food_item import FoodItem

class Inventory:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.food_item = FoodItem
        self.read_from_file()

    def read_from_file(self):
        
        try:
            with open(self.file_name, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    food_item = FoodItem(row[0], row[1], int(row[2]), row[3], row[4])
                    self.food_items.append(food_item)
        except FileNotFoundError:
            print(f"File {self.file_name} not found. Creating a new file.")
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Category", "Quantity", "Barcode", "Expiry Date"])

    def write_to_file(self):
        try:
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Category", "Quantity", "Barcode", "Expiry Date"])
                for food_item in self.food_items:
                    writer.writerow([food_item.name, food_item.category, food_item.quantity, food_item.barcode, food_item.expiry_date.strftime("%Y-%m-%d")])
        except IOError as e:
            print(f"Error writing to file: {e}")

    def add_food_item(self, food_item: FoodItem):
        self.food_item.append(food_item)
        self.write_to_file()

    def edit_food_item(self, barcode: str, **kwargs):
        
        for food_item in self.food_item:
            if food_item.barcode == barcode:
                for key, value in kwargs.items():
                    if hasattr(food_item, key):
                        setattr(food_item, key, value)
                self.write_to_file()
                return
        raise ValueError("Food item not found")

    def delete_food_item(self, barcode: str):
       
        self.food_items = [food_item for food_item in self.food_item if food_item.barcode!= barcode]
        self.write_to_file()

    #... other methods...