from enum import StrEnum

class Trn(StrEnum):
    BAIXO = "baixo"
    MEDIO = "medio"
    ALTO = "alto"

class LogComm:
    def __init__(self):
        self.dis = 0
        self.rain = ""
        self.trn = ""
        self.frag = ""
        self.dayweek = 1

        self.week = {
            "segunda" : 1,
            "terca" : 2,
            "quarta" : 3,
            "quinta" : 4,
            "sexta" : 5,
            "sabado" : 6,
            "domingo" : 7
        }
        pass

    def checkYN(self, value):
        return str(value).upper() == "S"

    def Anl1(self):
        return "ATRASA" if self.checkYN(self.rain) and self.trn == Trn.ALTO.value else "NO PRASO"
    
    def Anl2(self):
        return "ATRASA" if self.dis > 300 and (self.dayweek == self.week.get("sabado") or self.dayweek == self.week.get("domingo")) else "NO PRASO"
    
    def Anl3(self):
        return "ATRASA" if self.checkYN(self.frag) and self.trn != Trn.BAIXO.value else "NO PRASO"
    
    def Anl4(self):
        return "ATRASA" if self.dis > 50 or self.trn != Trn.BAIXO.value else "NO PRASO"
    
    def Anl5(self):
        return "ATRASA" if self.checkYN(self.rain) and self.dis > 200 else "NO PRASO"
    
    def inputSystem(self):
        self.dis = int(input())
        self.rain = str(input())
        self.trn = str(input())
        self.frag = str(input())
        self.dayweek = int(input())
        pass

    def values(self):
        self.dis = 80
        self.rain = "S"
        self.trn = "alto"
        self.frag = "N"
        self.dayweek = 3
        pass

    def run(self):
        self.inputSystem()
        # self.values()
        late = 0
        Anl = [self.Anl1(), self.Anl2(), self.Anl3(), self.Anl4(), self.Anl5()]

        for i in range(5):
            print("Analista ", i+1, ":", Anl[i])
            if Anl[i] == "ATRASA": late += 1
        
        print("ATRASA: ", late)
        print("NO PRASO: ", 5 - late)
        print("DECISAO: ", "NO PRASO" if late < 3 else "ATRASA")
    
lab = LogComm()
lab.run()