import random

def battle_phase(user_crew, enemy_crew):
    total_user = user_crew.crew_number
    total_enemy = enemy_crew.crew_number
    user = [0,0,0,0]
    enemy = [0,0,0,0]
    winner = 0
    
    while (user[0] <= total_user):
        user[0] = int(input("How many units do you want to put into attackers? "+str(total_user)+" units: "))
    total_user -= user[0]
    
    while (user[1] <= total_user):
        user[1] = int(input("How many units do you want to put into defenders? "+str(total_user)+" units: "))
    total_user -= user[1]
    
    while (user[2] <= total_user):
        user[2] = int(input("How many units do you want to put into sailors? "+str(total_user)+" units: "))
    total_user -= user[2]
    
    while (user[3] <= total_user):
        user[3] = int(input("How many units do you want to put into medics? "+str(total_user)+" units: "))
    total_user -= user[3]
    
    
    enemy[0] = random.randrange(0,total_enemy+1)
    total_enemy -= enemy[0]
    enemy[1] = random.randrange(0,total_enemy+1)
    total_enemy -= enemy[1]
    enemy[2] = random.randrange(0,total_enemy+1)
    total_enemy -= enemy[2]
    enemy[3] = random.randrange(0,total_enemy+1)
    total_enemy -= enemy[3]
    
    for i in range(3):
        if (user[i]*user_crew.power < enemy[i]*enemy_crew.power):
            winner -= 1
        elif (user[i]*user_crew.power > enemy[i]*enemy_crew.power):
            winner += 1
    
    if (winner > 0):
        return -1
    elif (winner < 0):
        return 1
    else:
        return 0
    
