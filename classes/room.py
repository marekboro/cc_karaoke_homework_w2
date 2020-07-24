#from classes.guest import Guest

class Room:
    def __init__(self,room_number,song_list,is_occupied,occupant, price):
        self.room_number = room_number
        self.song_list = song_list
        self.is_occupied = False
        self.price = price
        self.occupant = occupant

