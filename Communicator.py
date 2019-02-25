from MarioLevel1 import MarioLevel

class Communicator:
    currentGame = None
    
    def newLevel(self):
        self.currentGame = MarioLevel()

    def passInput(self, commands):
        return self.currentGame.acceptInput(commands)
        

if __name__ == '__main__':
    Communicator().newLevel()
    Communicator().passInput()


#tmp = game
#print(tmp.setString(tmp)+"1")
