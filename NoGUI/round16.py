class Round16():

    def __init__(self):
        
        self.round16 = []
        self.result = []


    def addteams(self,group):
        for team in group.winner():
            self.round16.append(team)
        self.result.append({"Goals":0,"Won":False})
    
    def addresult(self,team,goal,won):
        
        for i in range(len(self.round16)):
            if team.country_getter == self.round16[i].country_getter:
                self.result[i]["Goals"] = goal
                self.result[i]["Won"] = won
    
    def winners(self):

        winners = []
        for i in range(len(self.result)):
            if self.result[i]["Won"]:
                winners.append(self.round16[i])
        return winners

    def round_teams(self):
        return self.round16
