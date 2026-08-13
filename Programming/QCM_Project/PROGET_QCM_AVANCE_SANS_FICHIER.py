""""
*****************************************************************************************************************
* Autor : MAZA Kossivi Renaud                                                                                   *
*                                                                                                               *
* Title: Projet_Python_1_avancé                                                                                 *
*                                                                                                               *
* Date : 06-07-08/06/2025                                                                                       *
*                                                                                                               *
* Purpose: Test of my knowladge in python                                                                       *
*                                                                                                               *
* version :  1                                                                                                  *
*                                                                                                               *
* Curse teacher : Dr AMOUZOU Akpénè Dorcas                                                                      *
*                                                                                                               *
* Foctionnement:                                                                                                *
*   #Ce programme s'inscrit dans le sens du RENAUD_PROGET_QCM_PYTHON_SIMPLE ;                                   *
*mais cette fois ,on a une  série de 10 QCM de 10 questions.                                                    *
*   #Mais s'il y a une bonne réponse  , l'utilisateur à +2 , sinon il a -2.                                     *
*   #A la fin son score  lui sera affiché  et une observation lui sera donné par rapport à son niveau .         *
*   #L' utilisateur est libre commencer l' épreuve ou non ,la poursuivre à la fin de n'importe série  ou non.   *
*   #L'utilisateur doit respecter les régles de réponse pour passer d'un champ à un autre.                      *
*                                                                                                               *
* Language: pyton                                                                                               *
*****************************************************************************************************************
"""

questionnaire_1 = [
    {
        "question": "Quelle est la capitale de la France ?",
        "choix": [ "A.Paris", "B.Londres", "C.Berlin", "D.Rome"],
        "reponse": "A"
    },
    {
        "question": "Quel est le résultat de 3 * 4 ?",
        "choix": ["A.7", "B.12", "C.9", "D.14"],
        "reponse": "B"
    },
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
        "question": "Quelle est la formule chimique du chlorure de sodium?",
        "choix": ["A.CO2", "B.H2O", "C.O2", "D.NaCl"],
        "reponse": "D"
    },
    {
        "question": "Qui a écrit *Les Misérables* ?",
        "choix": ["A.Victor Hugo", "B.Émile Zola", "C.Molière", "D.Albert Camus"],
        "reponse": "A"
    },
    {
        "question": "Quel est le plus grand océan du monde ?",
        "choix": ["A.Atlantique", "B.Arctique", "C.Pacifique", "D.Indien"],
        "reponse": "C"
    },
    {
        "question": "Quelle est la valeur de Pi (approximativement) ?",
        "choix": ["A.2.14", "B.3.14", "C.4.14", "D.3.41"],
        "reponse": "B"
    },
    {
        "question": "Combien de continents existe-t-il ?",
        "choix": ["A.5", "B.6", "C.7", "D.8"],
        "reponse": "C"
    },
    {
        "question": "Quelle est la langue la plus parlée au monde ?",
        "choix": ["A.Anglais", "B.Espagnol", "C.Chinois mandarin", "D.Arabe"],
        "reponse": "C"
    }
]


questionnaire_2 = [

        {   "question": "Quelle est la capitale de l’Espagne ?",
            "choix": ["A.Madrid", "B.Barcelone", "C.Valence", "D.Séville"],
            "reponse": "A"
       },
        {
            "question": "En quelle année a eu lieu la Révolution française ?",
            "choix": ["A.1776", "B.1789", "C.1804", "D.1914"],
            "reponse": "B"
        },
        {
            "question": "Quel est le carré de 8 ?",
            "choix": ["A.64", "B.16", "C.32", "D.81"],
            "reponse": "A"
        },
        {
            "question": "Combien font 7 + 5 * 2 ?",
            "choix": ["A.24", "B.17", "C.19", "D.22"],
            "reponse": "B"
        },

        {
            "question": "Quel est l'état physique de l'eau à 100°C ?",
            "choix": ["A.Solide", "B.Liquide", "C.Gaz", "D.Plasma"],
            "reponse": "C"
        },
        {
            "question": "Quel est le symbole chimique de l’oxygène ?",
            "choix": ["A.Ox", "B.O2", "C.O", "D.Oy"],
            "reponse": "C"

        },

        {
            "question": "Quel langage est utilisé pour les pages web ?",
            "choix": ["A.Python", "B.HTML", "C.C++", "D.Java"],
            "reponse": "B"
        },
        {
                "question": "Que signifie 'CPU' ?",
                "choix": ["A.Central Processing Unit", "B.Computer Primary Unit", "C.Central Program Utility", "D.Computer Processor Unit"],
                "reponse": "A"
        },

        {        "question": "Quel est le plus long fleuve du monde ?",
                "choix": ["A.Amazon", "B.Nil", "C.Yangtsé", "D.Mississippi"],
                "reponse": "A"
        },
        {
                "question": "Quel pays a le plus grand nombre d’habitants ?",
                "choix": ["A.Inde", "B.Chine", "C.États-Unis", "D.Brésil"],
                "reponse": "A"
        }

]
questionnaire_3 = [
    {
        "question": "Comment dit-on 'bonjour' en allemand ?",
        "choix": ["A.Hola", "B.Hello", "C.Hallo", "D.Ciao"],
        "reponse": "C"
    },
    {
        "question": "Quelle langue est parlée au Brésil ?",
        "choix": ["A.Espagnol", "B.Portugais", "C.Français", "D.Anglais"],
        "reponse": "B"
    },
    {
        "question": "Qui était Napoléon Bonaparte ?",
        "choix": ["A.Un roi", "B.Un empereur", "C.Un philosophe", "D.Un peintre"],
        "reponse": "B"
    },
    {
        "question": "Quand a eu lieu la Seconde Guerre mondiale ?",
        "choix": ["A.1914-1918", "B.1939-1945", "C.1804-1815", "D.1945-1955"],
        "reponse": "C"
    },
    {
        "question": "Combien de joueurs y a-t-il dans une équipe de football ?",
        "choix": ["A.9", "B.10", "C.11", "D.12"],
        "reponse": 'C'
    },
    {
        "question": "Qui a remporté la Coupe du Monde 2018 ?",
        "choix": ["A.Brésil", "B.Croatie", "C.France", "D.Allemagne"],
        "reponse": "C"
    },
    {
        "question": "Quel instrument a des touches blanches et noires ?",
        "choix": ["A.Guitare", "B.Piano", "C.Violoncelle", "D.Flûte"],
        "reponse": "B"
    },
    {
        "question": "Qui est le chanteur de 'Gaou à paris' ?",
        "choix": ["A.Prince", "B.Elvis Presley", "C.Asalffo", "D.Justin Bieber"],
        "reponse": "C"
    },
    {
        "question": "Quel instrument dont à hériter le chanteur Mussa Diabaté ?",
        "choix": ["A.Guitare", "B.Harpe", "C.cora", "D.Flûte"],
        "reponse": "C"
    },
    {
        "question": "Qui fut  le  président de l'ukraine lorsque la russie envahissait la crimée qui une région de l'ukraine annexée par la russie' ?",
        "choix": ["A.Barack Obama", "B.Boris Elsin", "C.Vladimir Poutine", "D.Pédro Porotchinko"],
        "reponse": "D"
    }


]
questionnaire_4 = [
    {
        "question": "Quelle est la formule chimique du méthane ?",
        "choix": ["A. H2O"," B. CO2 ","C. O2","D. CH4"],
        "reponse": "D"
    },
    {
        "question": "Quelle particule possède une charge négative ?",
        "choix": ["A. Proton","B. Neutron","C. Électron","D. Photon"],
        "reponse": "C"
    },
    {
        "question": "Quel est l’organe principal de la circulation sanguine ?",
        "choix":["A. Le foie","B. Le cœur","C. Le poumon","D. Le rein"] ,
        "reponse": "B"
    },
    {
        "question": "Quel gaz est nécessaire à la respiration humaine ?",
        "choix": ["A. Dioxyde de carbone "," B. Azote "," C. Oxygène "," D. Hydrogène"],
        "reponse": "C"
    },
    {
        "question": "Quelle planète est surnommée la planète rouge ?",
        "choix": ["A. Vénus","  B. Mars","  C. Jupiter","  D. Saturne"],
        "reponse": "B"
    },
    {
        "question": "Quel est l’unité de mesure de la force ?",
        "choix": ["A. Watt "," B. Pascal "," C. Newton","  D. Joule"],
        "reponse": "C"
    },
    {
        "question": "Quelle est la vitesse de la lumière dans le vide ?",
        "choix":["A. 300 000 km/h","  B. 300 000 m/s "," C. 300 000 km/s "," D. 3 000 km/s"],
        "reponse": "C"
    },
    {
        "question": "Quelle molécule transporte l’oxygène dans le sang ?",
        "choix": ["A. L’adrénaline "," B. L’hémoglobine","  C. Le plasma "," D. L’insuline"],

        "reponse": "B"
    },
    {
        "question": "Quel est l'état de la matière dans le noyau du Soleil ?",
        "choix": "A. Solide  B. Liquide  C. Gazeux  D. Plasma",
        "reponse": "D"
    },
    {
        "question": "Comment s’appelle la transformation d’un liquide en gaz ?",
        "choix": ["A. Fusion "," B. Condensation  ","C. Vaporisation "," D. Sublimation"],
        "reponse": "C"
    }
]
questionnaire_5 = [
    {
        "question": "Quelle est la capitale du Togoland ?",
        "choix": ["A. Sokodé "," B. Kara "," C. Lomé "," D. Anèho"],
        "reponse": "D"
    },
    {
        "question": "Combien de régions administratives compte le Togo ?",
        "choix": ["A. 4 "," B. 5 "," C. 6","  D. 7"],
        "reponse": "D"
    },
    {
        "question": "Quel pays parmi ces pays ne partage pas de frontière avec le Togo ?",
        "choix": ["A. Ghana  ","B. Côte d’Ivoire "," C. Bénin  ","D. Burkina Faso"],
        "reponse": "B"
    },
    {
        "question": "Quel est le nom du fleuve qui forme une partie de la frontière entre le Togo et le Ghana ?",
        "choix":[ "A. Mono "," B. Volta "," C. Niger","  D. Oti"],
        "reponse": "A"
    },
    {
        "question": "Quel est le principal parti politique du Togo ?",
        "choix": ["A. RPT"," B. UNIR "," C. ADDI "," D. ANC",],
        "reponse": "B"
    },
    {
        "question": "Quel est l'ancien nom du Togo sous la colonisation allemande ?",
        "choix": ["A. Togoland "," B. Togoville  ","C. Togo-Allemand "," D. Westafrika"],
        "reponse": "A"
    },
    {
        "question": "Qui fut le premier président du Togo indépendant ?",
        "choix":["A. Togoland "," B. Togoville  ","C. Togo-Allemand "," D. Westafrika"],
        "reponse": "A"
    },
    {
        "question": "Quelle est l' ethnie la plus représentée dans l' armée togolaise ?",
        "choix": ["A. Éwé "," B. Kabyè "," C. Moba"," D. Kotokoli"],
        "reponse": "C"
    },
    {
        "question": "Quel est le principal aéroport international du Togo ?",
        "choix": ["A. Aéroport de sarakawa"," B. Aéroport de Sokodé "," C. Aéroport de Gnassigbé Ayadema ","D. Aéroport de Kara"],
        "reponse": "C"
    },
    {
        "question": "Quel est le plat national consommé au pétit déjeuné par la population  Togolaise  ?",
        "choix": ["A. Attiéké "," B. Fufu "," C. Akoumé "," D. Ayimolou"],
        "reponse": "C"
    }
]

questionnaire_6= [
    {
        "question": "Quel est le livre sacré des musulmans ?",
        "choix": ["A. Bible","  B. Torah "," C. Coran "," D. Vedas"],
        "reponse": "C"
    },
    {
        "question": "Combien de commandements Dieu a-t-il donnés à Moïse selon la Bible ?",
        "choix": ["A. 5 "," B. 7 "," C. 10 "," D. 12"],
        "reponse": "C"
    },
    {
        "question": "Qui est considéré comme le fondateur du christianisme ?",
        "choix": ["A. Abraham "," B. Moïse "," C. Jésus-Christ "," D. Paul"],

        "reponse": "C"
    },
    {
        "question": "Quel jour de la semaine les musulmans célèbrent-ils généralement leur culte ?",
        "choix":[ "A. Vendredi  ","B. Dimanche "," C. Samedi "," D. Lundi"],
        "reponse": "B"
    },
    {
        "question": "Quel prophète a reçu les dix commandements ?",
        "choix": ["A. Abraham "," B. David "," C. Moïse","  D. Élie"],
        "reponse": "C"
    },
    {
        "question": "Quel est le lieu de pèlerinage sacré des musulmans ?",
        "choix": ["A. Jérusalem "," B. Médine "," C. La Mecque "," D. Bagdad"],
        "reponse": "C"
    },
    {
        "question": "Combien de livres contient la bible?",
        "choix": ["A. 24 "," B. 27 "," C. 39 "," D. 66"],
        "reponse": "D"
    },
    {
        "question": "Dans quelle religion Krishna est-il une divinité ?",
        "choix": ["A. Bouddhisme "," B. Islam "," C. Hindouisme "," D. Judaïsme"],
        "reponse": "C"
    },
    {
        "question": "Quel est le jour sacré de repos dans le judaïsme ?",
        "choix": ["A. Vendredi "," B. Samedi "," C. Dimanche "," D. Lundi"],
        "reponse": "B"
    },
    {
        "question": "Comment appelle-t-on le jeûne musulman du mois de Ramadan ?",
        "choix": ["A. Zakat "," B. Hajj "," C. Salat "," D. Sawm"],
        "reponse": "D"
    }
]

questionnaire_7 = [
{
        "question": "Qui est l’actuel vice président des États-Unis  ?",
        "choix": ["A. Donald Trump ","   B. Joe Biden "," C. Barack Obama "," D. Jedy Vince"],
        "reponse": "A"
    },
    {
        "question": "Quel président la france l'opération militaire mènant  à l'élimination du guide lybien Mohamar Khadafi ?",
        "choix": ["A. Nicolas Sarkozy" "B. François Hollande ","C. Emmanuel Macron  ""D. Jacques Chirac"],
        "reponse": "A"
    },
    {
        "question": "Quel est le nom de l’actuel président du Togo  ?",
        "choix": ["A. Savi de Tové","B. Faure Gnassingbé "," C. Gilchrist Olympio "," D. Komlan Mally"],
        "reponse": "A"
    },
    {
        "question": "Qui est le président de la Russie connu pour avoir succédé à Boris Eltsine en 1999 ?",
        "choix": ["A. Dmitri Medvedev "," B. Mikhail Gorbatchev "," C. Vladimir Poutine "," D. Sergueï Lavrov"],
        "reponse": "C"
    },
    {
        "question": "Quel président sud-africain a succédé à Nelson Mandela en 1999 ?",
        "choix":[ "A. Thabo Mbeki "," B. Jacob Zuma "," C. Cyril Ramaphosa "," D. Frederik de Klerk"],
        "reponse": "A"
    },
    {
        "question": "Qui est actuellement président de la Chine  ?",
        "choix": ["A. Hu Jintao","  B. Xi Jinping "," C. Deng Xiaoping "," D. Li Keqiang"],
        "reponse": "B"
    },
    {
        "question": "Quel président a été destitué lors de la révolution tunisienne en 2011 ?",
        "choix": ["A. Kais Saied","  B. Zine El Abidine ","Ben Ali "," C. Habib Bourguiba "," D. Mohamed Ghannouchi"],
        "reponse": "B"
    },
    {
        "question": "Quel président brésilien a été célèbre pour sa politique environnementale controversée ?",
        "choix": ["A. Dilma Rousseff "," B. Jair Bolsonaro "," C. Luiz Inácio Lula da Silva "," D. Fernando Henrique Cardoso"],
        "reponse": "B"
    },
    {
        "question": "Quel président ukrainien a dirigé le pays au moment de l’invasion russe en 2022 ?",
        "choix": ["A. Petro Porochenko "," B. Viktor Iouchtchenko "," C. Volodymyr Zelensky "," D. Leonid Koutchma"],
        "reponse": "C"
    },
    {
        "question": "Quel président du Rwanda est reconnu pour avoir dirigé le pays depuis la fin du génocide de 1994 ?",
        "choix": ["A. Juvenal Habyarimana "," B. Pasteur Bizimungu "," C. Paul Kagame "," D. Édouard Karemera"],
        "reponse": "C"
    }
]
questionnaire_8 = [
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
        "question": "Quel inventeur est à l’origine du vaccin contre la rage ?",
        "choix": ["A. Louis Pasteur", "B. Robert Koch", "C. Edward Jenner", "D. Marie Curie"],
        "reponse": "A"
    },
    {
        "question": "Qui a inventé l’imprimerie moderne au XVe siècle ?",
        "choix": ["A. Johannes Gutenberg", "B. Léonard de Vinci", "C. Isaac Newton", "D. Blaise Pascal"],
        "reponse": "A"
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

questionnaire_9 = [
{
        "question": "Quelle est la capitale du Kazakhstan ?",
        "choix": ["A. Almaty", "B. Tachkent", "C. Astana (Noursoultan)", "D. Bichkek"],
        "reponse": "C"
    },
    {
        "question": "Quelle est la capitale du Sri Lanka ?",
        "choix": ["A. Colombo", "B. Kandy", "C. Galle", "D. Sri Jayawardenepura Kotte"],
        "reponse": "D"
    },
    {
        "question": "Quelle est la capitale de la Birmanie (Myanmar) ?",
        "choix": ["A. Rangoon", "B. Naypyidaw", "C. Mandalay", "D. Bagan"],
        "reponse": "B"
    },
    {
        "question": "Quelle est la capitale de la Moldavie ?",
        "choix": ["A. Bucarest", "B. Sofia", "C. Chisinau", "D. Vilnius"],
        "reponse": "C"
    },
    {
        "question": "Quelle est la capitale du Malawi ?",
        "choix": ["A. Lilongwe", "B. Blantyre", "C. Lusaka", "D. Maputo"],
        "reponse": "A"
    },
    {
        "question": "Quelle est la capitale du Bhoutan ?",
        "choix": ["A. Thimphou", "B. Katmandou", "C. Dacca", "D. Paro"],
        "reponse": "A"
    },
    {
        "question": "Quelle est la capitale du Suriname ?",
        "choix": ["A. Paramaribo", "B. Cayenne", "C. Georgetown", "D. Caracas"],
        "reponse": "A"
    },
    {
        "question": "Quelle est la capitale de l’Azerbaïdjan ?",
        "choix": ["A. Tbilissi", "B. Erevan", "C. Bakou", "D. Achgabat"],
        "reponse": "C"
    },
    {
        "question": "Quelle est la capitale du Lesotho ?",
        "choix": ["A. Mbabane", "B. Maseru", "C. Gaborone", "D. Pretoria"],
        "reponse": "B"
    },
    {
        "question": "Quelle est la capitale du Honduras ?",
        "choix": ["A. San Salvador", "B. Managua", "C. Guatemala", "D. Tegucigalpa"],
        "reponse": "D"
    }
]
questionnaire_10 = [
{
        "question": "Quelle civilisation ancienne a construit les pyramides de Gizeh ?",
        "choix": ["A. Les Romains", "B. Les Grecs", "C. Les Égyptiens", "D. Les Mésopotamiens"],
        "reponse": "C"
    },
    {
        "question": "Où la civilisation maya s’est-elle principalement développée ?",
        "choix": ["A. En Afrique du Nord", "B. En Asie Mineure", "C. En Amérique centrale", "D. En Océanie"],
        "reponse": "C"
    },
    {
        "question": "Quelle ville était la capitale de l’Empire babylonien ?",
        "choix": ["A. Ninive", "B. Sumer", "C. Babylone", "D. Ur"],
        "reponse": "C"
    },
    {
        "question": "Quel philosophe est associé à la civilisation grecque classique ?",
        "choix": ["A. Confucius", "B. Socrate", "C. Bouddha", "D. Hammurabi"],
        "reponse": "B"
    },
    {
        "question": "La civilisation de la vallée de l’Indus est connue pour ses villes planifiées. Quelle est l’une de ses principales cités ?",
        "choix": ["A. Pékin", "B. Mohenjo-Daro", "C. Samarcande", "D. Angkor"],
        "reponse": "B"
    },
    {
        "question": "Les Olmèques sont considérés comme la civilisation mère de quelle région ?",
        "choix": ["A. L’Afrique de l’Ouest", "B. L’Europe centrale", "C. L’Amérique du Sud", "D. L’Amérique précolombienne"],
        "reponse": "D"
    },
    {
        "question": "Quelle civilisation africaine médiévale est célèbre pour son commerce de l’or et du sel ?",
        "choix": ["A. Le royaume du Zimbabwe", "B. L’empire du Mali", "C. Le royaume du Bénin", "D. L’empire d’Aksoum"],
        "reponse": "B"
    },
    {
        "question": "Quelle civilisation est connue pour ses guerriers samouraïs et sa structure féodale ?",
        "choix": ["A. Chinoise", "B. Mongole", "C. Japonaise", "D. Coréenne"],
        "reponse": "C"
    },
    {
        "question": "Quelle civilisation a érigé les statues monumentales de l’île de Pâques ?",
        "choix": ["A. Polynésienne", "B. Aztèque", "C. Mochica", "D. Maya"],
        "reponse": "A"
    },
    {
        "question": "Quelle civilisation andine est connue pour sa capitale Cuzco et le Machu Picchu ?",
        "choix": ["A. Aztèque", "B. Inca", "C. Tiahuanaco", "D. Wari"],
        "reponse": "B"
    }
]
def observation(a,cpt):
    if cpt<0:



       return f"Votre etes  nul  en  culture générale après la série  de question {a} vous devez sérieusement vous cultivé intélectuellement"
    elif cpt>=0 and cpt<6*a:
        return f" Votre niveau est très  insuffisant en  culture générale après la série  de question {a} vous devez doublé d'éffort en terme de culture générale"
    elif cpt>=6*a:
        return f"Votre niveau est insuffisant en  culture générale après la série  de question {a}  vous devez doublé d'éffort en terme de culture générale"
    elif 6*a >= cpt <= 10*a:
         return f"Vous étes  faible en  culture générale après la série  de question {a}  vous devez doublé d'éffort en terme de culture générale"
    elif 10*a >= cpt <= 12*a:
        return f"Votre  niveau est passable en  culture générale après la série  de question {a}  vous devez cultivé davantage  en culture"
    elif  cpt>=12*a and cpt<=14*a :
        return  f"Votre niveau est assez bien en  culture générale après la série  de question {a}  continuer à vous cultivé "
    elif   cpt>=14*a and cpt <= 16*a:
        return f"Votre  niveau est bien en  culture générale après la série  de question {a} continuer dans ce sens"
    elif  cpt >= 16*a and cpt <= 18*a:
        return f"Votre  niveau est Très - bien  en  culture générale après  la série de question {a} continuer dans ce sens"
    else:
        return f"Vous  avez  un Exécéllent niveau  en  culture générale après  la série de question{a}"

   # print("Nous voici à la fin de notre épreuve de culture générale")
print("")
print("==================== BIENVENUE DANS CE QUIZ DE CULTURE GENERALE ==================")
print("")
print("Le principe est simple,vous aurez un quiz de 20 questions auquel vous répondrez et vous aurez votre note sur 20 accompagné d'une observation. ")
print("NB: Une bonne reponse vaut +2 et une mauvise -2 ; alors  faites gaf soyez sur avant de repondre   ")
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

liste_des_questionnaires=[questionnaire_1,questionnaire_2,questionnaire_3,questionnaire_4,questionnaire_5,questionnaire_6,questionnaire_7,questionnaire_8,questionnaire_9,questionnaire_10]
import random
def questions_un_champion(liste_des_questionnaires):
    #global reponse
    global i
    global cpt
    i=1
    continuer = True
    #for i in range(len(liste_des_questionnaires)):

    while continuer:
        cpt = 0
        cpt2 = 0
        a=1
        print(f"Série de qestion {cpt + 1} :  ")
        for q in liste_des_questionnaires :
            random.shuffle(q)
            for i in range(len(q))  :
                    print(" ",F"Question {i+1} :", q[i]["question"])
                    print(" ","Choix :", q[i]["choix"])
                    print(" ","Vous devez répondre en choisissant soit l'option A,soit B ,soit C ou D")
                    reponse1=input(f'     Reponse {i+1} : ')

                    print("")
                    while reponse1 not in answers:
                        print("" " 👀👀 Revoyez et veuillez suivre les règles de reponses  👀👀")
                        reponse1 = input(f'   Reponse {i+1}: ')

                    if reponse1== q[i]["reponse"]:
                        print("  ","  👍👍👍 **Bonne reponse**  👍👍👍")
                        print(" ")
                        cpt+=2
                    else:
                        print(f" " "  🥵🥵🥵** Mauvaise  reponse **  🥺🥺🥺 ,  👉👉👉👉   La bonne reponse était : ",   {q[i]['reponse']}," 👈👈👈👈")
                        cpt-=2
                        print(" ")
                    i += 1
            print(" ")
            print(f"==================================Ton score est : {cpt} / {20*a} après la série de question {a} ==============================================")
            print("")
            print(f"== == == == == == == == == == OBSERVATION: {observation(a, cpt) }  == == == == == == == == == == == == ==")
            print("")
            a+=1
            if a > len(liste_des_questionnaires):

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
questions_un_champion(liste_des_questionnaires)


