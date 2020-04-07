hotels = {
    "Hotel California": {
    "101": {},
    "102": {},
    "103": {},
    "104": {},
    "105": {},
}, "Hotel Atlanta": {
    "101": {},
    "102": {},
    "103": {},
    "104": {},
    "105": {},
}, "Hotel Trivago": {
    "101": {},
    "102": {},
    "103": {},
    "104": {},
    "105": {},
}
}

list_of_hotels = [hotels]
main_menu = '''

1. Print hotel room status
2. Check in customer
3. Check out customer
4. Manage hotels
5. Quit

'''

manage_hotels = '''

1. Print hotel list
2. Add a new hotel
3. Close an existing hotel
4. Quit

'''

# Dwayne = {
#     "occupant_name": "Dwayne",
#     "phone_number": "111-111-1111",
#     "prepaid": True
# }

# Darrell = {
#     "occupant_name": "Darrell",
#     "phone_number": "222-222-2222",
#     "prepaid": False
# }

# Dwight = {
#     "occupant_name": "Dwight",
#     "phone_number": "333-333-3333",
#     "prepaid": True
# }

# Dilly_Dilly = {
#     "occupant_name": "Dilly Dilly",
#     "phone_number": "444-444-4444",
#     "prepaid": False
# }

Delilah = {
    "occupant_name": "Delilah",
    "phone_number": "555-555-5555",
    "prepaid": True
}

# function to check if a room is occupied
def is_vacant(room):
    if hotel[room] == {}:
        print(f"{room} is empty.")
    else:
        print(f'{room} is occupied by {hotel[room]["occupant_name"]}.')

# function to assign a person to a room
def check_in(hotel, room, name):
    if list_of_hotels[hotels][room] == {}:
        list_of_hotels[hotels][room] = name
    else:
        print(f'{room} is occupied!')
check_in(0, "105", Delilah)
check_in(1, "103", Dilly_Dilly)

# function to check a person out of the room and return the person dictionary
def check_out(hotel, room):
    if hotels[hotel][room]["prepaid"] == True:
        print("They're paid up! Check 'em out.")
        if hotels[hotel][room] != {}:
            guest_info = hotels[hotel][room]
            hotels[hotel][room] = {}
            # print(guest_info)
            return guest_info
        else:
            print(f"{room} is empty.")
    else:
        print("They owe us money! Hold them hostage forever.")

# function to create a new customer
def new_customer():
    name = input("What's the customer's name? ")
    phone_number = input("What's the customer's phone number? ")
    prepay = input("Will the customer be pre-paying? True or False ")
    if prepay == "True":
        prepay = True
    elif prepay == "False":
        prepay = False
    name = {
        "name": name,
        "phone number": phone_number,
        "prepaid": prepay
    }
    return name

while True:
    menu_choice = int(input(main_menu))
    # Add if/else statements for each menu item
    if menu_choice == 1:
        for hotel in hotels:
            print(hotel)
    elif menu_choice == 2:
        hotel_name = input("What hotel? ")
        if hotel_name == "Hotel California":
            hotel_name = 0
        elif hotel_name == "Hotel Atlanta":
            hotel_name = 1
        elif hotel_name == "Hotel Trivago":
            hotel_name = 2
        else:
            print("No such hotel - sorry!")
            break
        room = input("What room? ")
        if hotels[hotel_name][room] == {}:
            name = new_customer()
            check_in(hotel_name, room, name)
            print(hotels)
        else:
            print("Room is full!  Pick another one")
    elif menu_choice == 3:
        hotel_name = input("What hotel are you checking out of? ")
        if hotel_name == "Hotel California":
            hotel_name = 0
        elif hotel_name == "Hotel Atlanta":
            hotel_name = 1
        elif hotel_name == "Hotel Trivago":
            hotel_name = 2
        else:
            print("No such hotel - sorry!")
        room = input("What room are you checking out of? ")
        check_out(hotel_name, room)
    elif menu_choice == 4:
        menu_choice = int(input(manage_hotels))
        if menu_choice == 1:
            print(hotels)
        elif menu_choice == 2:
            hotel_name = input("What's the name of the new establishment? ")
            hotels.append(hotel_name)
        elif menu_choice == 3:
            hotel_name = input("Which hotel are we closing? ")
            del hotels[hotel_name]
        else:
            break
    else:
        break
print('Thank you for using the Hotels app!')