class Ship:
    def __init__(self, crew, power, wealth):
        '''
        Crew: array of Pirates
        Power: Integer
        Wealth: Integer
        '''
        self.crew = crew
        self.power = power
        self.wealth = wealth

    def getPirateByName(self, name):
        for pirate in crew:
            if pirate.getName() == name:
                return pirate
    
    def getCrew(self):
        return self.crew

    def getPirateType(self):
        return self.pirateType