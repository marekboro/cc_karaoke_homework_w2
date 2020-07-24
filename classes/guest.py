class Guest:
    def __init__(self,name,wallet,fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
    
    def modify_wallet(self,ammount):
        self.wallet = round(self.wallet + ammount,2) # without rounding up, subtraction in floats is a dangerous game. 
        

        