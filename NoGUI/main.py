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
def add_teams_list(lst, groups, matches) -> None:
    #si, esto da un pequeño bug, pero por ahora funciona
    names = []
    while len(lst) < 32:
        new_team = input("Introduce the next team: ")
        if new_team == "exit" or new_team == "EXIT" or new_team == "Exit":
            print("I'll save this for later ;)")
            break
        #every new team is appended to a list
        elif new_team not in names:
            names.append(new_team)
            new_country = tm.Team(new_team)
            lst.append(new_country)
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
                matches.append(str(team) + " VS " + str(other))
            else:
                continue
    return matches

#this repeats the last method but for every group
def matches_per_group(groups, groups_matches) -> None:
    for group in groups:
        groups_matches[groups[group].groupName()] = generate_matches(groups[group], groups_matches)

#this method is meant to show the user the matches per group so the user can select the match and give the score
def select_group(groups_matches, group_name) -> list:
    matches = []
    for match in groups_matches[group_name]:
        matches.append(match)
    return matches

def team_goals(groups, group, team_name, goals):
    team = groups[group].team_getter(team_name)
    groups[group].add_goals_for(team, goals)

def match_results(groups, group, team_a, team_b, goals_a, goals_b):
    #team_a y team_b son str, mientras que teamA y teamB son objetos Team
    teamA = groups[group].team_getter(team_a)
    teamB = groups[group].team_getter(team_b)
    groups[group].add_goals_for(teamA, goals_a)
    groups[group].add_goals_for(teamB, goals_b)
    if goals_a > goals_b:
        teamA.match_won_setter()
        teamB.match_lost_setter()
    elif goals_a < goals_b:
        teamA.match_lost_setter()
        teamB.match_won_setter()
    elif goals_a == goals_b:
        teamA.match_drawed_setter()
        teamB.match_drawed_setter()
    groups[group].points()


def app() -> None:
    #falta poner un try aquí porque a veces se putea la recursion
    groups = create_groups()
    #lst es la lista que contiene a los equipos
    lst = []
    group_phase_matches = {}
    octavos = rd.Round16()
    cuartos = qf.Qfinal()
    semi = sf.Sfinal()
    final = fn.Final()
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
                print(" 2. Round 16")
                print(" 3. Quarters")
                print(" 4. Semifinal")
                print(" 5. Final")
                select_2 = input("Option: ")
                if select_2 == "1":
                    print("Select a group: ")
                    group_input = input("   A, B, C, D, E, F, G or H: ").capitalize()
                    matches_temp = select_group(group_phase_matches, group_input)
                    os.system('cls')
                    print("Select a match:")
                    for index in range(len(matches_temp)):
                        print(index + 1, matches_temp[index])
                    match_input = input("Option: ")
                    print("Introduce the score:")
                    team_a = matches_temp[int(match_input)][: matches_temp[int(match_input)].find("VS")].strip()
                    team_b = matches_temp[int(match_input)][matches_temp[int(match_input)].find("VS") + 2:].strip()
                    score_input_A = int(input(team_a + ": "))
                    score_input_B = int(input(team_b + ": "))
                    match_results(groups, group_input, team_a, team_b, score_input_A, score_input_B)
                    os.system('cls')
                    print("Is this the last group phase match?")
                    last_match = input("Y/N: ").strip()
                    if last_match == "Y" or last_match == "y":
                        for group in groups.values():
                            # group.winners()
                            octavos.addteams(group)
                    else:
                        continue
                if select_2 == "2":
                    print("Introduce a score: ")
                    #no tengo tiempo de hacerlo mas bonito y elegante, tons se aguantan
                    length = len(octavos.round_teams())
                    for i in range(length / 2):
                        print(i, ".", octavos.round_teams()[i].country_getter(), "VS", octavos.round_teams()[length - i - 1].country_getter())
                    match_input = input("Option: ")
                    if match_input == "1":
                        goals_a = input(octavos.round_teams[0].country_getter(), ":")
                        goals_b = input(octavos.round_teams[15].country_getter(), ":")
                        octavos.addresult(octavos.round_teams[0], int(goals_a), True if goals_a > goals_b else False)
                        octavos.addresult(octavos.round_teams[15], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "2":
                        goals_a = input(octavos.round_teams[1].country_getter(), ":")
                        goals_b = input(octavos.round_teams[14].country_getter(), ":")
                        octavos.addresult(octavos.round_teams[1], int(goals_a), True if goals_a > goals_b else False)
                        octavos.addresult(octavos.round_teams[14], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "3":
                        goals_a = input(octavos.round_teams[2].country_getter(), ":")
                        goals_b = input(octavos.round_teams[13].country_getter(), ":")
                        octavos.addresult(octavos.round_teams[2], int(goals_a), True if goals_a > goals_b else False)
                        octavos.addresult(octavos.round_teams[13], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "4":
                        goals_a = input(octavos.round_teams[3].country_getter(), ":")
                        goals_b = input(octavos.round_teams[12].country_getter(), ":")
                        octavos.addresult(octavos.round_teams[3], int(goals_a), True if goals_a > goals_b else False)
                        octavos.addresult(octavos.round_teams[12], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "5":
                        goals_a = input(octavos.round_teams[4].country_getter(), ":")
                        goals_b = input(octavos.round_teams[11].country_getter(), ":")
                        octavos.addresult(octavos.round_teams[4], int(goals_a), True if goals_a > goals_b else False)
                        octavos.addresult(octavos.round_teams[11], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "6":
                        goals_a = input(octavos.round_teams[5].country_getter(), ":")
                        goals_b = input(octavos.round_teams[10].country_getter(), ":")
                        octavos.addresult(octavos.round_teams[5], int(goals_a), True if goals_a > goals_b else False)
                        octavos.addresult(octavos.round_teams[10], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "7":
                        goals_a = input(octavos.round_teams[6].country_getter(), ":")
                        goals_b = input(octavos.round_teams[9].country_getter(), ":")
                        octavos.addresult(octavos.round_teams[6], int(goals_a), True if goals_a > goals_b else False)
                        octavos.addresult(octavos.round_teams[9], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "8":
                        goals_a = input(octavos.round_teams[7].country_getter(), ":")
                        goals_b = input(octavos.round_teams[8].country_getter(), ":")
                        octavos.addresult(octavos.round_teams[7], int(goals_a), True if goals_a > goals_b else False)
                        octavos.addresult(octavos.round_teams[8], int(goals_b), True if goals_a < goals_b else False)
                    os.system('cls')
                    print("Is this the last group phase match?")
                    last_match = input("Y/N: ").strip()
                    if last_match == "Y" or last_match == "y":
                        octavos.winners()
                        cuartos.addteams(octavos)
                    else:
                        continue
                if select_2 == "3":
                    print("Introduce a score: ")
                    length = len(cuartos.round_teams())
                    for i in range(length / 2):
                        print(i, ".", cuartos.round_teams()[i].country_getter(), "VS", cuartos.round_teams()[length - i - 1].country_getter())
                    match_input = input("Option: ")
                    if match_input == "1":
                        goals_a = input(cuartos.round_teams[0].country_getter(), ":")
                        goals_b = input(cuartos.round_teams[7].country_getter(), ":")
                        cuartos.addresult(cuartos.round_teams[0], int(goals_a), True if goals_a > goals_b else False)
                        cuartos.addresult(cuartos.round_teams[7], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "2":
                        goals_a = input(cuartos.round_teams[1].country_getter(), ":")
                        goals_b = input(cuartos.round_teams[6].country_getter(), ":")
                        cuartos.addresult(cuartos.round_teams[1], int(goals_a), True if goals_a > goals_b else False)
                        cuartos.addresult(cuartos.round_teams[6], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "3":
                        goals_a = input(cuartos.round_teams[2].country_getter(), ":")
                        goals_b = input(cuartos.round_teams[5].country_getter(), ":")
                        cuartos.addresult(cuartos.round_teams[2], int(goals_a), True if goals_a > goals_b else False)
                        cuartos.addresult(cuartos.round_teams[5], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "4":
                        goals_a = input(cuartos.round_teams[3].country_getter(), ":")
                        goals_b = input(cuartos.round_teams[4].country_getter(), ":")
                        cuartos.addresult(cuartos.round_teams[3], int(goals_a), True if goals_a > goals_b else False)
                        cuartos.addresult(cuartos.round_teams[4], int(goals_b), True if goals_a < goals_b else False)
                    os.system('cls')
                    print("Is this the last group phase match?")
                    last_match = input("Y/N: ").strip()
                    if last_match == "Y" or last_match == "y":
                        cuartos.winners()
                        semi.addteams(cuartos)
                    else:
                        continue
                if select_2 == "4":
                    print("Introduce a score: ")
                    length = len(semi.round_teams())
                    for i in range(length / 2):
                        print(i, ".", semi.round_teams()[i].country_getter(), "VS", semi.round_teams()[length - i - 1].country_getter())
                    match_input = input("Option: ")
                    if match_input == "1":
                        goals_a = input(semi.round_teams[0].country_getter(), ":")
                        goals_b = input(semi.round_teams[3].country_getter(), ":")
                        semi.addresult(semi.round_teams[0], int(goals_a), True if goals_a > goals_b else False)
                        semi.addresult(semi.round_teams[3], int(goals_b), True if goals_a < goals_b else False)
                    if match_input == "2":
                        goals_a = input(semi.round_teams[1].country_getter(), ":")
                        goals_b = input(semi.round_teams[2].country_getter(), ":")
                        semi.addresult(semi.round_teams[1], int(goals_a), True if goals_a > goals_b else False)
                        semi.addresult(semi.round_teams[2], int(goals_b), True if goals_a < goals_b else False)
                    os.system('cls')
                    print("Is this the last group phase match?")
                    last_match = input("Y/N: ").strip()
                    if last_match == "Y" or last_match == "y":
                        semi.winners()
                        final.addteams(semi)
                    else:
                        continue
                if select_2 == "5":
                    print("Introduce the score: ")
                    goals_a = input(final.round_teams[0].country_getter(), ":")
                    goals_b = input(final.round_teams[1].country_getter(), ":")
                    final.addresult(final.round_teams[0], int(goals_a), True if goals_a > goals_b else False)
                    final.addresult(final.round_teams[1], int(goals_b), True if goals_a < goals_b else False)
                    final.winners()
                    os.system('cls')
                    print("The winner is:", final.winners()[0])
        else:
            break
        #os.system('cls')
    

app()
