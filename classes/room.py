from classes.guest import Guest
from classes.song import Song
import random

class Room:
    def __init__(self,aroom_number,song_list,is_occupied,occupant, price):
        self.aroom_number = aroom_number
        self.song_list = song_list
        self.is_occupied = is_occupied # if this is set to False by default, then the setUp from run_tests will fail to create an occupied room causing test: test_room2_is_occupied_true to FAIL. Why does setUp not overwrite this??
        self.price = price
        self.occupant = occupant
        #occupant    # aka guest
    
# - EXTENSION

    # def play_random_song(self,song_list):
    #     random_song= random.choice(song_list)
    #     return random_song

# - /EXTENSION
    
    def check_in_to_room(self,Guest, aroom_number):
        if self.is_occupied:
            return "Room is not empty"
        elif not self.is_occupied:
                self.occupant = Guest
                self.is_occupied = True
                Guest.modify_wallet(-self.price)
                #kareokebar.modify_till(self.price) # to update kareoke bar cash
                return f"Welcome to room {aroom_number}"

