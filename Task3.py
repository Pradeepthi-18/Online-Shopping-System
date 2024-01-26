class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_product(self, product, quantity):
        if product in self.items:
            self.items[product] -= quantity
            if self.items[product] <= 0:
                del self.items[product]

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.order_history = []

    def add_to_order_history(self, order):
        self.order_history.append(order)

    def login(self, username, password):
        return self.username == username and self.password == password

if __name__ == "__main__":
    # Create some sample products
    laptop = Product("Laptop", 1000, 10)
    phone = Product("Phone", 500, 20)
    earphones = Product("Earphones", 250, 5)

    while True:
        # Display available products and stock
        print("Available Products:")
        print(f"1. {laptop.name} - ${laptop.price} (Stock: {laptop.stock_quantity})")
        print(f"2. {phone.name} - ${phone.price} (Stock: {phone.stock_quantity})")
        print(f"3. {earphones.name} - ${earphones.price} (Stock: {earphones.stock_quantity})")

        num_users = int(input("Enter the number of users (0 to exit): "))
        if num_users == 0:
            print("Exiting the program...")
            break

        # Shopping process for each user
        for _ in range(num_users):
            print("\nUser:")
            # Create a shopping cart for each user
            cart = ShoppingCart()

            # Add products to the cart
            while True:
                choice = input("Enter product choice you want to purchase (1, 2, 3): ")
                if choice not in ["1", "2", "3"]:
                    print("Invalid choice. Please select a valid product.")
                    continue

                product = None
                if choice == "1":
                    product = laptop
                elif choice == "2":
                    product = phone
                elif choice == "3":
                    product = earphones

                if product:
                    quantity = int(input("Enter quantity: "))
                    if quantity > product.stock_quantity:
                        print("Sorry, the quantity you requested exceeds the available stock.")
                    else:
                        cart.add_product(product, quantity)
                        product.stock_quantity -= quantity  # Update stock quantity
                    break  # Exit the loop if the choice is valid

            # Remove products from the cart
            remove_choice = input("Do you want to remove any product? (yes/no): ")
            if remove_choice.lower() == "yes":
                remove_product = input("Enter product name to remove: ")
                remove_quantity = int(input("Enter quantity to remove: "))
                if remove_product.lower() == "laptop":
                    cart.remove_product(laptop, remove_quantity)
                    laptop.stock_quantity += remove_quantity  # Restore stock quantity
                elif remove_product.lower() == "phone":
                    cart.remove_product(phone, remove_quantity)
                    phone.stock_quantity += remove_quantity  # Restore stock quantity
                elif remove_product.lower() == "earphones":
                    cart.remove_product(earphones, remove_quantity)
                    earphones.stock_quantity += remove_quantity  # Restore stock quantity

            # Create a user and login
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            logged_in = user.login(username, password)
            if logged_in:
                print(f"{username} is logged in successfully!")
            else:
                print("Invalid username or password.")

            # Add order to user's order history
            user.add_to_order_history(cart.items)

            # Print user's order history
            print(f"{username}'s Order History:")
            for order in user.order_history:
                for product, quantity in order.items():
                    print(f"Product: {product.name}, Quantity: {quantity}")
