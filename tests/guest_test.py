import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        name = "Homer Simpson"
        money_in_wallet = 240.20
        fav_song = "Radio GaGa"
        self.guest = Guest(name,money_in_wallet,fav_song)

    def test_guest_has_a_name(self):
        pass
