import thread
import time
import os
#TODO: 
#son quand un job commence
#meilleur methode pour le comptage du temps: boucle for avec des sleep  de 10s
# killer les vlc apres appel

os.system("clear")
print "Je suis votre Coach personnel, Je vais vous faire bosser moi! :p"



#Questions 
matieres =[]
temps =[]

while(True):
	a=raw_input('\nQuelle activite voulez-vous travailler?')
	if(a == ""):
		break
	matieres.append(a) 
	temps.append(input('Combien de temps ? (h) '))

schedule = dict(zip(matieres,temps))
#schedule = {'Manger': 1, 'Pause': 0.5, 'Web Of things': 2, 'Web Of Things': 2}
print "\nVoila votre emploi du temps: \n",schedule


#pour chaque matiere:
for mat,tmp in schedule.iteritems():
	print "\n\n\n --> Demarage Activite: ", mat, "\n", time.asctime()
        t =thread.start_new_thread(os.system,("cvlc ~/Musique/go.mp3",))
	
        #calcul temps/2, temps -15 min, temps -5min
	tmp = tmp *3600 #secs
	mitemps = dernier_quart = dernier_5 = 0
	
	mitemps = tmp/2
	if mitemps > 900 :
		dernier_quart = mitemps - (15* 60)
		dernier_5 = 300
		
		#decompte temps
		time.sleep(mitemps)
		#arret t/2,t-13,t5
		print "mitemps!!!",time.asctime()
		t =thread.start_new_thread(os.system,("cvlc ~/Musique/mitemps.mp3",))
		
		
		#decompte temps
		time.sleep(dernier_quart)
		#arret t/2,t-13,t5
		print "DERnier Quart!!!!", time.asctime()
		t = thread.start_new_thread(os.system,("cvlc ~/Musique/15min.mp3",))
		
		#decompte temps
		time.sleep(dernier_5)
		#arret t/2,t-13,t5
		print "5 min!!!", time.asctime()
							
		t = thread.start_new_thread(os.system,("cvlc ~/Musique/5min.mp3",))
		time.sleep(300)


t =thread.start_new_thread(os.system,("cvlc ~/Musique/fin.mp3",))
print "Bien Joue!\n Au revoir fiston! ;)\n",time.asctime()
t =thread.start_new_thread(os.system,("killall vlc",))
thread.exit()


