""""
********************************************************************************************
* Autor : MAZA Kossivi Renaud                                                              *
*                                                                                          *
* Date : 06/08/2025                                                                        *
*                                                                                          *
* Purpose: project of questions quiz (QCM)                                                 *
*                                                                                          *
* version :  2 (utilisation de fichier)                                                                            *
*                                                                                          *
* Curse teacher : Dr AMOUZOU Akpénè Dorcas                                                 *
*                                                                                          *
* Language: pyton                                                                          *
*                                                                                          *
* Title: Projet_Python_1                                                                   *
********************************************************************************************
"""
#Fonction pour obsaervation
def observation(a,cpt):
    if cpt<0:
      return f"Votre etes  nul  en  culture générale après la série  de question {a} vous devez sérieusement vous cultivé intélectuellement"
    elif cpt>=0 and cpt<6*a:
        return f" Votre niveau est très  insuffisant en  culture générale après la série  de question {a} vous devez doublé d'éffort en terme de culture générale"
    elif cpt>=6*a and cpt<8*a:
        return f"Votre niveau est insuffisant en  culture générale après la série  de question {a}  vous devez doublé d'éffort en terme de culture générale"
    elif cpt>=8*a and cpt < 10*a:
         return f"Vous étes  faible en  culture générale après la série  de question {a}  vous devez doublé d'éffort en terme de culture générale"
    elif cpt >=10*a and cpt < 12*a:
        return f"Votre  niveau est passable en  culture générale après la série  de question {a}  vous devez cultivé davantage  en culture"
    elif  cpt>=12*a and cpt<14*a :
        return  f"Votre niveau est assez bien en  culture générale après la série  de question {a}  continuer à vous cultivé "
    elif   cpt>=14*a and cpt < 16*a:
        return f"Votre  niveau est bien en  culture générale après la série  de question {a} continuer dans ce sens"
    elif  cpt >= 16*a and cpt <= 18*a:
        return f"Votre  niveau est Très - bien  en  culture générale après  la série de question {a} continuer dans ce sens"
    else:
        return f"Vous  avez  un Exécéllent niveau  en  culture générale après  la série de question{a}"


print("\t\t\t\t\t\t\t\t==================== BIENVENUE DANS CE QUIZ DE CULTURE GENERALE ======================\t\t\t\t\t\t\t\t")
print("")
print("Le principe est simple,vous aurez une série de  10 quiz de 10 questions chacun auquel vous répondrez et vous aurez votre note sur 20 accompagné d'une observation. ")
print("NB: Une bonne reponse vaut +2 et une mauvaise -2 ; alors  faites gaf et soyez sûr avant de repondre   , vous avez aussi la possibilité de quitter quand vous avez  fini une série donnée")
print("Etes - vous prèt")
print("Veuillez votre élément de reponse  cette liste ['oui','OUI','o','O','yes','YES'] si  vous etes prèt , sinon choisir dans cette liste ['NON','non','n','N','no','NO']")
reponse = input('Reponse : ')
liste_1reponses=['oui','OUI','o','O','yes','YES']
liste_2reponses=['NON','non','n','N','no','NO']
answers = ['A','C','B','D']
while reponse not in liste_1reponses and reponse not in liste_2reponses:
    print("" "👀👀 Revoyez  et veuillez suivre les règles de reponses 👀👀")
    reponse = input('Reponse : ')

if reponse in liste_1reponses:
    print(" 👏👏👏  Let's go . 👏🏽👏🏽👏🏽" )
else :
    print(" 😡😡😡  Revenez quand vous sereiez serireux et  prèt. 😡😡😡 " )
    exit(0)
reponses=['oui','OUI','o','O']
import ast
with open("questionnaire.txt","r",encoding="UTF-8") as file:
    content = file.read()
    liste_de_questions =ast.literal_eval(content)

import random
def questions_un_champion(liste_de_questions):
    #global reponse
    global i
    global cpt
    i=1
    continuer = True
    while continuer:
        cpt = 0
        cpt2 = 0
        a=1
        print(f"Série de qestion {cpt + 1} :  ")
        for q in liste_de_questions :
            random.shuffle(q)
            for i in range(len(q))  :
                    print(" ",f"Question {i+1} :", q[i]["question"])
                    print(" ","Choix :", q[i]["choix"])
                    print(" ","Vous devez répondre en choisissant soit l'option A,soit B ,soit C ou D")
                    reponse1=input(f"  Reponse {i+1} : ")

                    print("")
                    while reponse1 not in answers:
                        print("" " 👀👀 Revoyez et veuillez suivre les règles de reponses  👀👀")
                        reponse1 = input(f"Reponse {i+1}: ")

                    if reponse1== q[i]["reponse"]:
                        print("  ","  👍👍👍 **Bonne reponse**  👍👍👍")
                        print(" ")
                        cpt+=2
                    else:
                        print(f"  🥵🥵🥵** Mauvaise  reponse **  🥺🥺🥺 ,  👉👉👉👉   La bonne reponse était : ,   {q[i]['reponse']}",    " 👈👈👈👈")
                        cpt-=2
                        print(" ")
                    i += 1
            print(" ")
            print(f"==================================Ton score est : {cpt} / {20*a} après la série de question {a} ==============================================")
            print("")
            print(f"== == == == == == == == == == OBSERVATION: {observation(a, cpt) }  == == == == == == == == == == == == ==")
            print("")
            a+=1
            if a > len(liste_de_questions):

                print(" 🙏🙏🙏🙏 Nous voici à la fin de ce quiz  de  question pour un champion,Merci pour votre participation  🙏🙏🙏🙏")
                continuer = False
            else:
                reponse2=input("Voulez vous continuer avec d' autres questions  :  ")

                if reponse2 in  liste_1reponses:

                    print(f"On continue alors avec  la série de question  {cpt2+2}" )
                    cpt2+=1
                    b=cpt2+1
                    continuer = True

                else:
                   print("  🙏🙏🙏🙏 Nous vous remercions pour votre participation et on espère vous revoir dans un futur proche 🙏🙏🙏🙏")
                   continuer=False
                   break
questions_un_champion(liste_de_questions)


