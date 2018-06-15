from soccersimulator import SoccerTeam, Simulation, show_simu
from profAI import fonceurStrategy,defenseStrategy,get_team


## Creation d'une equipe
pyteam = get_team(2)
thon = SoccerTeam(name="ThonTeam")
thon.add("PyPlayer",fonceurStrategy()) 
thon.add("ThonPlayer",defenseStrategy())   #Strategie aleatoire
#Creation d'une partie
simu = Simulation(pyteam,thon) # simu declaré mais Simulation est un class appelé
#Jouer et afficher la partie
show_simu(simu)  # appelé
