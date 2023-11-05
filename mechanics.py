import random

def battle_phase(user_crew, user_crew_positions, enemy_crew, enemy_crew_positions):
    '''
    user_crew: the ship object
    enemy_crew: ship object
    user_crew_positions: an integer array [attackers, defenders, sailors, medics]
    enemy_crew_positions: an integer array [attackers, defenders, sailors, medics]
    '''
    user_hp = user_crew.getCrew() #user crew size
    enemy_hp = enemy_crew.getCrew() #enemy crew size
    
    user_crew_values = [x * user_crew.getPower() for x in user_crew_positions] 
    #this gives us [damage per tick, speed per tick, defense per tick, heal per tick]
    enemy_crew_values = [x * enemy_crew.getPower() for x in enemy_crew_positions]

    while(user_hp > 0 and enemy_hp > 0):
        user_hp -= (enemy_crew_values[0] - enemy_crew_values[2]) #user_hp gets subtracted by the enemy attacker's damage
        enemy_hp -= (user_crew_values[0] - user_crew_values[2]) #enemy_hp gets subtracted by the user's attacker damage

        user_diff = int(user_hp) - sum(user_crew_positions) #get the number of units killed in this tick on user team
        enemy_diff = int(enemy_hp) - sum(enemy_crew_positions) #get the number of units killed in this tick on enemy team

        for i in range(user_diff):
            user_crew_values[randrange(0, 4)] -= 1 #for each dead crew mate, lose a random position
        for i in range(enemy_diff):
            user_crew_values[randrange(0, 4)] -= 1 #for each dead crew mate, lose a random position
        
        if(user_hp <= 0 and enemy_hp <= 0): return 0 #tie
        if(user_hp <= 0): return -1 #enemy wins
        if(enemy_hp <= 0): return 1 #user wins

        user_hp += user_crew_values[3]
        enemy_hp += enemy_crew_values[3]

        #update new positions (after some died lol)
        user_crew_values = [x * user_crew.getPower() for x in user_crew_positions] 
        enemy_crew_values = [x * enemy_crew.getPower() for x in enemy_crew_positions]
    
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