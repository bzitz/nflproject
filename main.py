import csv
import game

csvfile = open('2015.csv', 'r')
reader = csv.reader(csvfile)

games = []
for x in reader:
   games.append(game.Game(x[1],x[2],x[3],x[4],x[5],x[6]))

for z in games:
    print z.description()
