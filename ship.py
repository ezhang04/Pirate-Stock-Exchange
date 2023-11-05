import pygame
class Ship:
    def __init__(self, crew, power, wealth,path):
        '''
        Crew: Integer (number of pirates)
        Power: Integer
        Wealth: Integer
        '''
        self.crew = crew
        self.power = power
        self.wealth = wealth
        self.sprite = pygame.image.load(path)
    
    def setCrew(self, crew):
        self.crew = crew
        
    def getCrew(self):
        return self.crew
    
    def addCrewMember(self):
        self.crew += 1

    def setPower(self, power):
        self.power = power

    def setWealth(self, wealth):
        self.wealth = wealth
    
    def getPower(self):
        return self.power
    
    def getWealth(self):
        return self.wealth