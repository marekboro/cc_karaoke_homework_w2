import unittest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        aroom_number = 1
        song1 = Song("Radio GaGa","rock")
        song2 = Song("We are the champions","rock")
        songs_list = [song1,song2]
        is_occupied = False
        occupant = None
        price = 200.50
        self.room = Room(aroom_number,songs_list,is_occupied,occupant,price)
    
    def test_room_number(self):
        expected = 1
        actual = self.room.aroom_number
        self.assertEqual(expected,actual)
        #pass
        

