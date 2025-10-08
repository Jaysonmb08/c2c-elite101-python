def get_user_information():
    name = input("Please enter your name: ")
    order_number = input("Please enter your order number: ")
    address = input("Please enter your delivery address: ")
    return {
        "name": name,
        "order_number": order_number,
        "address": address
    }

def greet_user(user_info):
    print(f"\nHello, {user_info['name']}!")
    print(f"Thanks for providing your order #{user_info['order_number']} for delivery to {user_info['address']}.")

def track_order_status(order_number):
    print(f"\nChecking status for order #{order_number}...")
    print("Your order is currently out for delivery and should arrive soon!")

def main():
    user_info = get_user_information()
    greet_user(user_info)
    track_order_status(user_info["order_number"])

if __name__ == "__main__":
    main()
