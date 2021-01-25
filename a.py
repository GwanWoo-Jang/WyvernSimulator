import random


ice = 0
earth = 1
fire = 2
light = 3
dark = 4


def fight():
    turn = 0
    while True:
        break


class Unit:
    def __init__(self, name, type, attack, defence, health, speed, chance_ch, damage_ch, effect, resistance_effect, chance_dual ):
        self.name = name
        self.type = type
        self.attack = attack
        self.defence = defence
        self.health = health
        self.speed = speed
        self.chance_ch = chance_ch * 0.01
        self.damage_ch = damage_ch * 0.01
        self.effect = resistance_effect * 0.01
        self.chance_dual = chance_dual *0.01
        print(name + " 생성")
		
my_unit1 = Unit("생성된 유닛1", ice, 100, 100, 1500, 300, 15, 150, 0, 0, 5)
enermy_unit1 = Unit("생성된 유닛2", fire, 100, 100, 1500, 50, 15, 150, 0, 0, 5)

#tempspeed_unit1 = my_unit1.speed + my_unit1.speed * (random.random()*0.05)

#print(tempspeed_unit1)

	
 




        
