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

    def modify_till(self, number):
        self.till = round(self.till + number,2)

    def check_in(self,room_number, customer):
        try:
            self.rooms[room_number].check_in_to_room(customer,room_number)
            self.modify_till(self.rooms[room_number].price)
        except:
            return self.rooms[room_number].check_in_to_room(customer,room_number)

    def add_songs_to_room_list(self, room_number):
        self.rooms[room_number].song_list.extend(self.songsDB)

   

