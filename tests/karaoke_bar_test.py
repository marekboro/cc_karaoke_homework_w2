import unittest
from classes.karaoke_bar import KaraokeBar
from classes.song import Song
from classes.guest import Guest
from classes.room import Room


class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        room_1 = Room(1,[],False,None,300)
        room_2 = Room(2,[],False,None,300)
        room_3 = Room(3,[],False,None,300)
        room_4 = Room(4,[],False,None,300)
        room_5 = Room(5,[],False,None,300)

        self.Bar_rooms = [room_1,room_2,room_3,room_4,room_5]
        
        song_1 = Song("Song 1", "indie_rock")
        song_2 = Song("Song 2","pop")
        song_3 = Song("Song 3","rock")
        song_4 = Song("Song 4","rock")
        song_5 = Song("Song 5","rock")
        song_6 = Song("Song 6","disco")
        song_7 = Song("Song 7","disco")
        song_8 = Song("Song 8","pop")
        song_9 = Song("Song 9","funk")
        song_10 = Song("Song 10","funk")
        
        self.songs_database = [song_1,song_2,song_3,song_4,song_5,song_6,song_7,song_8,song_9,song_10]
        
        self.money_in_till = 200
        
        self.the_bar = KaraokeBar(self.Bar_rooms, self.money_in_till, self.songs_database)

        self.customer_1 = Guest("Mr Curst Omar1",600, song_8)
        self.customer_2 = Guest("Mr Curst Omar2",400, song_1)
        self.customer_3 = Guest("Mr Curst Omar3",500, song_2)
        self.customer_4 = Guest("Mr Curst Omar4",290, song_3)
        self.customer_5 = Guest("Mr Curst Omar5",310, song_5)
        self.customer_6 = Guest("Mr Curst Omar6",400, song_6)
        self.customer_7 = Guest("Mr Curst Omar7",400, song_9)
        #self.check_in = KaraokeBar.check_in
    #def test_bar_has_a_name(self):

   #     pass
    def test_name_of_bar(self):
        expected = "Singoholics Annonymous"
        bar_name = self.the_bar.get_name()
        actual = bar_name
        self.assertEqual(expected,actual)

    def test_checking_name_after_customer__checks_into_a_room_(self):
        expected = "hello"
        the_customer = self.customer_1
        self.the_bar.check_in(0,the_customer)
        #[1].check_in_to_room(customer_1)
        
        customer_name = self.the_bar.rooms[0].occupant.name
        actual = customer_name
        self.assertEqual(expected,actual)

    
