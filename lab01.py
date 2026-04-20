class IntArith:
    def __init__(self):
        self.a = 0
        self.b = 0

    def inputSystem(self):
        self.a = int(input("Number a: "))
        self.b = int(input("Number b: "))
    
    def add(self):
        print("a + b =", (self.a + self.b))
    
    def sub(self):
        print("a - b =", (self.a - self.b))

    def mult(self): 
        print("a * b =", (self.a * self.b))
    
    def expo(self):
        print("a ** b =", (self.a ** self.b))
    
    def div(self):
        print("a // b =", (self.a // self.b))
    
    def rem(self):
        print("a % b =", (self.a % self.b))
    
    def vars(self):
        print("a =",self.a, "\nb =",self.b)

    def run(self):
        self.vars()
        self.add()
        self.sub()
        self.mult()
        self.expo()
        self.div()
        self.rem()

lab = IntArith()
lab.inputSystem()
lab.run()