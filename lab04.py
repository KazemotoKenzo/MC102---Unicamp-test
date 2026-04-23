from enum import StrEnum

class Spell(StrEnum):
    EXP = "expelliarmus"
    STS = "sectumsempra"
    PTG = "protego"
    CLT = "chocolate"

#    def execute(self):
#        match self:
#            case Spell.EXP:
#                print("Expelliarmus")
#                pass

#            case Spell.STS:
#                print("Sectumsempra")
#                pass

#            case Spell.PTG:
#                print("Protego")
#                pass

#            case Spell.CLT:
#                print("Chocolate")
#                pass

class WizardDuel:
    def __init__(self):
        self.wizard_hp = 0
        self.wizard_mp = 0
        self.enemie_hp = 0
        self.enemie_dg = 0
        self.berzerk   = 0

        self.action    = ""

        self.turn = True

        self.reducedamage = False
        self.bleed        = 0
        self.protect      = False

        self.dispatch = {
            Spell.EXP: self.exp,
            Spell.STS: self.sts,
            Spell.PTG: self.ptg,
            Spell.CLT: self.clt
        }
        pass

    def exp(self):
        if(self.wizard_mp < 5):
            self.wizard_hp -= 5
            return
        
        self.wizard_mp -= 5
        self.enemie_hp -= 10
        self.reducedamage = True
        pass
        

    def sts(self):
        if(self.wizard_mp < 20):
            self.wizard_hp -= 5
            return
        
        self.wizard_mp -= 20
        self.enemie_hp -= 10
        self.bleed      = 3
        pass

    def ptg(self):
        if(self.wizard_mp < 10):
            self.wizard_hp -= 5
            return
        
        self.wizard_mp -= 10
        self.protect    = True
        pass

    def clt(self):
        self.wizard_mp += 15
        self.wizard_hp += 10
        return

    def enemieAction(self):
        if self.protect:
            self.protect = False
            return
        
        reduce = 0
        if self.reducedamage:
            reduce = 5
            self.reducedamage = False

        mult = 1
        if self.enemie_hp <= self.berzerk: mult = 2

        damage = (self.enemie_dg * mult) - reduce
        self.wizard_hp -= damage if damage > 0 else 0
        pass

    def bleedEffect(self):
        if(self.bleed > 0): self.enemie_hp -= 5
        self.bleed -= 1
        pass

    def spellAction(self):
        self.action = str(input()).lower()
        self.dispatch[self.action]()
        pass

    def end(self):
        if(self.wizard_hp <= 0):
            print("Bruxo perdeu a batalha!")
            return True
        if(self.enemie_hp <= 0):
            print("Bruxo venceu a batalha!")
            return True
        return False

    def inputSystem(self):
        self.wizard_hp = int(input())
        self.wizard_mp = int(input())
        self.enemie_hp = int(input())
        self.enemie_dg = int(input())
        self.berzerk   = int(input())
        pass

    def run(self):
        self.inputSystem()

        while(True):
            self.spellAction()
            if self.end(): break
            self.enemieAction()
            if self.end(): break
            self.bleedEffect()
            if self.end(): break
        pass
        
    def values(self):
        self.wizard_hp = 100
        self.wizard_mp = 20
        self.enemie_hp = 25
        self.enemie_dg = 10
        self.berzerk   = 10
        pass

lab04 = WizardDuel()
lab04.run()
