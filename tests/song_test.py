import unittest
#import classes.song
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        name = "Under Pressure"
        genre = "rock"
        self.song = Song(name,genre)

    def test_name_of_song(self):
        expected = "Under Pressure"
        actual = self.song.name
        self.assertEqual(expected,actual)

    def test_genre_of_song(self):
        expected = "rock"
        actual = self.song.genre
        self.assertEqual(expected,actual)
