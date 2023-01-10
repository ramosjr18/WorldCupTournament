import team as tm
import group as grp
import round16 as rd
import qfinal as qf
import sfinal as sf
import final as fn
import random as rnd
import os

#this function just creates the groups for the group fase
def create_groups() -> dict:
    groups = {"group_A": grp.Group("A"), "group_B": grp.Group("B"), "group_C": grp.Group("C"), "group_D": grp.Group("D"), "group_E": grp.Group("E"), "group_F": grp.Group("F"), "group_G": grp.Group("G"), "group_H": grp.Group("H")}
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
        random_group = get_random_group(groups)
        groups.get(random_group).add_team(team)

#this method gets the input from the user to create the 32 teams
def add_teams_list(lst, groups, matches) -> None:
    while len(lst) < 32:
        new_team = input("Introduce the next team: ")
        if new_team == "exit" or new_team == "EXIT" or new_team == "Exit":
            print("I'll save this for later ;)")
            break
        #every new team is appended to a list
        elif new_team not in lst:
            new_country = tm.Team(new_team)
            lst.append(tm.Team(new_country))
            print("The team number ", len(lst), " has been added succesfully")
        else:
            print("This team is already in the list, you retard")
    #si, sé que es un bug, si el usuario se equivoca escribiendo el último equipo está pendejo y ya que lo mame
    if len(lst) == 32:
        assign_random_team(lst, groups)
        matches_per_group(groups, matches)


#this method generates the matches from the group phase
def generate_matches(group, matches) -> None:
    #the matches list saves the different matches combinations per group, each one has 6
    matches = []
    #used teams just makes sure a team doesn't play against itself and the matches don't repeat
    used_teams = []
    #gets a list of teams per group
    teams = group.groupTeams()
    for team in teams.keys():
        used_teams.append(team)
        for other in teams.keys():
            if other not in used_teams:
                matches.append(str(team.country_getter()) + " VS " + str(other.country_getter()))
            else:
                continue
    return matches

#this repeats the last method but for every group
def matches_per_group(groups, groups_matches) -> None:
    groups_matches = {}
    for group in groups:
        groups_matches[groups[group].groupName()] = generate_matches(groups[group])

#this method is meant to show the user the matches per group so the user can select the match and give the score
def select_group(groups_matches, group_name):
    for matches in range(groups_matches):
        print

def app() -> None:
    groups = create_groups()
    lst = []
    group_phase_matches = {}
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
            add_teams_list(lst, groups, group_phase_matches)
        elif select == "2":
            if len(lst) < 32:
                print("Finish entering the teams first, u dumbas")
            else:
                os.system('cls')
                print("Where we at?")
                print(" 1. Groups")
                select_2 = input("Option: ")
                if select_2 == "1":
                    print(" Select a group: ")
                    group_input = input(" A, B, C, D, E, F, G or H")
                    try:
                        select_group(group_phase_matches, group_input)
                    except:
                        print("that shit dont exist")
                        continue
                    
                    

        else:
            break
        os.system('cls')
    

app()