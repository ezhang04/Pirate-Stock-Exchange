import random

def battle_phase(user_crew, user_crew_positions, enemy_crew, enemy_crew_positions):
    '''
    user_crew: the ship object
    enemy_crew: ship object
    user_crew_positions: an integer array [attackers, defenders, sailors, medics]
    enemy_crew_positions: an integer array [attackers, defenders, sailors, medics]
    '''
    power1 = user_crew.getPower()
    power2 = enemy_crew.getPower()
    win = 0
    
    for i in range(4):
        if ((user_crew_positions[i]*power1 - enemy_crew_positions[i]*power2) < 0):
            win -= 1
        elif ((user_crew_positions[i]*power1 - enemy_crew_positions[i]*power2) > 0):
            win += 1
    if (win < 0):
        return -1
    elif (win > 0):
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