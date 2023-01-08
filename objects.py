import random
import team as tm
import group as gp


def assign_group(groups, country):
    while True:
        index = random.randint(0, 7)
        if len(groups[index].groupTeams()) < 4:
            groups[index].add_team(country)
            break

def create_team(groups, country):
    country_team = tm.Team(country)
    assign_group(groups, country_team)

def input_team(groups, countries):
    while True:
        new_country = input()
        if new_country not in countries:
            countries.append(new_country)
            create_team(groups, new_country)
            break
        else:
            print("the country has already been assigned to a group")

def main():
    groups = [gp.Group["A"], gp.Group["B"], gp.Group["C"], gp.Group["D"], gp.Group["E"], gp.Group["F"], gp.Group["G"], gp.Group["H"]]
    countries = []
    while len(countries) < 32:
        print("Introduce the country number ", len(countries) + 1, ":")
        input_team(groups, countries)

main()