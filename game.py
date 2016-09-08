import nfldb
import constants

class Game(object):
    def __init__(self,favorite,line,dog,ou,year,week):    
        def formatLine(line):
            if line == 'PK':
                return 0
            else:
                return float(line)
        
        def standardizeTeam(team):
            for teamarray in constants.TEAMS:
                if team in teamarray:
                    return teamarray[0] 

        def getGameData(week, year, favorite):
            db = nfldb.connect()
            q = nfldb.Query(db)
            q.game(season_year = year, season_type='Regular', week=week, team = standardizeTeam(favorite))
            for g in q.as_games():
                self.away_score = g.away_score
                self.home_score = g.home_score
                self.away_team = g.away_team
                self.home_team = g.home_team
                self.gsis_id = g.gsis_id
                self.winner = g.winner
                self.loser = g.loser

        getGameData(week, year, favorite)       
        self.spread = formatLine(line) 
        self.favorite = standardizeTeam(favorite) 
        self.underdog = standardizeTeam(dog)
        self.ou = ou
        self.week = week
        self.year = year
        #print self.home_team

    def description(self):
        print "The game between %s and %s in week %s of the %s Regular Season. %s was favored by %d points" % (self.home_team, self.away_team, self.week, self.year, self.favorite, abs(self.spread))
