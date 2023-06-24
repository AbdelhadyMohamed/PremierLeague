from tkinter import *
from tkinter import ttk


def play_match(team1, team2, team1_goals, team2_goals):
    if team1_goals > team2_goals:
        team1.win(team1_goals, team2_goals)
        team2.lose(team2_goals, team1_goals)
    elif team1_goals == team2_goals:
        team1.draw(team1_goals, team1_goals)
        team2.draw(team1_goals, team1_goals)
    elif team1_goals < team2_goals:
        team1.lose(team1_goals, team2_goals)
        team2.win(team2_goals, team1_goals)
    Table1.rank_teams()


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
        self.goals_forward = +goals_scored
        self.goals_against = +goals_received
        self.matches_played = +1
        self.wins = +1

    def draw(self, goals_scored, goals_received):
        self.points = self.points + 1
        self.goals_forward = +goals_scored
        self.goals_against = +goals_received
        self.matches_played = +1
        self.draws = +1

    def lose(self, goals_scored, goals_received):
        self.points = self.points + 0
        self.goals_forward = +goals_scored
        self.goals_against = +goals_received
        self.matches_played = +1
        self.losses = +1


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
            self.teams[i].current_rank = i + 1

        return self.teams


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
Sheffield_United = Team("Sheffield United", 0, 0, 0, 0, 0, 0, 0, 0)
Tottenham = Team("Tottenham", 0, 0, 0, 0, 0, 0, 0, 0)
West_Ham = Team("West Ham", 0, 0, 0, 0, 0, 0, 0, 0)
Wloves = Team("Wloves", 0, 0, 0, 0, 0, 0, 0, 0)
teams = [Bournemouth, Arsenal, Aston_Villa, Brentford, Brighton, Burnley, Chelsea, Crystal_Palace, Everton, Fulham,
         Liverpool,
         Luton_Town, Manchester_City, Manchester_United, Newcastle, Nottem_Forest, Sheffield_United, Tottenham,
         West_Ham, Wloves]

Table1 = Table()
play_match(Wloves, West_Ham, 7, 0)


class ViewTable:
    def __init__(self):
        page = Tk()
        page.title("Premier League")
        page.minsize(900, 600)
        page.minsize(950, 650)
        page.iconbitmap("premier_league.ico")

        self.page = page

        # Defines style of new window
        style = ttk.Style(self.page)  # add style to treeview
        style.theme_use("clam")

        # Builds frame of widgets on page
        self.table_view_frame = ttk.Frame(self.page)
        self.table_view_frame.pack(fill="both", expand=True)

        self.build_tree()

        self.tree.configure(height=15)  # Adjust the height value as desired

        self.table_view_frame.configure(height=400)

        page.mainloop()

    def build_tree(self):
        tree_frame = ttk.Frame(self.table_view_frame)

        # Column configuration
        self.table_view_frame.columnconfigure(0, weight=10)
        self.table_view_frame.columnconfigure(1, weight=1)

        # Create Treeview
        self.tree = ttk.Treeview(tree_frame)

        # Define our columns
        self.tree['columns'] = ('Current Rank',
                                'Club', 'Matches Played', 'Wins', 'Draws', 'Losses', 'Goal Forwarded', 'Goals Against',
                                'Points')

        # Only shows headings and hides first empty column
        self.tree['show'] = 'headings'

        # Displays headers
        for column in self.tree[
            "columns"]:  # cycles through headers and uses internal identifiers as names for columns (text = column)
            self.tree.heading(column, text=column, anchor=W)

        # Define columns attributes
        for column in self.tree["columns"]:
            self.tree.column(column, width=120, minwidth=120, anchor=W)

        # Shows data in tree
        all_teams = Table1.rank_teams()

        for team in all_teams:  # values are themselves dictionaries
            self.tree.insert("", "end", values=(
                team.current_rank, team.team_name, team.matches_played, team.wins,
                team.draws, team.losses, team.goals_forward, team.goals_against, team.points)
                             )

        # Creates object of scrollbar
        s = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree['yscrollcommand'] = s.set

        # Grids the tree and scrollbar
        self.tree.grid(row=0, column=0)
        s.grid(row=0, column=1, sticky=NSEW)

        # Packs the frame
        tree_frame.grid(row=0, column=0, pady=20)


ViewTable()
