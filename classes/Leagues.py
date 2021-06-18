import soccer_data_api
from soccer_data_api import SoccerDataAPI
 
class Leagues:
    def __init__(self, league):
        self.league = league
        self.soccer_data = SoccerDataAPI()
        self.url = ""
    
    def get_league(self):
        data = []
        if(self.league.lower() == "Premiere League".lower()):
            data = self.soccer_data.english_premier()
            self.url = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Premier_League_Logo.svg/1200px-Premier_League_Logo.svg.png"
        
        elif(self.league.lower() == "La Liga".lower()):
            data = self.soccer_data.la_liga()
            self.url = "https://iscreativestudio.com/wp-content/uploads/2016/08/logotipos4.jpg"
        
        elif(self.league.lower() == "Ligue 1".lower()):
            data = self.soccer_data.ligue_1()
            self.url = "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Ligue_1_Uber_Eats.svg/1200px-Ligue_1_Uber_Eats.svg.png"
        
        elif(self.league.lower() == "Bundesliga".lower()):
            data = self.soccer_data.bundesliga()
            self.url = "https://www.logofootball.net/wp-content/uploads/bundesliga-logo.png"
        
        elif(self.league.lower() == "Serie A".lower()):
            data = self.soccer_data.serie_a()
            self.url = "https://www.insidesport.co/wp-content/uploads/2020/02/1581149078672.png"
        
        elif(self.league.lower() == "Eredivisie".lower()):
            data = self.soccer_data.eredivisie()
            self.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Eredivisie_nieuw_logo_2017-.svg/1200px-Eredivisie_nieuw_logo_2017-.svg.png"
        
        elif(self.league.lower() == "Russian Premier League".lower()):
            data = self.soccer_data.russian_premier()
            self.url = "https://europeanleagues.com/wp-content/uploads/RUS-PL-new.png"
        
        elif(self.league.lower() == "English Championship".lower()):
            data = self.soccer_data.english_championship()
            self.url = "https://upload.wikimedia.org/wikipedia/en/3/37/EFL_Championship.png"
        
        return data
    
    def get_logo(self):
        return self.url

    def get_top_scorer(self):
        data = []
        #loop through teams in this object's league
        for team in self.get_league():
            data.append(team["top_scorer"])

        players = {}
        #finding player with maximum number of goals
        for player in data:
            player = player.split(" ")
            
            #check if player has first and last name
            if(len(player) == 4):
                playerName =  player[0] + " " + player[1]
            else:
                playerName =  player[0]
            
            players[playerName] = int(player[len(player) - 1 ])
            
        return max(players, key=players.get)  + " - " + str(max(players.values()))



        
    


