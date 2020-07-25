#from classes.guest import Guest

class Room:
    def __init__(self,aroom_number,song_list,is_occupied,occupant, price):
        self.aroom_number = aroom_number
        self.song_list = song_list
        self.is_occupied = is_occupied # if this is set to False by default, then the setUp from run_tests will fail to create an occupied room causing test: test_room2_is_occupied_true to FAIL. Why does setUp not overwrite this??
        self.price = price
        self.occupant = occupant
        #occupant    # aka guest

