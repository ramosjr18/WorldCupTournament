class Group():

    """ 
        Constructor Method
    """
    def __init__(self, name):

        self._name = name
        self._group = {}
    
    """ add team method """
    
    def add_team(self,team):
        self._group[team.country_getter()] = [team,{"GF":0,"GA":0,"GD":0,"Pts":0}]
    
    def remove_team(self, team):
        self._group.pop(team.country_getter())

    def team_getter(self, team):
        return self._group[team][0]

    def add_goals_for(self, team, gf):
        self._group[team.country_getter()][1]["GF"] += gf
        self._group[team.country_getter()][1]["GD"] = self._group[team.country_getter()][1]["GF"] - self._group[team.country_getter()][1]["GA"]  
    
    def add_goals_goal(self, team, ga):
        self._group[team.country_getter()][1]["GA"] += ga
        self._group[team.country_getter()][1]["GD"] = self._group[team.country_getter()][1]["GF"] - self._group[team.country_getter()][1]["GA"]  
    
    def poinst(self):
        
        for key in self._group:
            self._group[key][1]["Pts"] = self._group[key][0].match_won_getter()*3 + self._group[key][0].match_drawed_getter()*1

    """ team info """

    def winner(self):
        
        winners = []
        winner1 = 0
        winner2 = 0


        for key in self._group:
            if self._group[key][1]["Pts"] > winner1:
                winner2 = winner1
                winner1 = self._group[key][1]["Pts"]

        for key in self._group:
            if self._group[key][1]["Pts"] == winner1:
                winners.append(key)
            if self._group[key][1]["Pts"] == winner2:
                winners.append(key)


        return winners

    def groupInfo(self):
        
        print(f"{self._name}")
        for value in self._group.values():
            print(value[0].print_information())
            for k,v in value[1].items():
                print(f"{k}: {v}")
            print()

        print(self._group)

    def groupTeams(self) -> dict:
        return self._group

    def groupName(self) -> str:
        return self._name
