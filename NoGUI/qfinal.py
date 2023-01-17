class Qfinal():

    def __init__(self):
        
        self.qfinal = []
        self.result = []


    def addteams(self,round16):
        for team in round16.winners():
            self.qfinal.append(team)
        self.result.append({"Goals":0,"Won":False})
    
    def addresult(self,team,goal,won):
        
        for i in range(len(self.qfinal)):
            if team.country_getter() == self.qfinal[i].country_getter():
                self.result[i]["Goals"] = goal
                self.result[i]["Won"] = won
    
    def winners(self):

        winners = []
        for i in range(len(self.result)):
            if self.result[i]["Won"]:
                winners.append(self.qfinal[i])
        return winners
