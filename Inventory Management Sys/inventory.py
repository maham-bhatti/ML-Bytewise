import csv
from datetime import date, timedelta
from food_item import FoodItem  # Assuming FoodItem class is defined in food_item.py

class Inventory:
    def __init__(self):
        self.items = []

    def add_food_item(self, food_item):
        self.items.append(food_item)

    def edit_food_item(self, barcode, name=None, category=None, quantity=None, expiry_date=None):
        for item in self.items:
            if item.barcode == barcode:
                if name:
                    item.name = name
                if category:
                    item.category = category
                if quantity is not None:
                    item.quantity = quantity
                if expiry_date:
                    item.expiry_date = expiry_date
                return True
        return False

    def delete_food_item(self, barcode):
        for item in self.items:
            if item.barcode == barcode:
                self.items.remove(item)
                return True
        return False

    def search_food_item(self, name=None, barcode=None):
        results = []
        for item in self.items:
            if name and item.name == name:
                results.append(item)
            elif barcode and item.barcode == barcode:
                results.append(item)
        return results

    def handle_near_expiry_items(self, days=7):
        near_expiry_items = []
        today = date.today()
        for item in self.items:
            if item.expiry_date <= today + timedelta(days=days):
                near_expiry_items.append(item)
        return near_expiry_items

    def display_items(self):
        for item in self.items:
            print(item)

    def write_to_csv(self, filename):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Category', 'Quantity', 'Barcode', 'Expiry Date'])
                for item in self.items:
                    writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date])
            print(f"Inventory data successfully written to {filename}")
        except IOError as e:
            print(f"Error writing to {filename}: {e}")

    def read_from_csv(self, filename):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    name, category, quantity, barcode, expiry_date = row
                    quantity = int(quantity)  # Convert quantity from string to int
                    expiry_date = date.fromisoformat(expiry_date)  # Convert expiry_date from ISO format to date object
                    item = FoodItem(name, category, quantity, barcode, expiry_date)
                    self.items.append(item)
            print(f"Inventory data successfully read from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error reading from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Add some sample items
    item1 = FoodItem("Apple", "Fruit", 10, "123456789", date(2024, 8, 1))
    item2 = FoodItem("Milk", "Dairy", 5, "987654321", date(2024, 7, 10))
    inventory.add_food_item(item1)
    inventory.add_food_item(item2)
    
    # Write inventory data to CSV
    inventory.write_to_csv("inventory.csv")
    
    # Clear current items (for demonstration)
    inventory.items = []
    
    # Read inventory data from CSV
    inventory.read_from_csv("inventory.csv")
    
    # Display items after reading from CSV
    print("\nItems after reading from CSV:")
    inventory.display_items()
