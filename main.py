import gui
import team as tm
import group as grp
import round16 as rd
import qfinal as qf
import sfinal as sf
import final as fn
import random as rnd
import os
import customtkinter as ctk

#this function just creates the groups for the group fase
def create_groups() -> dict:
    groups = {"A": grp.Group("A"), "B": grp.Group("B"), "C": grp.Group("C"), "D": grp.Group("D"), "E": grp.Group("E"), "F": grp.Group("F"), "G": grp.Group("G"), "H": grp.Group("H")}
    return groups

#this assigns each team the user has given to a random group in an elegant way
#gotta love recursive functions
def get_random_group(groups) -> str:
    random_group = rnd.choice(list(groups.keys()))
    #the return checks if the group has already 4 groups in it so every groups has that limit
    return random_group if len(groups.get(random_group).groupTeams()) < 4 else get_random_group(groups)

#this functions acts as a medium taking the list of teams and the list of groups
def assign_random_team(teams, groups) -> None:
    for team in teams:
        try:
            random_group = get_random_group(groups)
        except:
            random_group = get_random_group(groups)
        groups.get(random_group).add_team(team)

#this method gets the input from the user to create the 32 teams
def add_teams_list(teams):
    #si, esto da un pequeño bug, pero por ahora funciona
    groups = []
    for i in range(0,len(teams),4):
        print(i)
        group = grp.Group(str(i))
        for j in range(4):
            new_team = tm.Team(teams[j+i])
            group.add_team(new_team)
        groups.append(group)
    
    return groups


if __name__ == "__main__":
    app = gui.App()
    app.mainloop()
