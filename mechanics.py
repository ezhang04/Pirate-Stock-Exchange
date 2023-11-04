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
    
def treasure (crew):
    value = random.randrange(0,501)
    temp = crew.getWealth()
    crew.setWealth(temp+value)

def death (crew):
    death = []
    death[0] = "Captain Slips-a-Lot fell overboard. Lost 1 crew member"
    death[1] = "No-Toes Ned the Napper fell out of the crow's nest while naping. Lost 1 crew member"
    death[2] = "Stumblebum Stan the Stinker died to an infection. Lost 1 crew member"
    death[3] = "Gigglin' Gus the Gullible accidently shot himself with his flintknock pistol. Lost 1 crew member"
    death[4] = "Captain Giggles McScurvy hasn't had an orange in a while. Lost 1 crew member from scurvy"
    death[5] = "Chucklin' Charlie the Clueless wanted to know what fire tasted like. Lost 1 crew member"
    death[6] = "Jolly Roger the Jokester made Captain Chucklechops laugh so hard he died. Lost 1 crew member"
    death[7] = "Captain Guffawsalot forced Chuckles the Clumsy walk the plank. Lost 1 crew member"
    num = random.randrange(0,8)
    num1 = crew.getCrew()
    crew.setCrew(num1-1)
    return death[num]