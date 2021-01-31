import random


ice = 0
earth = 1
fire = 2
light = 3
dark = 4

def caculate_gauge(list_speed, list_gauge):
    result = []
    if len(list_speed) != len(list_gauge):
        print("길이 오류")
        return -1
    for i in range(len(list_speed)):
        result.append((100 - list_gauge[i])/list_speed[i])
    min_result = min(result)
    for i in range(len(result)):
        if min_result == result[i]:
            result[i] = 100
        else :
            result[i] = result[i] + ((min_result/result[i]) * 100 )
    return result


def fight(my_unit1,my_unit2 ,enermy_unit):
    turn = 0
    temp1 = start_speed_unit(my_unit1)
    temp2 = start_speed_unit(my_unit2)
    temp3 = start_speed_unit(enermy_unit)
    list_speed = [temp1, temp2, temp3]
    list_gauge = [0, 0, 0]
    list_gauge = caculate_gauge(list_speed, list_gauge)
    list_speed = [my_unit1.speed, my_unit2.speed, enermy_unit.speed]
    print(list_speed)
    for i in range(1, 5):
        print(i,"번째턴")
        n = 0
        for j in list_gauge:
            if j >= 100:
                n = 1
        if n == 0:
            print("연산")
            list_gauge = caculate_gauge(list_speed, list_gauge)
        print(list_gauge)
        max_gauge = max(list_gauge)
        list_gauge[list_gauge.index(max_gauge)] = 0





    

    
    
    

def start_speed_unit(unit):
    return unit.speed + unit.speed * (random.random() *0.05)




class Unit:
    def __init__(self, name, type_c, attack, defence, health, speed, chance_ch, damage_ch, effect, resistance_effect, chance_dual ):
        self.name = name
        self.type = type_c
        self.attack = attack
        self.defence = defence
        self.health = health
        self.speed = speed
        self.chance_ch = chance_ch * 0.01
        self.damage_ch = damage_ch * 0.01
        self.effect = resistance_effect * 0.01
        self.chance_dual = chance_dual *0.01
        self.gauge = 0
        print(name + " 생성")
    def skill_1():
        print("skill_1")
    def skill_2():
        print("skill_2")
    def skill_3():
        print("skill_3")



		
my_unit1 = Unit("생성된 유닛1", ice, 100, 100, 1500, 100, 15, 150, 0, 0, 5)
my_unit2 = Unit("생성된 유닛2", ice, 100, 100, 2000, 200, 15, 150, 0 ,0 ,5)
enermy_unit1 = Unit("생성된 유닛3", fire, 100, 100, 1500, 50, 15, 150, 0, 0, 5)

#tempspeed_unit1 = my_unit1.speed + my_unit1.speed * (random.random()*0.05)
#tempspeed_unit1 = start_speed_unit(my_unit1)






fight(my_unit1,my_unit2, enermy_unit1)
	
 




        
