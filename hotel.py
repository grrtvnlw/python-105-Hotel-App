hotel_california = {
    "Room 101": '',
    "Room 102": '',
    "Room 103": '',
    "Room 104": '',
    "Room 105": '',
}

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

hotel_california["Room 101"] = Dwayne
hotel_california["Room 102"] = Darrell
hotel_california["Room 103"] = Dwight
hotel_california["Room 104"] = Dilly_Dilly
print(hotel_california)
# put someone in an unoccupied room
def book_room(room, name):
    if hotel_california[room] == '':
        hotel_california[room] = name
    else:
        print(f'{room} is occupied!')
book_room("Room 105", Delilah)
print(hotel_california)
book_room("Room 102", "DJ")
# make a room available by setting the occupent name to ''
def make_avail(room):
    hotel_california[room] = ''
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
    if hotel_california[room] == '':
        print(f"{room} is empty.")
    else:
        print(f'{room} is occupied by {hotel_california[room]["occupant_name"]}.')
room_occupied("Room 103")
room_occupied("Room 101")