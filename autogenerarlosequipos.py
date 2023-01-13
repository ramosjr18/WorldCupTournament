# Lista de equipos
teams = ["Netherlands", "Senegal", "Ecuador", "Qatar", "England", "Usa", "Iran", "Wales", "Argentina", "Poland", "Mexico", "Saudi arabia", "France", "Australia", "Tunisia", "Denmark", "Japan", "Spain", "Germany", "Costa Rica", "Morocco", "Croatia", "Belgium", "Canada", "Brazil", "Switzerland", "Cameroon", "Serbia", "Portugal", "South Korea", "Uruguay", "Ghana"]


# Botón "autogenerar"
def autogenerar():

    group_A = []
    group_B = []
    group_C = []
    group_D = []
    group_E = []
    group_F = []
    group_G = []
    group_H = []


    for team in teams:

        if team in ["Netherlands", "Senegal", "Ecuador", "Qatar"]:
        # Agregamos el elemento al grupo A
            group_A.append(team)

        if team in ["England", "Usa", "Iran", "Wales"]:
            group_B.append(team)

        if team in ["Argentina", "Poland", "Mexico", "Saudi arabia"]:
            group_C.append(team)

        if team in ["France", "Australia", "Tunisia", "Denmark"]:
            group_D.append(team)

        if team in ["Japan", "Spain", "Germany", "Costa Rica"]:
            group_E.append(team)

        if team in ["Morocco", "Croatia", "Belgium", "Canada"]:
            group_F.append(team)

        if team in ["Brazil", "Switzerland", "Cameroon", "Serbia"]:
            group_G.append(team)
        
        if team in ["Portugal", "South Korea", "Uruguay", "Ghana"]:
            group_H.append(team)

# Imprimimos los grupos y sus elementos
    print("Group A:", group_A)
    print("Group B:", group_B)
    print("Group C:", group_C)
    print("Group D:", group_D)
    print("Group E:", group_E)
    print("Group F:", group_F)
    print("Group G:", group_G)
    print("Group H:", group_H)

autogenerar()