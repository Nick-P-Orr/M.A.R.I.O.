from MarioLevel1 import MarioLevel

class Communicator:
    currentGame = None
    createOutput = True
    
    def newLevel(self):
        self.currentGame = MarioLevel()

    def passInput(self, commands):
        if self.createOutput and commands != None:
            file = open('commands.txt', 'a')
            for com in commands:
                if com == 0:
                    file.write('left,')
                elif com == 1:
                    file.write('right,')
                elif com == 2:
                    file.write('run,')
                elif com == 3:
                    file.write('jump,')
            file.write('\n')
            file.close()

        return self.currentGame.acceptInput(commands)
        

if __name__ == '__main__':
    Communicator().newLevel()
    Communicator().passInput()


#tmp = game
#print(tmp.setString(tmp)+"1")
