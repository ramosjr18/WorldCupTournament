class Final():

    def __init__(self):
        
        self.final = []
        self.result = []


    def addteams(self,sfinal):
        for team in sfinal.winners():
            self.final.append(team)
        self.result.append({"Goals":0,"Won":False})
    
    def addresult(self,team,goal,won):
        for i in range(len(self.final)):
            if team.country_getter() == self.final[i].country_getter():
                self.result[i]["Goals"] = goal
                self.result[i]["Won"] = won
    
    def winners(self):

        winners = []
        for i in range(len(self.result)):
            if self.result[i]["Won"]:
                winners.append(self.final[i])
        return winners
