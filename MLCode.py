#from Communicator import Communicator
class MLCode:
    def setS(self):
        return "MLCode"

    def printS(self):
        print("MLCode")
    
#    def C(self):
#        tmp = Communicator
#        s = tmp.temp1(tmp)
#        print(str(tmp.temp1(tmp))+"2")

    def saveFile(self):
        file = open("MLCode.txt", "w")
        file.write("Hello\n")
        file.write(MLCode.setS(self)+"\n")
        file.close()

    def readFile(self):
        file = open("Game.txt", "r")
        for line in file:
            print(line)
        file.close()

if __name__ == '__main__':
#    MLCode().setS()
#    MLCode().printS()
#    MLCode().C()
    MLCode().saveFile()
    MLCode().readFile()
