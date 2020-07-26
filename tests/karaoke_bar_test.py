import unittest
from classes.karaoke_bar import KaraokeBar

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        rooms = [1,2,3,4]
        money_in_till = 100
        are_rooms_available = True
        songs_database = ["Radio GaGa","We are the champions","Under Pressure"]
        self.the_bar = KaraokeBar(rooms,are_rooms_available, money_in_till,songs_database)


    #def test_bar_has_a_name(self):

   #     pass
    def test_name_of_bar(self):
        expected = "Singoholics Annonymous"
        bar_name = self.the_bar.get_name()
        actual = bar_name
        self.assertEqual(expected,actual)