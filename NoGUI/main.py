import team as tm
import group as grp
import round16 as rd
import qfinal as qf
import sfinal as sf
import final as fn
import random as rnd
import os

def create_groups() -> dict:
    groups = {"group_A": grp.Group("A"), "group_B": grp.Group("B"), "group_C": grp.Group("C"), "group_D": grp.Group("D"), "group_E": grp.Group("E"), "group_F": grp.Group("F"), "group_G": grp.Group("G"), "group_H": grp.Group("H")}
    return groups

def get_random_group(groups) -> str:
    random_group = rnd.choice(list(groups.keys()))
    return random_group if len(groups.get(random_group).groupTeams()) < 4 else get_random_group(groups)

def assign_random_team(teams, groups) -> None:
    for team in teams:
        random_group = get_random_group(groups)
        groups.get(random_group).add_team(team)

def add_teams_list(lst, groups) -> None:
    while len(lst) < 32:
        new_team = input("Introduce the next team: ")
        if new_team == "exit" or new_team == "EXIT" or new_team == "Exit":
            print("I'll save this for later ;)")
            break
        elif new_team not in lst:
            new_country = tm.Team(new_team)
            lst.append(tm.Team(new_country))
            print("The team number ", len(lst), " has been added succesfully")
        else:
            print("This team is already in the list, you retard")
    #si, sé que es un bug, si el usuario se equivoca escribiendo el último equipo está pendejo y ya que lo mame
    if len(lst) == 32:
        assign_random_team(lst, groups)

def generate_matches(group) -> list:
    matches = []
    used_teams = []
    teams = group.groupTeams()
    for team in teams.keys():
        used_teams.append(team)
        for other in teams.keys():
            if other not in used_teams:
                matches.append(str(team.country_getter()) + " VS " + str(other.country_getter()))
            else:
                continue
    return matches

def matches_per_group(groups) -> dict:
    groups_matches = {}
    for group in groups:
        groups_matches[groups[group].groupName()] = generate_matches(groups[group])
    return groups_matches


def app() -> None:
    groups = create_groups()
    lst = []
    while True:
        print("Choose wisely:")
        if not lst:
            print(" 1. Create the teams list.")
        elif len(lst) == 32:
            print("you completed this part already")
        else:
            print(" 1. Continue with the teams list where you left.")
        print(" 2. Introduce a score.")
        print(" 3. Remove a team cos u stupid and wrote it wrong")
        print(" 4. Exit")
        
        select = input("Option: ")
        if select == "1":
            add_teams_list(lst, groups)
        elif select == "2":
            if len(lst) < 32:
                print("Finish entering the teams first, u dumbas")
            else:
                os.system('cls')
                print("Where we at?")
                print(" 1. Groups")
                select_2 = input("Option: ")
                if select_2 == "1":
                    print(matches_per_group(groups))
                    break
        else:
            break
        os.system('cls')
    

app()