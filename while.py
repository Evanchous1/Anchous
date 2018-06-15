from time import *
from random import *
from colorama import Fore, Back, Style, init
import os 

seed(clock())
init()
hg=300
ug=10
hm=100
um=28
hp=200
up=20
m=0
g=100
ork=100
mag=100
life=1
def y():	
	f=open('save.txt','w')
	f.write('dmg '+str(u)+'\ndmg '+str(h)+'\nmoney '+str(m))
	f.close()

os.system('cls')
print(Fore.WHITE+Back.GREEN+'добро пожаловать в "ОКРАИНУ МОСКВЫ"'+Style.RESET_ALL)
save=int(input('1-начать заново\n2-Продолжить игру\n'))
os.system('cls')
if save==1:
	print(Fore.CYAN+'Выберите класс\n1:Головорез\n2:Мужык\n3:Пацан\n'+Style.RESET_ALL)
	k=int(input())
	if k==1:
		print('!Вы головорез!\nЗдоровье:300\nУрон:10\n')
		h=hg
		u=ug
	if k==2:
		print('!Вы Мужык!\nЗдоровье:100\nУрон:28\n')
		h=hm
		u=um
	if k==3:
		print('!Вы Пацан!\nЗдоровье:200\nУрон:20\n')
		h=hp
		u=up
	m=0
	hmax=h
	y()

if save==2:
	f=open('save.txt','r')
	w = f.read()
	l = w.split('\n')
	print (l)
	u=l[0]
	h=int(l[1])
	m=l[2]
	print(h)
def x():
	print('---------------------------------')
	print(Fore.GREEN+'Ваше здоровье: '+Style.RESET_ALL,h)
	print(Fore.YELLOW+'Монеты: '+Style.RESET_ALL,m)
	print('---------------------------------')
sleep(1)
while 1:
	a = randrange(3) 
	if a==0:	
		x()
		print
		print('на вас напал маленький гопник\n')
		q=int(input('1-убежать\n2-напасть\n3-суицид\n'))
		if q==1:
			print('!Вы успешно убежали!')
		if q==2:
			while 1:
				print('вы ударили гопника Ваше здоровье :',h,'здоровье гопника :',g)
				g=g-u
				if g<1:
					print('вы убили гопника +10 монет') 
					m=m+10
					g=100
					y()
					break
				print('вас ударил гопник Ваше здоровье :',h,'здоровье гопника',g)
				h=h-15
				if h<1:
					print('вас убил гопник')
					m=m+15
					g=100
					life=0
					y()
					break
		if q==3:
			break 
	sleep(1)		
	os.system('cls')		
	if a==1:
		x()
		print('вы видите подозрительный магазин')
		q=int(input('1-зайти\n2-убежать\n3-cуицид\n'))
		if q==1:
			print('на вас напала злая кассирша')
			while 1:
				print('вы ударили кассиршу Ваше здоровье :',h,'здоровье кассирши :',mag)
				mag=mag-15
				if mag<1:
					print('вы победили кассиршу +15 монет')
					m=m+15
					mag=100
					y()
					break
				print('вас укусила злая кассирша Ваше здоровье :',h,'здоровье кассирши :',mag)
				h=h-10
				if h<1:
					print('вас убили')
					life=0	
					mag=100
					y()
					break	
		if q==2:
			print('\n!вы убежали!\n')	
		if q==3:
			break
	sleep(1)
	os.system('cls')		
	if a==2:
		x()
		q=int(input('"вы видите ларёк"\n1-посмотреть\n2-пройти мимо\n3-суицид\n'))
		if q==1:
			z=int(input('привет!Желаешь выпить пива?(10 монет)\n 1-да 2-нет\n'))
			if z==1:
				if m>10:
					m=m-10
					h=hmax
					y()
					print('Здоровье пополнено -10 монет')
					print(Fore.WHITE+Back.YELLOW+'Пивка для рывка!'+Style.RESET_ALL)
				else:
					print(Fore.RED+'!вам не хватает монет!'+Style.RESET_ALL)
					sleep(1)	
			if z==2:
				print('Пока!') 
		if q==2:
			print('Вы прошли мимо')		
		if q==3:
			break
	os.system('cls')		




	if not life:
		break	
sleep(1)
print(Fore.BLACK+Back.GREEN+'*Y O U  A R E  D E A D*'+Style.RESET_ALL)
