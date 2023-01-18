class thirdplace():

    def __init__(self):
        
        self.thirdplace = []
        self.result = []


    def addteams(self,sfinal):
        for team in sfinal.lossers():
            self.thirdplace.append(team)
            self.result.append({"Goals":0,"Won":False})
    
    def addresult(self,team,goal,won):
        for i in range(len(self.thirdplace)):
            if team.country_getter == self.thirdplace[i].country_getter:
                self.result[i]["Goals"] = goal
                self.result[i]["Won"] = won
    
    def winners(self):

        winners = []
        for i in range(len(self.result)):
            if self.result[i]["Won"]:
                winners.append(self.thirdplace[i])
        return winners