
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.
 
    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_information():
    name = input("Please enter your name: ")
    order_number = input("Please enter your order number: ")
    address = input("Please enter your delivery address: ")
    return {
        "name": name,
        "order_number": order_number,
        "address": address
    }


def greet_user(name):
    print(f"Hello, {name}!")

def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()
