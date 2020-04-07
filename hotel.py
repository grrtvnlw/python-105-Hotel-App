hotel_california = {
    "Room 101": {
        "occupant_name": "Dwayne",
        "phone_number": "111-111-1111",
        "prepaid": True
    },
    "Room 102": {
        "occupant_name": "Darrell",
        "phone_number": "222-222-2222",
        "prepaid": False
    },
    "Room 103": {
        "occupant_name": "Dwight",
        "phone_number": "333-333-3333",
        "prepaid": True
    },
    "Room 104": {
        "occupant_name": "Dilly Dilly",
        "phone_number": "444-444-4444",
        "prepaid": False
    },
    "Room 105": {
        "occupant_name": "",
        "phone_number": "",
        "prepaid": False
    },
}
print(hotel_california)
# put someone in an unoccupied room
def book_room(room, name):
    if hotel_california[room]["occupant_name"] == '':
        hotel_california[room]["occupant_name"] = name
    else:
        print(f'{room} is occupied!')
book_room("Room 105", "Delilah")
print(hotel_california)
book_room("Room 102", "DJ")
# make a room available by setting the occupent name to ''
def make_avail(room):
    hotel_california[room]["occupant_name"] = ''
    hotel_california[room]["phone_number"] = ''
    hotel_california[room]["prepaid"] = False
make_avail("Room 101")
print(hotel_california)
# check if a room number is valid
def room_check(room):
    if room in hotel_california:
        print(f'{room} is a room here at Hotel California.')
    else:
        print(f'{room} is not a room here at Hotel California.')
room_check("Room 105")
room_check("Room 110")
# check if a room number is occupied or not
def room_occupied(room):
    if hotel_california[room]["occupant_name"] == '':
        print(f"{room} is empty.")
    else:
        print(f'{room} is occupied by {hotel_california[room]["occupant_name"]}.')
room_occupied("Room 103")
room_occupied("Room 101")