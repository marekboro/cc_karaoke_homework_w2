class Guest:
    def __init__(self,name,wallet,fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
    
    def modify_wallet(self,ammount):
        self.wallet = round(self.wallet + ammount,2) # without rounding up, subtraction in floats is a dangerous game. 
        
    def get_fav_song(self):
        return self.fav_song
    def check_playlist(self, songlist):
        if songlist.count(self.fav_song) >= 1:
            return "Woohoo!"
        else:
            return "oh no"


    # def check_playlist(self, songlist):
    #     for self.fav_song in songlist:
    #         return "Woohoo!"
    #     else:
    #         return "oh no"

        