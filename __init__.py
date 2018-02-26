from soccersimulator import SoccerTeam
from .strategies  import fonceurStrategy
from .strategies  import defenseStrategy
from .strategies  import  strmilStrategy

def get_team(nb_players):
	myteam = SoccerTeam(name="MaTeam")
	if nb_players == 1:
		myteam.add("Joueur " ,fonceurStrategy())
	if nb_players == 2:
		myteam.add("Joueur 1", strmilStrategy())
		myteam.add("Joueur 2", defenseStrategy())
	if nb_players == 4:
		myteam.add("Joueur 1",fonceurStrategy())
		myteam.add("Joueur 2",fonceurStrategy())
		myteam.add("Joueur 3",fonceurStrategy())
		myteam.add("Joueur 4",fonceurStrategy())
	return myteam	

def get_team_challenge(num):
	myteam = SoccerTeam(name="MaTeamChallenge")
	if num == 1:
		myteam.add("Joueur Chal "+str(num),fonceurStrategy())
	return myteam
