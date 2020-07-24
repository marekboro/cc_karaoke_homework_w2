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

    # def test_guest2_has_name_fail(self):
    #     expected = "Homer Simpson"
    #     actual = self.guest2.name
    #     self.assertEqual(expected,actual)
    
    def test_guest2_has_name_None(self):
        expected = None
        actual = self.guest2.name
        self.assertEqual(expected,actual)

    

    