# NeilMart, Python game
# Written by Neil Fink, 2021

# Generate grocery store
def make_store():
    store = [[], [], []]
    return store


# Generate items
def make_items():
    items = [["Cola", "Popcorn", "Chips", "Chocolate", "Gummy Bears", "Ginger Ale"],
             ["Soup", "Crackers", "Ramen Noodles", "Spaghetti", "Tomato Sauce", "Tuna"],
             ["Diapers", "Toilet Paper", "Dish Soap", "Sanitizer", "Bleach"]]
    return items


def get_input(message, datatype):
    user_input = 0
    while user_input == 0:
        try:
            user_input = datatype(input(message))
        except ValueError:
            print("Not valid!")
    return user_input


def play_game1():
    # Game 1
    turn = 1
    rating = 5
    money = 0
    store = make_store()
    backroom = []
    capacity = 3

    print("Here are the rules for Game #1:\n"
          "You get a series of items delivered to you by the driver each turn.\n"
          "You must put all items to the shelf first, so that way customers can buy from your store!\n"
          "Items will only sell if they are placed next to each other!\n"
          "If items cannot sell, they can be placed in the backroom!\n"
          "Remember, your rating will go down every turn that you don't sell any items!\n")
    print(get_input("Input an int: ", int))


# Main method
print("\nWelcome to NeilMart!")
play_game1()
