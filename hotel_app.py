
Hotel_California = {
    "Hotel Name": "Hotel California",
    "101": {},
    "102": {},
    "103": {},
    "104": {},
    "105": {},
}

Hotel_Atlanta = {
    "Hotel Name": "Hotel Atlanta",
    "101": {},
    "102": {},
    "103": {},
    "104": {},
    "105": {},
}

Hotel_Trivago = {
    "Hotel Name": "Hotel Trivago",
    "101": {},
    "102": {},
    "103": {},
    "104": {},
    "105": {},
}

hotels = [Hotel_California, Hotel_Atlanta, Hotel_Trivago]

main_menu = '''

1. Print hotel room status
2. Check in customer
3. Check out customer
4. Manage hotels
5. Manage room data
6. Quit

'''

manage_hotels = '''

1. Print hotel list
2. Add a new hotel
3. Close an existing hotel
4. Quit

'''

room_data = '''

1. Print hotel list
2. Save room data
3. Load room data
4. Quit

'''

Dwayne = {
    "occupant_name": "Dwayne",
    "phone_number": "111-111-1111",
    "prepaid": True
}

Darrell = {
    "occupant_name": "Darrell",
    "phone_number": "222-222-2222",
    "prepaid": False
}

Dwight = {
    "occupant_name": "Dwight",
    "phone_number": "333-333-3333",
    "prepaid": True
}

Dilly_Dilly = {
    "occupant_name": "Dilly Dilly",
    "phone_number": "444-444-4444",
    "prepaid": False
}

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
    if hotels[hotel][room] == {}:
        hotels[hotel][room] = name
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

# function to create a new hotel
def new_hotel():
    name = input("What's the name of the hotel? ")
    name = {
        "name": name,
            "101": {},
            "102": {},
            "103": {},
            "104": {},
            "105": {},
    }
    return name

def save_room_info():

def load_room_info():

while True:
    menu_choice = int(input(main_menu))
    # Add if/else statements for each menu item
    # Print list of hotels
    if menu_choice == 1:
        for hotel in hotels:
            print(hotel)
    # Check in a customer
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
    # Check out a customer
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
    # Manage hotels
    elif menu_choice == 4:
        while True:
            menu_choice = int(input(manage_hotels))
            # Print list of hotels
            if menu_choice == 1:
                print(hotels)
            # Add a new hotel
            elif menu_choice == 2:
                hotels.append(new_hotel())
            # Remove a hotel
            elif menu_choice == 3:
                hotel_name = input("Which hotel are we closing? ")
                if hotel_name == "Hotel California":
                    hotel_name = Hotel_California
                elif hotel_name == "Hotel Atlanta":
                    hotel_name = Hotel_Atlanta
                elif hotel_name == "Hotel Trivago":
                    hotel_name = Hotel_Trivago
                else:
                    print("No such hotel - sorry!")
                hotel_int = hotels.index(hotel_name)
                del hotels[hotel_int]
            # Go back to main loop
            else:
                break
    # Manage room data
    elif menu_choice == 5:
        while True:
            menu_choice = int(input(room_data))
            # Print list of hotels
            if menu_choice == 1:
                print(hotels)
            # save room data
            elif menu_choice == 2:
            # load room info
            elif menu_choice == 2:
            # Go back to main loop
            else:
                break
    # Exit the programs
    else:
        break
print('Thank you for using the Hotels app!')