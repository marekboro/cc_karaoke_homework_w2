import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUP(self):
        room_number = 1
        songs_list = ["Radio GaGa", "We are the champions"]
        is_occupied = False
        occupant = None
        price = 200.50
        self.room = Room(room_number,songs_list,is_occupied,occupant,price)
    
    def test_room_has_number(self):
        pass

