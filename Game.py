#from MLCode import MLCode
#from Communicator import Communicator

class game:

    def setString(self):
        return "This is Game.py"
    
    def printString(self):
         print("This is Game.py")

    def saveFile(self):
        file = open("Game.txt", "w")
        file.write("Hello\n")
        file.write(game.setString(self)+"\n")
        file.close()

    def readFile(self):
        file = open("MLCode.txt", "r")
        for line in file:
            print(line)
        file.close()

if __name__ == '__main__':
#    game().main()
#    game().printString()
#    game().setString()
#    game().checkML()
    game().saveFile()
    game().readFile()


    
