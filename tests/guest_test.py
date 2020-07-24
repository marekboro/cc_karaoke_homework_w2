import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        name = "Homer Simpson"
        money_in_wallet = 240.20
        fav_song = "Radio GaGa"
        self.guest = Guest(name,money_in_wallet,fav_song)
        self.guest2 = Guest(None,200,"Bohemian Rhapsody")

    def test_guest_has_a_name(self):
        expected = "Homer Simpson"
        actual = self.guest.name
        self.assertEqual(expected,actual)

    def test_guest2_has_no_name(self):
        expected = None
        actual = self.guest2.name
        self.assertEqual(expected,actual)
    
    def test_fav_song_guest1(self):
        expected = "Radio GaGa"
        actual = self.guest.fav_song
        self.assertEqual(expected,actual)

    def test_wallet_size(self):
        expected = 240.2
        actual = self.guest.wallet
        self.assertEqual(expected,actual)

    def test_add_100_to_wallet_guest1(self):
        expected = 340.2
        self.guest.modify_wallet(100.0)
        actual = self.guest.wallet
        self.assertEqual(expected,actual)
    
    def test_remove_120_point_5_from_wallet(self):
        expected = 119.7
        self.guest.modify_wallet(-120.5)
        actual = self.guest.wallet
        self.assertEqual(expected,actual)
        
    
    

    

    