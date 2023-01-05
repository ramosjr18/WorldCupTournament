import team
import group


germany = team.Team("Germany")
spain = team.Team("Spain")
colombia = team.Team("Colombia")
peru = team.Team("Peru")

groupA = group.Group("Group A")

groupA.add_team(spain)
groupA.add_team(colombia)
groupA.add_team(peru)
groupA.add_team(germany)



groupA.groupInfo()
