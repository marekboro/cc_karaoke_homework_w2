import random
class KaraokeBar:
    def __init__(self,rooms,till,songsDB):
        self.name = "Singoholics Annonymous"
        self.rooms = rooms
        self.till = till
        self.songsDB = songsDB
    

    def get_name(self):
        bar_name = self.name
        return bar_name

    def check_in(self,room_number, customer):
        self.rooms[room_number].check_in_to_room(customer,room_number)

    def add_songs_to_room_list(self, room_number):
        self.rooms[room_number].song_list.extend(self.songsDB)

    #def play_songs(self,room_number):
    #    self.rooms[room_number]

