from enum import StrEnum

class Spell(StrEnum):
    EXP = "expelliarmus"
    STS = "sectumsempra"
    PTG = "protego"
    CLT = "chocolate"

    def execute(self):
        match self:
            case Spell.EXP:
                print("Expelliarmus")
                pass

            case Spell.STS:
                print("Sectumsempra")
                pass

            case Spell.PTG:
                print("Protego")
                pass

            case Spell.CLT:
                print("Chocolate")
                pass

class WizardDuel:
    def __init__(self):
        self.wizard_hp = 0
        self.wizard_mp = 0
        self.enemie_hp = 0
        self.enemie_dg = 0
        self.berzerk   = 0

        self.action    = ""

        self.turn = True
        pass

    def spellAction(self):
        self.action = str(input()).lower()
        Spell(self.action).execute()

lab04 = WizardDuel()
lab04.spellAction()
