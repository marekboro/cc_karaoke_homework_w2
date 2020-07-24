import unittest
#import classes.song
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        name = "Under Pressure"
        genre = "rock"
        self.song = Song(name,genre)

    def test_song_has_name(self):
        pass

