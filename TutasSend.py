
from re import S
import requests
import colorama



g ='\033[92m'
n = '\033[0m'
r = '\033[91m'

aldo="""
**********************************************************************
*     CODED BY: OROCHIMARU                                            * 
*     TELEGRAM: t.me/TUTAS_TECH                                       *   *   *
*     GITHUB  : https://github.com/TutasTech                          * *      *                                                   
*     YOUTUBE : https://youtube.com/channel/UClpEVLJVWOx89Vnqq-BG8Lg ********************                                                     
*     MY_TELEGRAM: @THEFAUCON                                         **        *
*     WHATSAPP:    FATAL ERROR 403 foriben                            *  *    *
*                                                                     *    *
*                                                                     *      
**********************************************************************                                                                     


"""


print(g)

print(aldo,"\n")


c=input("entrez le code du pays (sans +) exemple 237 : ") 

print("\n entrez le numero de telephone ",end='')
c1=input()

numb='+'+c+c1

print("le programe enverra le message à ",numb)

text=input("entrez le message ")


re = requests.post('https://textbelt.com/text',{
			'phone' : numb,
			'message' : text ,
			'key' : 'textbelt'
		})
		
print(re.json())


if '"success" : true ' in re.text:
	print("\033[message envoyé avec succès \033[0m")
	input('\n\t\tPress Enter To Exit...')
elif '"Only one test text message is allowed per day."' in re.text:
	print("\033[0m \n if you want to bypass this limit Connect to your vpn and retry\n ***OROCHIMARU")

else:
	print("\033[91m Error Occured")
	print("\033[91m Failed to send SMS! ")
	print("\n\t","\033[SPOWERED BY TUTASTECH \033[0m")	
	input('\n\t\tPress Enter To Exit...')


