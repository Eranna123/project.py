

class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        new_food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(new_food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                break

    def view_all_food_items(self):
        return self.food_items

    def remove_food_item(self, food_id):
        self.food_items = [item for item in self.food_items if item.food_id != food_id]

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_new_order(self, food_items):
        order = []
        for food_id in food_items:
            food_item = self.find_food_item_by_id(food_id)
            if food_item:
                order.append(food_item)
        self.order_history.append(order)

    def find_food_item_by_id(self, food_id):
        for food_item in admin.food_items:
            if food_item.food_id == food_id:
                return food_item
        return None

    def view_order_history(self):
        return self.order_history

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

admin = Admin()
admin.add_food_item("Tandoori roti", "4 pieces", 210, 0, 100)
admin.add_food_item(" Burger", "2 Piece", 120, 0, 80)
admin.add_food_item(" Butter bread", "500gm", 900, 0, 20)

admin.edit_food_item(2, " Burger", "1 Piece", 350, 0, 30)
admin.remove_food_item(1)

user1 = User("Aruna", "9876345256", "aru@example.com", "43, ABC palya", "secretpassword")
print("old user details:",user1.full_name ,user1.phone_number  ,user1.email  ,user1.address)
user1.place_new_order([2, 3])
user1.update_profile("eranna", "8765222109", "kiranaa@mail.com", "111, king Colony", "newpassword")
print("user details:" ,user1.full_name  ,user1.phone_number  ,user1.email  ,user1.address)

print("\nFood Items:")
for item in admin.view_all_food_items():
    print(f"{item.name} ({item.quantity}) [INR {item.price}]")

print("\nUser Order History:")
for order in user1.view_order_history():
    print(", ".join([item.name for item in order]))





















menu = {
    'Pizza': {'Regular': 11.50, 'Large': 15.99},
    'Burger': {'Cheeseburger':12.99 , 'Chicken Burger': 8.00},
    'Biryani': {'Chicken': 20.00, 'Veg': 15.99},
    'Noodles': {'Chicken': 12.99,'veg':10.00, 'Egg': 11.99}
}

def display_menu():
    print("Menu:")
    for item, varieties in menu.items():
        print(f"{item}:")
        for variety, price in varieties.items():
            print(f"   {variety}: ${price}")

def place_order():
    display_menu()
    order = {}
    while True:
        item = input("Enter the item name (or 'done' to finish): ")
        if item == 'done':
            break

        if item not in menu:
            print("Invalid item!")
            continue

        variety = input("Enter the variety: ")
        if variety not in menu[item]:
            print("Invalid variety!")
            continue

        quantity = int(input("Enter the quantity: "))
        if item not in order:
            order[item] = {}
        order[item][variety] = quantity

    return order

def calculate_total(order):
    total = 0
    for item, varieties in order.items():
        for variety, quantity in varieties.items():
            total += menu[item][variety] * quantity
    return total

def main():
    order = place_order()
    total = calculate_total(order)
    print(f"Your order: {order}")
    print(f"Total amount: ${total}")

if __name__ == '_main_':
 main()