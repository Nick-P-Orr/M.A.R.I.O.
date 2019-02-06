#from MLCode import MLCode

class game:

    def setString(self):
        return "This is Game.py"
    
    def printString(self):
         print("This is Game.py")

    def checkML(self):
        temp = MLCode
        print(temp.printS(temp))

 #   def main(self):
#        x = 1
#        while 1:
#            game.printString(self)
#            if(x != 1):
#                game.checkML(self)
#            x = 0

if __name__ == '__main__':
#    game().main()
    game().printString()
    game().setString()
    game().checkML()



    
