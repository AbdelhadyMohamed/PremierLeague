def match_update(team1, team2, team1_goals, team2_goals):
    if team1_goals > team2_goals:
        team1.win(team1_goals, team2_goals)
        team2.lose(team2_goals, team1_goals)
    elif team1_goals == team2_goals:
        team1.draw()
        team2.draw()
    elif team1_goals < team2_goals:
        team1.lose(team1_goals, team2_goals)
        team2.win(team2_goals, team1_goals)


class Team:
    def __init__(self, team_name, current_rank, matches_played, wins, draws, losses, goals_forward, goals_against,
                 points):
        self.team_name = team_name
        self.current_rank = current_rank
        self.matches_played = matches_played
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goals_forward = goals_forward
        self.goals_against = goals_against
        self.points = points

    def win(self, goals_scored, goals_received):
        self.points = self.points + 3
        self.goals_forward = goals_scored
        self.goals_against = goals_received

    def draw(self, goals_scored, goals_received):
        self.points = self.points + 1
        self.goals_forward = goals_scored
        self.goals_against = goals_received

    def lose(self, goals_scored, goals_received):
        self.points = self.points + 0
        self.goals_forward = goals_scored
        self.goals_against = goals_received


class Table:
    def __init__(self):
        self.teams = teams

    def get_teams(self):
        print(self.teams)

    def rank_teams(self):
        for i in range(len(self.teams) - 1):
            for j in range(len(self.teams) - i - 1):
                if self.teams[j].points < self.teams[j + 1].points:
                    self.teams[j], self.teams[j + 1] = self.teams[j + 1], self.teams[j]
                elif self.teams[j].points == self.teams[j + 1].points:
                    if self.teams[j].goals_forward - self.teams[j].goals_against < self.teams[j + 1].goals_forward - \
                            self.teams[j + 1].goals_against:
                        self.teams[j], self.teams[j + 1] = self.teams[j + 1], self.teams[j]
                    elif self.teams[j].goals_forward - self.teams[j].goals_against == self.teams[j + 1].goals_forward - \
                            self.teams[j + 1].goals_against:
                        if self.teams[j].goals_forward < self.teams[j + 1].goals_forward:
                            self.teams[j], self.teams[j + 1] = self.teams[j + 1], self.teams[j]
        for i in range(len(self.teams)):
            self.teams[i].current_rank = i+1

        print("season 2023-24")
        print("Club,        MP,W,D,L,GF,GA,PTS")
        for team in self.teams:
            print(team.current_rank, team.team_name, team.matches_played, team.wins, team.draws, team.losses,
                  team.goals_forward, team.goals_against, team.points)
        print("")


Bournemouth = Team("Bournemouth", 0, 0, 0, 0, 0, 0, 0, 0)
Arsenal = Team("Arsenal", 0, 0, 0, 0, 0, 0, 0, 0)
Aston_Villa = Team("Aston Villa", 0, 0, 0, 0, 0, 0, 0, 0)
Brentford = Team("Brentford", 0, 0, 0, 0, 0, 0, 0, 0)
Brighton = Team("Brighton", 0, 0, 0, 0, 0, 0, 0, 0)
Burnley = Team("Burnley", 0, 0, 0, 0, 0, 0, 0, 0)
Chelsea = Team("Chelsea", 0, 0, 0, 0, 0, 0, 0, 0)
Crystal_Palace = Team("Crystal Palace", 0, 0, 0, 0, 0, 0, 0, 0)
Everton = Team("Everton", 0, 0, 0, 0, 0, 0, 0, 0)
Fulham = Team("Fulham", 0, 0, 0, 0, 0, 0, 0, 0)
Liverpool = Team("Liverpool", 0, 0, 0, 0, 0, 0, 0, 0)
Luton_Town = Team("Luton Town", 0, 0, 0, 0, 0, 0, 0, 0)
Manchester_City = Team("Manchester City", 0, 0, 0, 0, 0, 0, 0, 0)
Manchester_United = Team("Manchester United", 0, 0, 0, 0, 0, 0, 0, 0)
Newcastle = Team("Newcastle", 0, 0, 0, 0, 0, 0, 0, 0)
Nottem_Forest = Team("Nottem Forest", 0, 0, 0, 0, 0, 0, 0, 0)
Sheffield_United=Team("Sheffield United", 0, 0, 0, 0, 0, 0, 0, 0)
Tottenham = Team("Tottenham", 0, 0, 0, 0, 0, 0, 0, 0)
West_Ham = Team("West Ham", 0, 0, 0, 0, 0, 0, 0, 0)
Wloves = Team("Wloves", 0, 0, 0, 0, 0, 0, 0, 0)
teams = [Bournemouth, Arsenal, Aston_Villa, Brentford, Brighton, Burnley, Chelsea, Crystal_Palace, Everton, Fulham,
         Liverpool,
         Luton_Town, Manchester_City, Manchester_United, Newcastle, Nottem_Forest,Sheffield_United ,Tottenham, West_Ham, Wloves]

Table1 = Table()
Table1.rank_teams()
Table1.rank_teams()
match_update(Manchester_City, Manchester_United, 6, 3)
