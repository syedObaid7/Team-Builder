import random

# Skill is based on 3 factors - (Overall, Offence, Defence)
playerSkill = {}

# Player names
players = ['zaid', 'obaid', 'umair',
           'hammad', 'fawaad', 'shobi']#, 'nouman', 'rayan', 'hassu', 'hamza', 'zuhair', 'musa',
         #  'zohaib']

# This bool checks if the teams are equal
flag = True

team = None


class Team:
    def __init__(self, overall=0, offence=0, defence=0, a=0):
        self.overall = overall
        self.offence = offence
        self.defence = defence
        self.a = a

    def calc_overall(self, a):
        for i in range(len(a)):
            self.overall += playerSkill.get(str(a[i]))[0]

    def calc_offence(self, a):
        for i in range(len(a)):
            self.offence += playerSkill.get(str(a[i]))[1]

    def calc_defence(self, a):
        for i in range(len(a)):
            self.defence += playerSkill.get(str(a[i]))[2]

    def print(self, a):
        self.a = a


# -------------------------------------------------------------------------------#
print(
    "This program will take in the skill scores of each player and "
    "sort any number of teams based on their skill level\nPlease follow the on screen instructions")
# Skills should be entered on a scale of 1-10
for i in range(len(players)):
    temp1 = [int(input("Enter the overall for " + players[i] + " (1-10) ")),
             int(input("Enter the offence for " + players[i] + " (1-10) ")),
             int(input("Enter the defence for " + players[i] + " (1-10) "))]

    playerSkill.update({players[i]: temp1})

while flag:
    playerNum = len(players)
    teamNum = int(input("Enter the number of teams "))
    team = [Team() for i in range(teamNum)]

    while playerNum > 0 and teamNum > 0:
        temp2 = random.sample(players, int(playerNum / teamNum))
        team[teamNum - 1].calc_overall(temp2)
        team[teamNum - 1].calc_offence(temp2)
        team[teamNum - 1].calc_defence(temp2)
        team[teamNum - 1].print(temp2)

        for i in temp2:
            players.remove(i)

        playerNum -= int(playerNum / teamNum)
        teamNum -= 1

    for i in range(len(team) - 1):
        flag = False
        flag1 = False
        flag2 = False
        flag3 = False

        if team[i].overall - team[i + 1].overall > 5:
            flag1 = True
        if team[i].offence - team[i + 1].offence > 5:
            flag2 = True
        if team[i].defence - team[i + 1].defence > 5:
            flag3 = True

        if flag1 and (flag2 or flag3) or (flag2 and flag3):
            print("Teams are not balanced")
            flag = True
            break

print("These teams are equal")
for i in team:
    print(i.a)
