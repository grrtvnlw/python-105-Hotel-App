hotel = {
    "Room 101": {},
    "Room 102": {},
    "Room 103": {},
    "Room 104": {},
    "Room 105": {},
}





def is_vacant(room):
    if hotel[room] == {}:
        print(f"{room} is empty.")
    else:
        print(f'{room} is occupied by {hotel[room]["occupant_name"]}.')
is_vacant("Room 103")
is_vacant("Room 101")