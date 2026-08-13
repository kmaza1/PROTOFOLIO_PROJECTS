""""
********************************************************************************************
* Autor : MAZA Kossivi Renaud                                                              *
*                                                                                          *
* Date : 06/06/2025                                                                        *
*                                                                                          *
* Purpose: project of questions quiz (QCM)                                                 *
*                                                                                          *
* version :  1                                                                             *
*                                                                                          *
* Curse teacher : Dr AMOUZOU Akpénè Dorcas                                                 *
*                                                                                          *
* Language: pyton                                                                          *
*                                                                                          *
* Title: Projet_Python_1                                                                   *
********************************************************************************************
"""
liste_des_questionnaires=[
        {
            "question": "Quelle planète est la plus proche du Soleil ?",
            "choix": ["A.Vénus", "B.Terre", "C.Mars", "D.Mercure"],
            "reponse": "D"
        },
        {
            "question": "Quel langage est principalement utilisé pour le développement web côté client ?",
            "choix": ["A.Python", "B.Java", "C.HTML", "D.JavaScript"],
            "reponse": "D"
        },

        {
            "question": "Qui a écrit *Les Misérables* ?",
            "choix": ["A.Victor Hugo", "B.Émile Zola", "C.Molière", "D.Albert Camus"],
            "reponse": "A"
        },

        {
            "question": "Quel est le nom du fleuve qui forme une partie de la frontière entre le Togo et le Ghana ?",
            "choix":[ "A. Mono "," B. Volta "," C. Niger","  D. Oti"],
            "reponse": "A"
        },

        {
            "question": "Quelle est l' ethnie la plus représentée dans l' armée togolaise ?",
            "choix": ["A. Éwé "," B. Kabyè "," C. Moba"," D. Kotokoli"],
            "reponse": "B"
        },
        {
            "question": "Quel est le principal aéroport international du Togo ?",
            "choix": ["A. Aéroport de sarakawa"," B. Aéroport de Sokodé "," C. Aéroport de Gnassigbé Ayadema ","D. Aéroport de Kara"],
            "reponse": "C"
        },
        {
            "question": "Quel est le plat national consommé au pétit déjeuné par la population  Togolaise  ?",
            "choix": ["A. Attiéké "," B. Fufu "," C. Akoumé "," D. Ayimolou"],
            "reponse": "D"
        },
        {
            "question": "Quelle planète est surnommée la planète rouge ?",
            "choix": ["A. Vénus","  B. Mars","  C. Jupiter","  D. Saturne"],
            "reponse": "B"
        },
        {
            "question": "Quel prophète a reçu les dix commandements ?",
            "choix": ["A. Abraham "," B. David "," C. Moïse","  D. Élie"],
            "reponse": "C"
        },
        {
            "question": "Combien de livres contient la bible?",
            "choix": ["A. 24 "," B. 27 "," C. 39 "," D. 66"],
            "reponse": "D"
        },
        {
            "question": "Quel président la france l'opération militaire mènant  à l'élimination du guide lybien Mohamar Khadafi ?",
            "choix": ["A. Nicolas Sarkozy" "B. François Hollande ","C. Emmanuel Macron  ""D. Jacques Chirac"],
            "reponse": "A"
        },
        {
            "question": "Qui est actuellement président de la Chine  ?",
            "choix": ["A. Hu Jintao","  B. Xi Jinping "," C. Deng Xiaoping "," D. Li Keqiang"],
            "reponse": "B"
        },
        {
            "question": "Qui a inventé l’ampoule électrique pratique ?",
            "choix": ["A. Thomas Edison", "B. Nikola Tesla", "C. Benjamin Franklin", "D. Alexander Graham Bell"],
            "reponse": "A"
        },
        {
            "question": "Qui est l’inventeur du téléphone ?",
            "choix": ["A. Thomas Edison", "B. Nikola Tesla", "C. Alexander Graham Bell", "D. Guglielmo Marconi"],
            "reponse": "C"
        },
        {
            "question": "Quel scientifique a inventé la radio ?",
            "choix": ["A. Isaac Newton", "B. Guglielmo Marconi", "C. Albert Einstein", "D. Alexander Fleming"],
            "reponse": "B"
        },
        {
            "question": "Qui est connu pour avoir développé la théorie de la relativité ?",
            "choix": ["A. Isaac Newton", "B. Galileo Galilei", "C. Nikola Tesla", "D. Albert Einstein"],
            "reponse": "D"
        },
        {
            "question": "Quel inventeur est célèbre pour la machine à vapeur ?",
            "choix": ["A. James Watt", "B. Thomas Savery", "C. Richard Trevithick", "D. George Stephenson"],
            "reponse": "A"
        },
        {
            "question": "Qui a découvert la pénicilline en 1928 ?",
            "choix": ["A. Marie Curie", "B. Louis Pasteur", "C. Alexander Fleming", "D. Jonas Salk"],
            "reponse": "C"
        },
        {
            "question": "Qui a conçu la première machine à calculer mécanique ?",
            "choix": ["A. Alan Turing", "B. Blaise Pascal", "C. Charles Babbage", "D. John Napier"],
            "reponse": "B"
        },
        {
            "question": "Quel duo de frères est à l'origine du premier vol motorisé en 1903 ?",
            "choix": ["A. Les frères Lumière", "B. Les frères Wright", "C. Les frères Curie", "D. Les frères Montgolfier"],
            "reponse": "B"
       }
]
def observation(cpt):
    if cpt<0:
          return f"Votre etes  nul  en  culture générale après la série cette épreuve de QCM"
    elif cpt>=0 and cpt<3:
        return f" Votre niveau est très  insuffisant en  culture générale après cette épreuve de QCM"
    elif cpt>=3 and cpt<6:
        return f"Votre niveau médiocre en  culture générale après la série  cette épreuve de QCM"
    elif  cpt >= 6 and cpt  < 10:
         return f"Vous étes  insuffisant en  culture générale après cette épreuve de QCM"
    elif cpt <=  10 and  cpt < 12:
        return f"Votre  niveau est passable en  culture générale après cette épreuve de QCM"
    elif  cpt>=12 and cpt<=14 :
        return  f"Votre niveau est assez bien en  culture générale après cette épreuve de QCM "
    elif   cpt >14 and cpt <= 16:
        return f"Votre  niveau est bien en  culture générale après cette épreuve de QCM"
    elif  cpt > 16 and cpt <= 18:
        return f"Votre  niveau est Très - bien  en  culture générale après  cette épreuve de QCM"
    else:
        return f"Vous  avez  un Exécéllent niveau  en  culture générale après cette épreuve de QCM"

import random
print("")
print("==================== BIENVENUE DANS CE QUIZ DE CULTURE GENERALE ==================")
print("")
print("Le principe est simple,vous aurez un quiz de 20 questions auquel vous répondrez et vous aurez votre note sur 20 accompagné d'une observation. ")
print("NB: Une bonne reponse vaut +1 et une mauvise -1 ; alors  faites gaf et soyez sur avant de repondre   ")
print("Etes - vous prèt")
reponse = input('Reponse : ')
liste_1reponses=['oui','OUI','o','O']
liste_2reponses=['NON','non','n','N']
answer = ['A','C','B','D']
while reponse not in liste_1reponses and reponse not in liste_2reponses:
    print("" "👀👀 Revoyez  et veuillez suivre les règles de reponses 👀👀")
    reponse = input('Reponse : ')

if reponse in liste_1reponses:
    print(" 👏👏👏  Let's go . 👏🏽👏🏽👏🏽")
else:
    print(" 😡😡😡  Revenez quand vous sereiez serireux et  prèt. 😡😡😡 ")
    exit(0)

def questions_un_champion(liste_des_questionnaire):

    cpt = 0
    random.shuffle(liste_des_questionnaire)

    for q in liste_des_questionnaire :
        print(" ","Question :", q["question"])
        print(" ","Choix :",q ["choix"])
        print(" ","Vous devez répondre en choisissant soit l'option A,soit B ,soit C ou D")
        print("")

        reponse = input('   Reponse : ')
        while reponse not  in answer:
             print("" " 👀👀 Revoyez et veuillez suivre les règles de reponses  👀👀")

             reponse = input('   Reponse : ')
        if reponse==q["reponse"] :
            print("  ","  👍👍👍 **Bonne reponse**  👍👍👍")
            cpt+=1
        else:
           print(f" " " 🥵🥵🥵** Mauvaise  reponse **  🥺🥺🥺 ,  👉👉👉👉   La bonne reponse était : ", q['reponse'] ,  " 👈👈👈👈")
           cpt-=1
    print(" ")
    #a=cpt
    print(f"===================         Ton score est de :{cpt}/ {len(liste_des_questionnaire)}  après cette épreuve de QCM  .  =================")

    print(f"== == == == == == == == == == OBSERVATION: {observation(cpt) }  == == == == == == == == == == == == ==")
    print("")
questions_un_champion(liste_des_questionnaires)