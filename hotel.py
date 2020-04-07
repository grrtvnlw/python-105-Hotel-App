hotel_california = {
    "Room 101": "Dwayne",
    "Room 102": "Darrell",
    "Room 103": "Dwight",
    "Room 104": "Dilly Dilly",
    "Room 105": ""
}
print(hotel_california)
# put someone in an unoccupied room
def book_room(room, name):
    if hotel_california[room] == '':
        hotel_california[room] = name
    else:
        print(f'{room} is occupied!')
book_room("Room 105", "Delilah")
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
        print("Empty Room.")
    else:
        print(f'Room is occupied by {hotel_california[room]}.')
room_occupied("Room 103")
room_occupied("Room 101")