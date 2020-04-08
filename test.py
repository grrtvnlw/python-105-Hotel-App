import json

Hotel_California = {
    "Hotel Name": "Hotel California",
    "101": {
        "bed type": "king",
        "pet friendly": True,
    },
    "102": {
        "bed type": "queen",
        "pet friendly": True,
    },
    "103": {
        "bed type": "double twin",
        "pet friendly": True,
    },
    "104": {
        "bed type": "king",
        "pet friendly": False,
    },
    "105": {
        "bed type": "queen",
        "pet friendly": False,
    },
    "106": {
        "bed type": "double twin",
        "pet friendly": False,
    },
}

Hotel_Atlanta = {
    "Hotel Name": "Hotel Atlanta",
    "101": {
        "bed type": "king",
        "pet friendly": True,
    },
    "102": {
        "bed type": "queen",
        "pet friendly": True,
    },
    "103": {
        "bed type": "double twin",
        "pet friendly": True,
    },
    "104": {
        "bed type": "king",
        "pet friendly": False,
    },
    "105": {
        "bed type": "queen",
        "pet friendly": False,
    },
    "106": {
        "bed type": "double twin",
        "pet friendly": False,
    },
}

Hotel_Trivago = {
    "Hotel Name": "Hotel Trivago",
    "101": {
        "bed type": "king",
        "pet friendly": True,
    },
    "102": {
        "bed type": "queen",
        "pet friendly": True,
    },
    "103": {
        "bed type": "double twin",
        "pet friendly": True,
    },
    "104": {
        "bed type": "king",
        "pet friendly": False,
    },
    "105": {
        "bed type": "queen",
        "pet friendly": False,
    },
    "106": {
        "bed type": "double twin",
        "pet friendly": False,
    },
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

# function to check a person into a room
def check_in(inp):
    
    for index in range(len(hotels)):
        if hotels[index]["Hotel Name"] == inp:
            inp = index
            room = input("What room? ")
            if hotels[index][room] == {}:
                name = new_customer()
                hotels[index][room] = name
            else:
                print(f'Room {room} is occupied!')

# function to check a person out of the room and return the person dictionary
def check_out(inp):
    for index in range(len(hotels)):
        if hotels[index]["Hotel Name"] == inp:
            inp = index
            room = input("What room are you checking out of? ")
            if hotels[inp][room]["prepaid"] == True:
                print("They're all paid up! Check them out.")
                guest_info = hotels[inp][room]
                hotels[inp][room] = {}
                return guest_info
            else:
                print("They haven't paid! Keep them here forever.")

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
        "Hotel Name": name,
            "101": {
                "bed type": "king",
                "pet friendly": True,
            },
            "102": {
                "bed type": "queen",
                "pet friendly": True,
            },
            "103": {
                "bed type": "double twin",
                "pet friendly": True,
            },
            "104": {
                "bed type": "king",
                "pet friendly": False,
            },
            "105": {
                "bed type": "queen",
                "pet friendly": False,
            },
            "106": {
                "bed type": "double twin",
                "pet friendly": False,
            },
    }
    return name

# request room type based off bed
def request_room_type(inp, room_type):
    for index in range(len(hotels)):
        if hotels[index]["Hotel Name"] == inp:
            inp = index
            if hotels[inp][room]["bed type"] == room_type:
                if hotels[inp][room]["bed type"] == 
                guest_info = hotels[inp][room]
                hotels[inp][room] = {}
                return guest_info
            else:
                print("They haven't paid! Keep them here forever.")

# request pet friendly room
def request_pet_friendly(inp):

# save room data
def save_room_info():
    file_name = "room_data.json"
    with open(file_name, "w") as save_file:
        json.dump(hotels, save_file)

# load room data
def load_room_info():
    file_name = "room_data.json"
    with open(file_name, "r") as file_handle:
        new_hotels = json.load(file_handle)
        try:
            for item in range(len(new_hotels)):
                hotels[item] = new_hotels[item]
        except IndexError:
            hotels.append(new_hotels[item])

while True:
    menu_choice = int(input(main_menu))
    # Print list of hotels
    if menu_choice == 1:
        for hotel in hotels:
            print(hotel)
    # Check in a customer
    elif menu_choice == 2:
        hotel_name = input("What hotel? ")
        preferance = input("Do you have a bed preferance? ").lower()
        check_in(hotel_name)
        if preferance == "yes":
            rm_type = input("King, Queen, or Double Twin? ").lower()
            request_room_type(hotel_name, rm_type)
        else:
            break
    # Check out a customer
    elif menu_choice == 3:
        hotel_name = input("What hotel are you checking out of? ")
        check_out(hotel_name)
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
                hotels[:] = [hotel for hotel in hotels if hotel.get('Hotel Name') != hotel_name]
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
                save_room_info()
                print("Room data has been successfully saved.")
            # load room info
            elif menu_choice == 3:
                load_room_info()
                print("Room data has been successfully loaded.")
            # Go back to main loop
            else:
                break
    # Exit the programs
    else:
        break
print('Thank you for using the Hotels app!')