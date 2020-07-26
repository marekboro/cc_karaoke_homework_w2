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
    
    def random_song_play(self,song_list):
        print("wollooloo ")
        return f"La la la {random.choice(self.song_list).name}"
        #return "oh my gosh"

    def rand_1(self):
        return f"La la la {random.choice(self.song_list).name}"
       # print("hi")

    def rand_2(self):           # this 
        return "rand2"          # and this seems to work

    def rand_3(self,song_list):
        random_name = random.choice(song_list).name
        return f" rand3 name: {random_name}"

    def song_name(self,song):
        return song.name

    def play_random_song(self,song_list):
        random_song= random.choice(song_list)
        return random_song
        

