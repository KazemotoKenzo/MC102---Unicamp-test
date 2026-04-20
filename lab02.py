class Subs:
    def __init__(self):
        self.n = 0
        self.r = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def inputSystem(self):
        self.n = int(input())
        self.r = float(input())
        self.x = float(input())
        self.y = float(input())
        self.z = float(input())
    
    def iCFlix(self):
        self.x = self.x * 1.1
    
    def iCBank1(self):
        self.y = (self.y + (self.r * self.n)) * 0.8

    def iCBank2(self):
        self.z = self.z + (self.r * self.n * 0.5) 
    
    def calc(self):
        self.iCFlix()
        self.iCBank1()
        self.iCBank2()

    def values(self,n, r, x, y, z):
        self.n = n
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def run(self):
        self.inputSystem()
        # self.values(, , , ,)
        self.calc()
        print(not (self.x > self.y or self.x > self.z))

lab = Subs()
lab.run()