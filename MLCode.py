from Communicator import Communicator
class MLCode:
    def setS(self):
        return "MLCode"

    def printS(self):
        print("MLCode")
    
    def C(self):
        tmp = Communicator
        s = tmp.temp1(tmp)
        print(str(tmp.temp1(tmp))+"2")

if __name__ == '__main__':
    MLCode().setS()
    MLCode().printS()
    MLCode().C()
