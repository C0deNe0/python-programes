#Design and implement an Adapter Pattern for a Music System.

class musicPlayer:
    def play(self):
        pass

#ADAPTER 1
class mp3Player:
    def play(self):
        print("playing mp3 music")

#ADAPTER 2 
class cdPlayer:
    def play(self):
        print("playing cd player")

#ADAPTER
class musicplayerAdapter(musicPlayer):
    def __init__(self,player):
        self.player = player
    
    def play(self):
        if isinstance(self.player,mp3Player):
            self.player.play()
        elif isinstance(self.player, cdPlayer):
            self.player.play()

#=======================================================#
#CLIENT CODE
if __name__ =="__main__":
    mp3player = mp3Player()
    cdplayer = cdPlayer()
    
    mp3A = musicplayerAdapter(mp3player)
    cdA = musicplayerAdapter(cdplayer)
    
    mp3A.play()
    cdA.play()
    
