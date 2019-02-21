from Game import game

class Communicator:
    currentGame = null
    
    def newLevel(self):
        self.currentGame = game()

    def passInput(commands):
        return self.currentGame.acceptInput(commands)
        

if __name__ == '__main__':
    Communicator().newLevel()
    Communicator().passInput()


#tmp = game
#print(tmp.setString(tmp)+"1")
