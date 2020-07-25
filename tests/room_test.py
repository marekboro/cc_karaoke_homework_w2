import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        aroom_number = 1
        song1 = Song("Radio GaGa","rock")
        song2 = Song("We are the champions","rock")
        song3 = Song("Breed","grunge")
        songs_list = [song1,song2]
        is_occupied = False
        guest1 = None
        guest2 = Guest("Bert Sampson",9001, song3)
        #occupant = guest2
        price = 200.50
        self.room = Room(aroom_number,songs_list,is_occupied,guest1,price)
        
        
        self.room2 = Room(2,self.room.song_list,True, guest2,730)

    
    def test_room_number(self):
        expected = 1
        actual = self.room.aroom_number
        self.assertEqual(expected,actual)

    def test_song_list_name_entry_at_index_0(self):
        expected = "Radio GaGa"
        actual = self.room.song_list[0].name
        self.assertEqual(expected,actual)
        
    def test_song_list_genre_entry_at_index_1(self):
        expected = "rock"
        actual = self.room.song_list[1].genre
        self.assertEqual(expected,actual)

    def test_room_is_occupied_false(self):
        expected = False
        actual = self.room.is_occupied
        actual = self.room.is_occupied
        self.assertEqual(expected,actual)

    def test_room2_is_occupied_true(self):
        expected = True
        actual = self.room2.is_occupied
        self.assertEqual(expected,actual)
    
    def test_room2_guest_name(self):
        expected = "Bert Sampson"
        actual = self.room2.occupant.name
        self.assertEqual(expected,actual)

    def test_room2_geuest_fav_song(self):
        expected = "Breed"
        actual = self.room2.occupant.fav_song.name
        self.assertEqual(expected,actual)


