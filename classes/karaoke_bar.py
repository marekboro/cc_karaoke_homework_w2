class KaraokeBar:
    def __init__(self,rooms,has_available_rooms ,till,songsDB):
        self.name = "Singoholics Annonymous"
        self.rooms = rooms
        self.has_available_rooms = has_available_rooms
        self.till = till
        self.songsDB = songsDB
    

    def get_name(self):
        bar_name = self.name
        return bar_name
    #def count_available_rooms()

