class Sfinal():

    def __init__(self):
        
        self.sfinal = []
        self.result = []


    def addteams(self,qfinal):
        for team in qfinal.winners():
            self.sfinal.append(team)
            self.result.append({"Goals":0,"Won":False})
    
    def addresult(self,team,goal,won):
        for i in range(len(self.sfinal)):
            if team.country_getter == self.sfinal[i].country_getter:
                self.result[i]["Goals"] = goal
                self.result[i]["Won"] = won
    
    def winners(self):

        winners = []
        for i in range(len(self.result)):
            if self.result[i]["Won"]:
                winners.append(self.sfinal[i])
        return winners

    def lossers(self):

        lossers = []
        for i in range(len(self.result)):
            if not (self.result[i]["Won"]):
                lossers.append(self.sfinal[i])
        return lossers
