#finalprojectprogramming

'''
1. Crear la clase para los equipos, grupos, ronda 16, qfinal, sfinal, final
2. crear objetos de los 32 equipos y asignar a los grupos de objetos 
3. auto generar los equipos que pasan de fase de grupos 
4. hacer sistema para que el usuario ponga los resultados 
5. el programa debe mostrar los resultados de todos los partidos del torneo
6. crear el Gui para 10 puntos extra
'''

rounds16 = []
qfinal = []

#defining class para team 
class Team():

    points = 0
    matches_played = 0
    win = 0
    draw = 0
    loss = 0
    goals_for = 0
    goals_against = 0
    goals_difference = 0
    
    def _init_(self, country):
        self.country = country

    def _lt_(self, other):
        if(self.points == other.points):
            if(self.goals_difference == other.goals_difference):
                return self.goals_for > other.goals_for
            else:
                return self.goals_difference > other.goals_difference
        else: 
            return self.points > other.points
    
    def addMatch (self, gf, ga):
        self.matches_played += 1
        self.goals_for += gf
        self.goals_against += ga
        
        result = gf -ga
        self.goals_difference = self.goals_difference + result 

        if (result > 0):
            self.win += 1
            self.points += 3

        if (result == 0):
            self.draw += 1
            self.points += 1

        if (result < 0):
            self.loss += 1

    def setDetails (self, p, mp, w, d, l, gf, ga, gd):
         self.points = p
         self.matches_played = mp
         self.win = w
         self.draw = d
         self.loss = l
         self.goals_for = gf
         self.goals_against = ga
         self.goals_difference = gd

    def showDetails (self):
        return print (self.country, '\n MP:', self.matches_played, 'W: ', self.win, 'D: ', self.draw, 'L: ', self.loss, 'GF: ', self.goals_for, 'GA: ', self.goals_against)
    
    def showDetails2 (self):
        return print(self.country, '\n', self.matches_played, self.win, self.draw, self.loss, self.goals_for, self.goals_against, self.goals_difference, self.points)



# defining class for group 
class Group ():
    winner_1 = None
    winner_2 = None

    def _init_(self, group_name, team1, team2, team3, team4):
        self.group_name = group_name
        self.team1 = team1
        self.team2 = team2
        self.team3 = team3
        self.team4 = team4

    def showGroup(self):
        print(self.group_name, ": ", self.team1.country, ", ", self.team2.country, ", ", self.team3.country, ", ", self.team4.country)

    def showGroupTeams (self):
        self.team1.showDetails()
        self.team2.showDetails()
        self.team3.showDetails()
        self.team4.showDetails()

    def showGroupTeams2(self):
        self.team1.showDetails2()
        self.team2.showDetails2()
        self.team3.showDetails2()
        self.team4.showDetails2()

#REVISAR ESTO 
    def closeGroup(self):
        list = [self.team4, self.team1, self.team3, self.team2]
        list.sort()
        self.winner_1 = list[0]
        self.winner_2 = list [1]
        return print(self.group_name, "winners: ", list[0].country, "and ", list[1].country)

# defining class for fasedegrupos
class Round16():

    round_winner = None

    def _init_(self, team1, team2):
        self.team1 = team1 
        self.team2 = team2
    
    def showRound(self):
        return print("Round 16 teams: ", self.team1.country, self.team2.country)

    def closeRound(self):
        list= [self.team1, self.team2]
        list.sort()
        self.round_winner = list[0]
        return print("Round 16 between: ", self.team1.country, "and ", self.team2.country, "-winner: ", self.round_winner.country)

# defining class for cuartosdefinal
class QuarterFinal():
    def _init_(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def showRound(self):
        return print("Quarter-finals teams: ", self.team1.country, self.team2.country)
    
    def closeRound(self):
        list= [self.team1, self.team2]
        list.sort()
        self.round_winner = list[0]
        return print("Quarter-finals between: ", self.team1.country, "and ", self.team2.country, "-winner: ", self.round_winner.country)


#matchFunctions
def addMatch(team_1, team_2, team1_goals, team2_goals):

    def checkTeam(team):
        if (isinstance(team,Team)):
            return True
        else:
            print("ERROR")
            return False
    def checkScore(score):
        if (isinstance(score, int)):
            if (score >= 0):
                return True
            else: 
                print("ERROR")
            return False
        else: 
            print("ERROR")
            return False

    if(checkTeam(team_1) == False):
        return
    if(checkTeam(team_2) == False):
        return    

    if(checkScore(team1_goals) == False):
        return
    if(checkScore(team2_goals) == False):
        return

    team_1.addMatch(team1_goals, team2_goals)
    team_2.addMatch(team2_goals, team1_goals)

#def los equipos
netherlands = Team ("Netherlands")
senegal = Team("Senegal")
ecuador = Team("Ecuador")
qatar = Team("Qatar")

england = Team("England")
usa = Team("USA")
iran = Team("Iran")
wales = Team("Wales")

argentina = Team("Argentina")
poland = Team("Poland")
mexico = Team("Mexico")
saudi_arabia = Team("Saudi Arabia")

france = Team("France")
australia = Team("Australia")
tunisia = Team("Tunisia")
denmark = Team("Denmark")

japan = Team("Japan")
spain = Team("Spain")
germany = Team("Germany")
costa_rica = Team("Costa Rica")

morocco = Team("Morocco")
croatia = Team("Croatia")
belgium = Team("Belgium")
canada = Team("Canada")

brazil = Team("Brazil")
switzerland = Team("Switzerland")
cameroon = Team("Cameroon")
serbia = Team("Serbia")

portugal = Team("Portugal")
south_korea = Team("South Korea")
uruguay = Team("Uruguay")
ghana = Team("Ghana")

#asignar los equipos a grupos
group_A = Group["Group A", netherlands, senegal, ecuador, qatar]
group_B = Group["Group B", england, usa, iran, wales]
group_C = Group["Group C", argentina, poland, mexico,saudi_arabia]
group_D = Group["Group D", france, australia, tunisia, denmark]
group_E = Group["Group E", japan, spain, germany, costa_rica]
group_F = Group["Group F", morocco, croatia, belgium, canada]
group_G = Group["Group G", brazil, switzerland, cameroon, serbia]
group_H = Group["Group H", portugal, south_korea, uruguay, ghana]

#ver los grupos
group_A.showGroup();
group_B.showGroup();
group_C.showGroup();
group_D.showGroup();
group_E.showGroup();
group_F.showGroup();
group_G.showGroup();
group_H.showGroup();

group_A.showGroupTeams();
group_B.showGroupTeams();
group_C.showGroupTeams();
group_D.showGroupTeams(); 
group_E.showGroupTeams();
group_F.showGroupTeams();
group_G.showGroupTeams();
group_H.showGroupTeams();


#asignar matches de los grupos 
#grupo A
addMatch(netherlands, senegal, 2, 0)
addMatch(netherlands, ecuador, 1, 1)
addMatch(netherlands, qatar, 2, 0)
addMatch(senegal, ecuador, 2, 1)
addMatch(senegal, qatar, 3, 1)
addMatch(ecuador, qatar, 2, 0)

group_A.closeGroup()

#grupo B
addMatch(england, iran, 6, 2)
addMatch(england, usa, 0, 0)
addMatch(england, wales, 3, 0)
addMatch(iran, usa, 0, 1)
addMatch(iran, wales, 2, 0)
addMatch(wales, usa, 1, 1)

group_B.closeGroup()

#group C
addMatch(argentina, poland, 2, 0)
addMatch(argentina, mexico, 2, 0)
addMatch(argentina, saudi_arabia, 1, 2)
addMatch(poland, mexico, 0, 0)
addMatch(poland, saudi_arabia, 2, 0)
addMatch(mexico, saudi_arabia, 2, 1)

group_C.closeGroup()

#group D
addMatch(france, australia, 4, 1)
addMatch(france, tunisia, 0, 1)
addMatch(france, denmark, 2, 1)
addMatch(australia, tunisia, 1, 0)
addMatch(australia, denmark, 1, 0)
addMatch(tunisia, denmark, 0, 0)

group_D.closeGroup()

#group E
addMatch(japan, spain, 2, 1)
addMatch(japan, germany, 2, 1)
addMatch(japan, costa_rica, 0, 1)
addMatch(spain, germany, 1, 1)
addMatch(spain, costa_rica, 7, 0)
addMatch(germany, costa_rica, 4, 2)

group_E.closeGroup()

#group F
addMatch(morocco, croatia, 0, 0)
addMatch(morocco, belgium, 2, 0)
addMatch(morocco, canada, 2, 1)
addMatch(croatia, belgium, 0, 0)
addMatch(croatia, canada, 4, 1)
addMatch(belgium, canada, 1, 0)

group_F.closeGroup()

#group G 
addMatch(brazil, switzerland, 1, 0)
addMatch(brazil, cameroon, 0, 1)
addMatch(brazil, serbia, 2, 0)
addMatch(switzerland, cameroon, 1, 0)
addMatch(switzerland, serbia, 3, 2)
addMatch(cameroon, serbia, 3, 3)

group_G.closeGroup()

#group H
addMatch(portugal, south_korea, 1, 2)
addMatch(portugal, uruguay, 2, 0)
addMatch(portugal, ghana, 3, 2)
addMatch(south_korea, uruguay, 0, 0)
addMatch(south_korea, ghana, 2, 3)
addMatch(uruguay, ghana, 2, 0)

group_H.closeGroup()


#asignar winner de cada group 
round16_1 = Round16 (group_A.winner_1, group_B.winner_2)
round16_2 = Round16 (group_C.winner_1, group_D.winner_2)
round16_3 = Round16 (group_E.winner_1, group_F.winner_2)
round16_4 = Round16 (group_G.winner_1, group_H.winner_2)
round16_5 = Round16 (group_B.winner_1, group_A.winner_2)
round16_6 = Round16 (group_D.winner_1, group_C.winner_2)
round16_7 = Round16 (group_F.winner_1, group_E.winner_2)
round16_8 = Round16 (group_H.winner_1, group_G.winner_2)

print(group_A.winner_1.country)

#asignar matches
addMatch(round16_1.team1, round16_1.team2, 3, 1)
addMatch(round16_2.team1, round16_2.team2, 2, 1)
addMatch(round16_3.team1, round16_3.team2, 1, 3)
addMatch(round16_4.team1, round16_4.team2, 4, 1)
addMatch(round16_5.team1, round16_5.team2, 3, 1)
addMatch(round16_6.team1, round16_6.team2, 3, 0)
addMatch(round16_7.team1, round16_7.team2, 3, 0)
addMatch(round16_8.team1, round16_8.team2, 6, 1)

#closing round16
round16_1.closeRound()
round16_2.closeRound()
round16_3.closeRound()
round16_4.closeRound()
round16_5.closeRound()
round16_6.closeRound()
round16_7.closeRound()
round16_8.closeRound()

#asignar teams to cuartos
qfinal_1 = QuarterFinal(round16_1.round_winner, round16_2.round_winner)
qfinal_2 = QuarterFinal(round16_3.round_winner, round16_4.round_winner)
qfinal_3 = QuarterFinal(round16_5.round_winner, round16_6.round_winner)
qfinal_4 = QuarterFinal(round16_7.round_winner, round16_8.round_winner)

addMatch(qfinal_1.team1, qfinal_1.team2, 3, 4)
addMatch(qfinal_2.team1, qfinal_2.team2, 4, 2)
addMatch(qfinal_3.team1, qfinal_3.team2, 2, 1)
addMatch(qfinal_4.team1, qfinal_4.team2, 1, 0)

#closing qfinal
qfinal_1.closeRound()
qfinal_2.closeRound()
qfinal_3.closeRound()
qfinal_4.closeRound()





















#DEFINIR LA CLASS PARA TEAM
class Team:
    
    """
        Constructor 
    """
    
    def __init__(self, country):
        
        # Initializing Team Values

        self._country = country
        self._match_Played = 0 
        self._match_won = 0
        self._match_drawed = 0
        self._match_lost = 0

    """ Setters"""

    def match_won_setter(self):

        self._match_won += 1
        self._match_Played += 1

    def match_drawed_setter(self):

        self._match_drawed += 1
        self._match_Played += 1

    def match_lost_setter(self):

        self._match_lost += 1
        self._match_Played += 1

    
    """ getters """

    def country_getter(self):
        
        return self._country

    def match_Played_getter(self):
        
        return self._match_Played

    def match_won_getter(self):
        
        return self._match_won

    def match_drawed_getter(self):
        
        return self._match_drawed

    def match_lost_getter(self):
        
        return self._match_lost

    """ information methods"""

    def __str__(self) -> str:
        return f"Country: {self.country_getter()}\nmp: {self.match_Played_getter()}\nw: {self.match_won_getter()}\nD: {self.match_drawed_getter()}\nL: {self.match_lost_getter()}"

    def print_information(self):
        print(self)



#DEFINIR LA CLASS PARA GROUP
class Group():

    """ 
        Constructor Method
    """
    def __init__(self, name):

        self._name = name
        self._group = {}
    
    """ add team method """
    
    def add_team(self,team):
        self._group[team.country_getter] = [team,{"GF":0,"GA":0,"GD":0,"Pts":0}]
    
    def remove_team(self, team):
        self._group.pop(team.country_getter)

    def add_goals_for(self, team, gf):
        self._group[team.country_getter][1]["GF"] += gf
        self._group[team.country_getter][1]["GD"] = self._group[team.country_getter][1]["GF"] - self._group[team.country_getter][1]["GA"]  
    
    def add_goals_goal(self, team, ga):
        self._group[team.country_getter][1]["GA"] += ga
        self._group[team.country_getter][1]["GD"] = self._group[team.country_getter][1]["GF"] - self._group[team.country_getter][1]["GA"]  
    
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

    def groupTeams(self):
        return self._group





#DEFINIR CLASS PARA FASE DE GRUPOS 
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





#DEFINIR CLASS PARA CUARTOS 
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
            if team.country_getter == self.qfinal[i].country_getter:
                self.result[i]["Goals"] = goal
                self.result[i]["Won"] = won
    
    def winners(self):

        winners = []
        for i in range(len(self.result)):
            if self.result[i]["Won"]:
                winners.append(self.qfinal[i])
        return winners


