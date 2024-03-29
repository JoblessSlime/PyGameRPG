# Créé par S145 15AST, le 01/06/2022 en Python 3.7

from math import*
from random import*
from time import *
import pygame
from pygame import *

pygame.init()



#========================================
#                sound
#========================================

mixer.music.load('Simple Leaves - An Original Track By CJ Music.mp3')
ost_autumn = mixer.Sound('Simple Leaves - An Original Track By CJ Music.mp3')
sound = 0
son = 1
new_son = 1
mixer.music.load('Lament of the Leaves - FantasyFolk Music.mp3')
ost_village = mixer.Sound('Lament of the Leaves - FantasyFolk Music.mp3')
mixer.music.load('Only Piano - Loneliness.mp3')
ost_garden = mixer.Sound('Only Piano - Loneliness.mp3')
mixer.music.load('A Tavern for the Night.mp3')
ost_citadelle = mixer.Sound('A Tavern for the Night.mp3')
mixer.music.load('Celtic Music - Origins.mp3')
ost_yggdrasil = mixer.Sound('Celtic Music - Origins.mp3')
mixer.music.load('(Medieval Celtic Fantasy Music) - A Pathway In The Sunken Woods.mp3')
ost_Spring = mixer.Sound('(Medieval Celtic Fantasy Music) - A Pathway In The Sunken Woods.mp3')
mixer.music.load('A Beautiful Dream.mp3')
ost_Hiver = mixer.Sound('A Beautiful Dream.mp3')
mixer.music.load('Dragon Quest VIII Symphonic Suite - Remembrances.mp3')
ost_Ruines = mixer.Sound('Dragon Quest VIII Symphonic Suite - Remembrances.mp3')
mixer.music.load('Relaxing Celtic Music - A Little Place Called Home.mp3')
ost_house = mixer.Sound('Relaxing Celtic Music - A Little Place Called Home.mp3')
mixer.music.load('(Dark Fantasy Battle Music) - The Lord Of Chaos -.mp3')
ost_battle = mixer.Sound('(Dark Fantasy Battle Music) - The Lord Of Chaos -.mp3')
mixer.music.load('Fantasy Music - Forever Still.mp3')
ost_library = mixer.Sound('Fantasy Music - Forever Still.mp3')
active = ost_library

mixer.music.load('slash1.mp3')
sound_slash = mixer.Sound('slash1.mp3')
mixer.music.load('slash2.mp3')
sound_crush = mixer.Sound('slash2.mp3')
mixer.music.load('boxcrash.mp3')
sound_critical = mixer.Sound('boxcrash.mp3')

#=============================
#           screen
#=============================

pygame.display.set_caption("Fantasy RPG")
screen = pygame.display.set_mode((830, 700))
bg_Ygg = pygame.image.load("ygg.png")
bg_Village = pygame.image.load("town.png")
bg_Spring = pygame.image.load("spring.png")
bg_Ruines = pygame.image.load("ruines.png")
bg_citadelle = pygame.image.load('city.png')
bg_autumn = pygame.image.load('autumn.png')
bg_winter1 = pygame.image.load('winter 1.png')
bg_winter2 = pygame.image.load('winter 2.png')
bg_battle = pygame.image.load('battle.png')
bg_house = pygame.image.load('maison.png')
bg_jardins = pygame.image.load('jardins.png')
bg_death = pygame.image.load('death.png')
bg_librairie = pygame.image.load('librairie.png')
bg_stats = pygame.image.load('levels.png')
bg_name = pygame.image.load('name.png')
bg_credit = pygame.image.load('credit.png')
activebg = bg_name

enter = pygame.image.load('enter.png')
box_lieux = pygame.image.load('box_lieux.png')
box_text = pygame.image.load('box_text.png')
magic = pygame.image.load('magie.png')
heal = pygame.image.load('health.png')
fireball = pygame.image.load('fire_ball.png')

obj0 = pygame.image.load('cotte_de_maille.png')
obj1 = pygame.image.load('épée_de_damocles.png')
obj1_1 = pygame.image.load('épée_de_damocles2.png')
obj2 = pygame.image.load('épée_de_fer.png')
obj3 = pygame.image.load('épée_royale.png')
obj3_3 = pygame.image.load('épée_royale2.png')
obj_démonic = pygame.image.load('épée_démoniaque.png')

'''
gold.png
health_potion.png
plastron.png
'''

temps = perf_counter()


inv_spe = {"clef" : 0 }

skill = []
Class = {"" : [1,1,1], "chevalier" : [1,1,1.5], "mage" : [1,1.7,1], "hero" : [1.2,2.2,2], "roi demon" : [1.4,2.5,1.8], "god of light" : [2,3,2.5], "god of darkness" : [1.8,3.1,2.8]}
Character_class = ""
class_bonus = Class[""]

base = 0

z = 0
day = 0
xp = 0
lvl = 1
gold = 0
enemy_lvl = 1

lvl_rank = 10

hour = "day"
daycounter = 90

slime_event = 0
équipe = []


#=================================================
#                     player
#=================================================

class Chara(pygame.sprite.Sprite):
    
    def __init__(self, char_type, hp, hp_lim, dgts, mc_var):
        super().__init__()
        self.char_type = char_type
        if self.char_type == "mc":
            self.image = pygame.image.load('chest.png')
            self.taille = 65,40
        elif self.char_type == "slime":
            self.image = pygame.image.load('slime.png')
            self.taille = 27,33
        elif self.char_type == "mimic":
            self.image = pygame.image.load('chest.png')
            self.taille = 65,40
        elif self.char_type == "dragon":
            self.image = pygame.image.load('dragon.png')
            self.taille = 65,40
        elif self.char_type == "alraune":
            self.image = pygame.image.load('0-alraune2.png')
            self.taille = 85,75
        elif self.char_type == "fred":
            self.image = pygame.image.load('0-fred2-removebg-preview.png')
            self.taille = 85,75
        self.all_char = pygame.sprite.Group()
        self.all_char.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 300
        
        self.vitesse = 1
        self.weapon_type = "lance"
        self.hp = hp
        self.hp_lim = hp_lim
        self.dgts = dgts
        if self.char_type == "mc" :
            self.pseudo = mc_var[0]
            self.force = mc_var[1]
            self.defense = mc_var[2]
            self.def_lim = mc_var[3]
            self.pm = mc_var[4]
            self.pm_lim = mc_var[5]
            self.crit = mc_var[6]
            self.esquive = mc_var[7]
            self.pts = 0

    def points(self):
        print("")
        print(" Où voulez vous dépensez vos pts de compétence ?")
        print("  0 pv    1 force    2 def    3 pm")
        where = int(input())
        if where >3 or where < 0:
            print("compétence introuvable")
            return""
        print(" Combien de pts voulez vous utilisez ?")
        print("  ( pts disponibles:", self.pts, ")")
        nbr = int(input())
        if nbr < 0:
            print("Vous ne pouvez pas mettre de nombres négatifs")
            return""
        if nbr > self.pts:
            nbr = self.pts
        self.pts = self.pts - nbr
        if where == 0:
            self.hp_lim = self.hp_lim + nbr
            print(" Vous avez augmentez vos pv de", nbr, "pts")
        elif where ==1:
            pass
            self.force = self.force + nbr
            print(" Vous avez augmentez votre force de", nbr, "pts")
        elif where == 2:
            self.def_lim = self.def_lim + nbr
            print(" Vous avez augmentez votre défense de", nbr, "pts")
        elif where == 3:
            self.pm_lim = self.pm_lim + nbr
            print(" Vous avez augmentez vos pm de", nbr, "pts")
        return""
        
        
    def health_bar(self, surface, bar_type):
        if bar_type == "health" :
            bar_color = (250,0,0)
        else :
            bar_color = (111,210,46)
            bar_position = [10, 200, self.pm, 0.1]
            
            
        if self.char_type == "mc" and bar_type == "health":
            bar_position = [10, 20, self.hp, 0.1]
        elif self.char_type != "mc" :
            bar_position = [self.rect.x, self.rect.y - 20, self.hp, 0.1]
            
        back_bar_color = (60,63,60)
        back_bar_position = bar_position
        if bar_type == "health":
            back_bar_position[3] = self.hp_lim
        else :
            back_bar_position[3] = self.pm_lim
            
            
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        
        
        
        

class Tool(pygame.sprite.Sprite):
    
    def __init__(self, char_type, x, y):
        super().__init__()
        self.char_type = char_type
        if self.char_type == "chest":
            self.image = pygame.image.load('chest.png')
        elif self.char_type == "house" :
            self.image = pygame.image.load('house.png')
        elif self.char_type == "shop":
            self.image = pygame.image.load('marchand.png')
        elif self.char_type == "boite":
            self.image = pygame.image.load('boite.png')
        elif self.char_type == "arbre":
            self.image = pygame.image.load('arbre.png')
        elif self.char_type == "tronc":
            self.image = pygame.image.load('tronc.png')
        elif self.char_type == "mairie":
            self.image = pygame.image.load('mairie.png')
        elif self.char_type == "box":
            self.image = pygame.image.load('box_lieux.png')
        elif self.char_type == "puit":
            self.image = pygame.image.load('puit.png')
        elif self.char_type == "eau":
            self.image = pygame.image.load('eau.png')
        elif self.char_type == "tombe":
            self.image = pygame.image.load('tombe.png')
        elif self.char_type == "poison":
            self.image = pygame.image.load('poison.png')
        elif self.char_type == "wall":
            self.image = pygame.image.load('wall.png')
        elif self.char_type == "livre":
            self.image = pygame.image.load('livre.png')
        elif self.char_type == "cube":
            self.image = pygame.image.load('cube.png')
        elif self.char_type == "bib":
            self.image = pygame.image.load('bibliothèque.png')
        elif self.char_type == "bib2":
            self.image = pygame.image.load('bibliothèque_2.png')
        elif self.char_type == "pan":
            self.image = pygame.image.load('panneaux.png')
        elif self.char_type == "anette":
            self.image = pygame.image.load('anette_help.png')
        elif self.char_type == "bourgeon":
            self.image = pygame.image.load('0-bourgeon2.png')
        elif self.char_type == "fog":
            self.image = pygame.image.load('0-fog2.png')
        self.all_char = pygame.sprite.Group()
        self.all_char.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Attacks(pygame.sprite.Sprite):
    
    def __init__(self, call, weapon_type, x, y):
        super().__init__()
        self.call = call
        self.dgts = call.dgts
        self.weapon_type = weapon_type
        if self.call.char_type == "alraune" :
            self.image = pygame.image.load('ronce.png')
        else:
            self.image = pygame.image.load('lance.png')
        self.all_char = pygame.sprite.Group()
        self.all_char.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

   
#=================================================
#                    équipements
#=================================================

class equipment :
    def __init__(self, nom, classe, rang, attack, defence, bonus):
        self.nom = nom
        self.classe = classe
        self.rang = rang
        self.attack = attack
        self.defence = defence
        self.bonus = bonus
        
    def __str__(self):
        print("  Nom:", self.nom, "  Classe:", self.classe, "  Rang:", self.rang)
        print("  Attack:", self.attack, "  Defense:", self.defence)
        if self.bonus != None:
            print("  Bonus:", self.bonus[0], self.bonus[1])
        return ""
            
    def objet (self):
        print(" ", self.nom)
        return ""
    
    def classer(self):
        if self.classe == "arme":
            return 0
        elif self.classe == "armure":
            return 1
        elif self.classe == "artéfact":
            return 2

class Objet_cons :
    def __init__(self,nom, nbr_utilisation, boost):
        self.nom
        self.nbr_utilisation = nbr_utilisation
        self.boost = boost
        
    def objet(self):
        print(" ", self.nom)
        return""
        
    def boost(self, char):
        if self.boost[0] == "hp":
            char.hp = char.hp + self.boost[1]
            if char.hp > char.hp_lim :
                char.hp = char.hp_lim
            print(" Vous avez récupéré", self.boost[1], "pv !")
        elif self.boost[0] == "for":
            char.force = char.force + self.boost[1]
            print(" Vous avez augmenté temporairement votre force de", self.boost[1], "!")
        elif self.boost[0] == "pm":
            char.pm = char.pm + self.boost[1]
            if char.pm > char.pm_lim :
                char.pm = char.pm_lim
            print(" Vous avez récupéré", self.boost[1], "pm !")
        self.nbr_utilisation = self.nbr_utilisation - 1
        return self.nbr_utilisation
    
    
def inventaire(inventory):
    for i in range(len(inventory)):
        if inventory[i]!= None:
            print(" ", i, end="")
            print(inventory[i].objet(), end="")
    return ""

def recherche_inv(inventory):
    print(inventaire(inventory))
    print("Tapez le numéro de l'objet dont vous voulez une information")
    num = int(input())
    if num > len(inventory) or num < 0:
        return " objet introuvable."
    print(inventory[num])
    return""
    

def équiper(inventory, équipé):
    print(inventaire(équipé))
    nani = int(input(" équiper(0)/retirer(1): "))
    if nani == 0 :
        print(inventaire(inventory))
        nani = int(input("Tapez le numéro de l'objet à équiper: "))
        if nani >= 0 and nani < len(inventory)+1:
            print("  ", inventory[nani].objet(), end="")
            confirmation = str(input(" (y/n) Voulez vous équiper cet objet ? "))
            if confirmation == "y":
                équipé[inventory[nani].classer()] = inventory[nani]
                print("  objet équipé.")
            else:
                print("  opération interrompue.")
        else:
            print("  opération interrompue.")
        return " "
    elif nani == 1 :
        nani = int(input("Tapez le numéro de l'objet à retirer: "))
        if nani >= 0 and nani < len(équipé)+1 and équipé[nani] != None:
            print("  ", équipé[nani].objet(), end="")
            confirmation = str(input(" (y/n) Voulez vous retirer cet objet ? "))
            if confirmation == "y" :
                équipé[nani] = None
                print("  objet retiré.")
            else:
                print("  opération interrompue.")
        else:
            print("  opération interrompue.")
        return " "
    return "opération interrompue."


inventory = []
équipé = [None, None, None]



#=================================================
#                    Lieux
#=================================================

class Lieu:
    def __init__(self, nom, diff, access):
        self.nom = nom
        self.diff = diff
        
    def __str__(self):
        return self.nom
    


lieux = [Lieu("Ville de départ", 0, 0),Lieu("Plaine",1,0),Lieu("Ruines",2,0),Lieu("Citadelle",0,0),Lieu("Champs d'automne",3,0),Lieu("Sentier enneigé",4,0), Lieu("Sentier enneigé 2",4.5,0), Lieu("Yggdrasil",5,0),Lieu("jardins du repos",0,0),Lieu("Bibliothèque magique",0,0),]
lieu_actuel = lieux[0]

def voyage(lieux):
    global lieu_actuel
    print(" Tapez le numéro du lieu")
    for i in range(len(lieux)):
        print("  ", i, lieux[i])
    futur_lieu = int(input())
    if futur_lieu > len(lieux) or futur_lieu < 0:
        print("Ce lieu n'existe pas")
    else:
        lieu_actuel = lieux[futur_lieu]
        print("Vous êtes arrivé à: ", lieu_actuel)
    return ""


#=================================================
#                    alliés
#=================================================
class alliés :
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race
        self.love = 0
        self.lvl = 1
        self.attack = 10
        self.pv = 50
        self.xp = 0
        self.lp = 0
        self.lvl_rank = 50
        self.love_rank = 5
        
    def __str__(self):
        return "nom: {}   race: {}   love: {}   lvl: {}   attack: {}   pv: {}".format(self.nom, self.race, self.love, self.lvl, self.attack, self.pv)
    
    def leveling(self, xp):
        if self.lvl_rank <= self.xp + xp:
            while self.lvl_rank <= self.xp + xp:
                self.lvl = self.lvl + 1
                self.xp = self.xp + xp - self.lvl_rank
                self.lvl_rank = int(self.lvl_rank * 1.25)
                self.pv = int(self.pv*1.05)
                self.attack = int(self.attack*1.125)
            return "votre allié ", self.nom, " est passé niveau ", self.lvl
        else:
            self.xp = self.xp + xp
            return ""
    
    def love_leveling(self, lp):
        if self.love_rank == 10:
            return ""
        if self.love_rank <= self.lp + lp:
            while self.love_rank <= self.lp + lp and self.love_rank < 10:
                self.love = self.love + 1
                self.lp = self.lp + lp - self.love_rank
                self.love_rank = int(self.love_rank * 1.15)
            return "votre allié ", self.nom, " est passé niveau ", self.lvl
        else:
            self.lp = self.lp + lp
            return ""
            

#=================================================
#                     time
#=================================================

def time():
    global temps
    global day
    global hour
    activebg = bg_credit
    screen.blit(activebg, (0,0))
    
    str_jour = "jour " + str(day)
    print("jour", day,",", hour)
    temps_2 = perf_counter()
    int_time = int(temps_2 - temps)
    print(int_time)
    str_time = str(int_time) + " s"
    
    write(str_jour,(415,300), 34, "white")
    write(str_time,(415,400), 34, "white")
    
    clef = True
    while clef:
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN: # MOUSEMOTION
                clef = False
    return""



#=================================================
#                    credits
#=================================================

def credits ():
    activebg = bg_credit
    screen.blit(activebg, (0,0))

    write("Made with python, using spyder",(415,50), 34, "white")
    pygame.display.flip()
    sleep(0.7)
    write("Developed by Jobless Slime",(415,85), 34, "white")
    pygame.display.flip()
    sleep(0.7)
    write("Musics:",(415,120), 34, "white")
    pygame.display.flip()
    sleep(0.3)
    write("Ville de départ : 'Lament of the Leaves' (Vindsvept)",(415,155), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Plaine : 'A pathway In the Sunken Woods' (Peter Crowley's Fantasy)",(415,190), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Ruines : 'Remembrances' (Dragon quest series)",(415,225), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Citadelle : 'A Tavern for the Night' (Peter Crowley's Fantasy)",(415,260), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Bibliothèque magique : 'Forever still' (Adrian von ziegler)",(415,295), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Champs d'automne : 'Simple Leaves' (CJ Musics)",(415,330), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Sentier enneigé : 'A beautiful dream' (Robert Amacker)",(415,365), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Yggdrasil : 'Origins' (Adrian von ziegler)",(415,400), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Jardins secret : 'Loneliness' (Adrian von ziegler)",(415,435), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Maison : 'A little place called Home' (Adrian von ziegler)",(415,470), 25, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Combat : 'The lord of chaos' (Peter Crowley's Fantasy)",(415,505), 25, "white")
    pygame.display.flip()
    sleep(0.7)
    write("graphics:",(415,540), 34, "white")
    pygame.display.flip()
    sleep(0.3)
    write(" Raphaël",(415,575), 25, "white")
    pygame.display.flip()
    sleep(0.6)
    write("With pygame library",(415,610), 34, "white")
    pygame.display.flip()
    sleep(0.7)
    write("Discord: Raphael sama#9028",(415,645), 34, "white")
    pygame.display.flip()
    
    clef = True
    while clef:
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN: # MOUSEMOTION
                clef = False
    
    return""



#=================================================
#                    stats
#=================================================

def stats (character):
    global lvl
    global lvl_rank
    global xp
    global gold
    global équipé
    global son
    global new_son
    global sound
    global active
    activebg = bg_stats
    clef = True
    while clef:
        
        screen.blit(activebg, (0,0))
        
        write(character.pseudo,(310,180), 34, "white")
        write(str(lvl),(150,280), 34, "white")
        write(str(xp),(150,350), 34, "white")
        write(str(lvl_rank),(250,350), 34, "white")
        write(str(gold),(150,410), 34, "white")
        write(str(character.hp),(150,480), 34, "white")
        write(str(character.hp_lim),(250,480), 34, "white")
        write(str(character.pm),(150,530), 34, "white")
        write(str(character.pm_lim),(250,530), 34, "white")
        write(str(character.force),(500,280), 34, "white")
        write(str(character.defense),(500,350), 34, "white")
        
        sortir = Tool("box", 250, 580)
        box1 = Tool("cube", 660, 200)
        box2 = Tool("cube", 660, 350)
        box3 = Tool("cube", 660, 500)
        
        screen.blit(sortir.image, sortir.rect)
        screen.blit(box1.image, box1.rect)
        screen.blit(box2.image, box2.rect)
        screen.blit(box3.image, box3.rect)
        
        write("sortir",(435,630), 34, "white")
        boxes = [sortir, box1, box2, box3]
        
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 : # MOUSEMOTION
                x,y = event.pos
                for box in boxes:
                    if box.rect.collidepoint(x,y):
                        if box == sortir:
                            clef = False
    
    return""
    
    '''
    print("")
    print("Nom : ", character.pseudo)
    print("niveau: ", lvl, "   prochain niveau: ", xp, "/", lvl_rank, "xp")
    print("hp: ", character.hp, "/", character.hp_lim, "   pm: ", character.pm,"/", character.pm_lim, "   or: ", gold)
    if équipé [0] != None :
        print("attack: ", character.dgts , "   force : ", character.force, "   arme: ", équipé[0].nom, "(", équipé[0].attack, ")")
    else:
        print("attack: ", character.force, "   force : ", character.force, "   arme:")
    if équipé [1] != None :
        print("defense: ", character.defense , "   armure: ", équipé[1].nom, "(", équipé[1].defence, ")")
    else:
        print("defense: ", character.defense , "   armure: ")
    if équipé [2] != None :
        print("artéfact: ", équipé[2].nom , "   ", équipé[2].bonus)
    return ""
    '''


def stats_load(character):
    global équipé
    character.dgts = character.force
    character.defense = character.def_lim
    if équipé[0] != None:
        character.dgts += équipé[0].attack
        character.defense += équipé[0].defence
    if équipé[1] != None:
        character.dgts += équipé[1].attack
        character.defense += équipé[1].defence
    if équipé[2] != None:
        character.dgts += équipé[2].attack
        character.defense += équipé[2].defence
    return ""

#=================================================
#                    shop
#=================================================

def shop ():
    global gold
    global inventory
    global activebg
    global son
    global new_son
    global sound
    global active
    active.stop()
    active = ost_house
    active.play(-1)
    activebg = bg_house
                
    achete_obj = False
    achete_what = []
    
    dico = {}
    vente = []
    épée_de_Damocles = equipment("épée de Damocles", "arme", "C", 15, 0, None)
    katana = equipment("katana", "arme", "B", 20, 0, None)
    épée_royale = equipment("épée royale", "arme", "A", 30, 5, None)
    armure_de_fer = equipment ("armure de fer", "armure", "C", 0, 7, None)
    armure_gelée = equipment ("armure gelée", "armure", "B", 0, 11, ("gel", None))
    armure_royale = equipment("armure royale", "armure", "A", 5, 20, ("gel", None))
    vente.append(épée_de_Damocles)
    vente.append(katana)
    vente.append(épée_royale)
    vente.append(armure_de_fer)
    vente.append(armure_gelée)
    vente.append(armure_royale)
    dico[0] = 30
    dico[1] = 50
    dico[2] = 90
    dico[3] = 30
    dico[4] = 60
    dico[5] = 110
    
    clef = True
    event_marchand = True
    all_parler = [True, False, False, False, False, False]
    while event_marchand :
        while clef:
        
            screen.blit(activebg,(0,0))
            forgeronne = pygame.image.load('0-gwen-removebg-preview.png')
            screen.blit(forgeronne, (345, 90))
            screen.blit(box_text, (200,350))
            write("Gwendolyn",(350,560), 18, "white")
            
            if all_parler[0]:
                write("Bienvenue à la forge de l'aube ! ",(400, 595), 14, "black")
                write("Ne vous retenez pas, achetez tout",(400, 615), 14, "black")
                write("ce qu'il vous faut.              ",(400, 635), 14, "black")
            elif all_parler[1]:
                write("Hey, vous n'avez pas assez d'argent",(400, 605), 14, "black")
                write("n'essayez pas de m'arnaquer !",(400, 630), 14, "black")
            elif all_parler[2]:
                write("Merci beaucoup pour votre achat !",(400, 615), 16, "black")
            elif all_parler[3]:
                write("Il paraît que certains êtres posséderaient",(400, 595), 14, "black")
                write("des objets légendaires. Je me demande si ",(400, 615), 14, "black")
                write("c'est vrai.              ",(400, 635), 14, "black")
            elif all_parler[4]:
                write("Les ruines enneigées sont dangeureuses, ",(400, 595), 14, "black")
                write("on dit qu'un dragon y à fait son nid.",(400, 615), 14, "black")
                write("Je vous conseille de faire attention.",(400, 635), 14, "black")
            elif all_parler[5]:
                write("Il existe de nombreuses légendes sur",(400, 595), 14, "black")
                write("les ruines à l'ouest. On dit qu'elles",(400, 615), 14, "black")
                write("auraient un lien avec celles du sud...",(400, 635), 14, "black")
            pygame.display.flip()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == KEYUP or event.type == MOUSEBUTTONDOWN:
                    clef = False
                    for i in range(len(all_parler)):
                        all_parler[i] = False
                            
                            
        event_acheter = True
        while event_acheter:
        
        
            screen.blit(activebg,(0,0))
            sortir = Tool("box", 10, 150)
            parler = Tool("box", 10, 300)
            acheter = Tool("box", 40, 580)

        
            box1 = Tool("cube", 460, 150)
            box2 = Tool("cube", 460, 300)
            box3 = Tool("cube", 460, 450)
            box4 = Tool("cube", 640, 150)
            box5 = Tool("cube", 640, 300)
            box6 = Tool("cube", 640, 450)
        
            screen.blit(sortir.image, sortir.rect)
            screen.blit(parler.image, parler.rect)
            screen.blit(acheter.image, acheter.rect)\
        
        
            screen.blit(box1.image, box1.rect)
            screen.blit(box2.image, box2.rect)
            screen.blit(box3.image, box3.rect)
            screen.blit(box4.image, box4.rect)
            screen.blit(box5.image, box5.rect)
            screen.blit(box6.image, box6.rect)
            screen.blit(obj1_1,(460,150))
            screen.blit(obj2,(460,300))
            screen.blit(obj3,(460,450))
            boxes = [sortir, parler, acheter, box1, box2, box3, box4, box5, box6]
        
            write("sortir",(200,200), 34, "white")
            write("parler",(200,350), 34, "white")
            write("acheter",(230,630), 34, "white")
        
            if achete_obj :
                write(achete_what[0].nom, (200,540), 16, "black")
                write(achete_what[1], (200,570), 16, "black")
            
            pygame.display.flip()
        
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 : # MOUSEMOTION
                    x,y = event.pos
                    for box in boxes:
                        if box.rect.collidepoint(x,y):
                            if box == sortir:
                                event_acheter = False
                                event_marchand = False
                            elif box == parler :
                                achete_obj = False
                                clef = True
                                event_acheter = False
                                all_parler[randint(3,5)] = True
                            elif box == acheter :
                                if achete_obj:
                                    if gold >= achete_what[2]:
                                        inventory.append(achete_what[0])
                                        gold -= achete_what[2]
                                        achete_obj = False
                                        #str_gold = "-" + str(achete_what[2])
                                        #write(str_gold, (250,520), 20, "black")
                                        clef = True
                                        event_acheter = False
                                        all_parler[2] = True
                                    else:
                                        clef = True
                                        event_acheter = False
                                        all_parler[1] = True
                                    
                            
                            
                            
                            elif box == box1 :
                                achete_obj = True
                                achete_what = [épée_de_Damocles, "30 or", 30]
                            elif box == box2 :
                                achete_obj = True
                                achete_what = [katana, "50 or", 50]
                            elif box == box3 :
                               achete_obj = True
                               achete_what = [épée_royale, "90 or", 90]
                            elif box == box4 :
                                achete_obj = True
                                achete_what = [armure_de_fer, "30 or", 30]
                            elif box == box5 :
                                achete_obj = True
                                achete_what = [armure_gelée, "60 or", 60]
                            elif box == box6 :
                                achete_obj = True
                                achete_what = [armure_royale, "110 or", 110]

    
    new_son = 1
    change_lieu()                      
    return ""




#=================================================
#                    battle
#=================================================

def battle (lvl_enemy, enemy, character):
    global xp
    global gold
    global inv_spe
    global activebg
    global new_son
    global active
    global équipé
    global lieux
    global lieu_actuel
    global event_mimic
    global slime_event
    global event_dragon
    active.stop()
    active = ost_battle
    active.play(-1)

    print("vous affrontez ennemi (", enemy.hp, "hp ) (lvl", lvl_enemy, ")")
    
    while enemy.hp > 0 and character.hp > 0:
        activebg = bg_battle
        screen.blit(activebg, (0,0))
        enemy.rect.x = 580
        enemy.rect.y = 350
        screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
        write(enemy.char_type, (590, 250), 32, "white")
        character.health_bar(screen, "health")
        character.health_bar(screen, "mp")
        enemy.health_bar(screen, "health")
        
        fuir = Tool("box", 20, 300)
        attaquer = Tool("box", 20, 450)
        screen.blit(fuir.image, fuir.rect)
        screen.blit(attaquer.image, attaquer.rect)
        boxes = [fuir, attaquer]
        
        write("fuir",(200,350), 34, "white")
        write("attaquer",(200,500), 34, "white")
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 : # MOUSEMOTION
                x,y = event.pos
                for box in boxes:
                    if box.rect.collidepoint(x,y):
                        if box == fuir:
                            new_son = 1
                            change_lieu()
                            return ""
                        elif box == attaquer :
                            dgts = character.dgts + randint(lvl, 3*lvl)
                            if randint(1,5) == 5: ######################################################
                                write("coup critique!", (430,250), 24, "white")
                                dgts = int(dgts * 1.5)
                                sound_critical.play(0)
                            else:
                                sound_slash.play(0)
                            enemy.hp = enemy.hp - dgts
                            dgts_str = "-" + str(dgts)
                            write(dgts_str, (500,300), 20, "red")
                            
                            pygame.display.flip()
                            sleep(0.5)
                            
                            aleatoire = random()
                            if aleatoire > 0.8 and enemy.hp < enemy.hp_lim:
                                heal = 16 + int(character.force) + randint(lvl_enemy, 3*lvl_enemy)
                                if enemy.hp + heal > enemy.hp_lim :
                                    heal = enemy.hp_lim - enemy.hp
                                enemy.hp += heal
                                dgts_str = "+" + str(heal)
                                write(dgts_str, (650,300), 20, "green")
                            else :
                                dgtse = enemy.dgts + randint(0, lvl_enemy // 1.5)
                                if dgtse < character.defense:
                                    dgts_rand = randint(1,2)
                                    character.hp -= dgts_rand
                                    dgts_str = "-" + str(dgts_rand)
                                    write(dgts_str, (450,450), 20, "red")
                                else:
                                    character.hp -= (dgtse - character.defense)
                                    dgts_str = "-" + str(dgtse)
                                    write(dgts_str, (450,450), 20, "red")
                                    
                            pygame.display.flip()
                            sleep(0.5)


    if enemy.hp <= 0 :
        gold = gold + 2*lvl_enemy
        gain = int(lvl_enemy*1.8) + int(random()*lvl_enemy)
        xp += gain
        print("-vous avez gagné")
        print("vous recevez", lvl_enemy,"or")
        print ("vous recevez", gain, "xp")
        if lvl_enemy >= 10 :
            if random() < 0.2 :
                inv_spe["clef"] = inv_spe["clef"] + 1
                print("vous obtenez 1 clef.")
        new_son = 1
        change_lieu()
        if enemy.char_type == "mimic" and lieu_actuel == lieux[2]:
            event_mimic = False
        elif enemy.char_type == "slime" and lieu_actuel == lieux[0]:
            slime_event = 1
        elif enemy.char_type == "dragon" :
            event_dragon = False
            
        return(leveling(character))
    elif character.hp <= 0:
        print("")
        print("-vous avez perdu")
        new_son = 1
        change_lieu()
    return""



#=================================================
#                    boss
#=================================================

def boss(boss, character):
    global xp
    global gold
    if random() > 0.6 and ( character.rect.x - boss.rect.x > -50 and character.rect.x - boss.rect.x < 50 ) and ( character.rect.y - boss.rect.y > -50 and character.rect.y - boss.rect.y < 50 ) :
        arme = arme = Attacks(boss, boss.weapon_type, boss.rect.x + 20, boss.rect.y - 50)
        screen.blit(arme.image, (arme.rect.x, arme.rect.y))
        pygame.display.flip()
        if touche(arme, character):
            character.hp -= boss.dgts
    else :
        if random() > 0.1 :
            if random() > 0.7 :
                if character.rect.x > boss.rect.x :
                    boss.rect.x += boss.vitesse
                else :
                    boss.rect.x -= boss.vitesse
                if character.rect.y > boss.rect.y :
                    boss.rect.y += boss.vitesse
                else :
                    boss.rect.y -= boss.vitesse
            else :
                if (character.rect.y - boss.rect.y) + (character.rect.x - boss.rect.x) > 0:
                    if character.rect.y - boss.rect.y > character.rect.x - boss.rect.x :
                        if character.rect.y > boss.rect.y:
                            boss.rect.y += boss.vitesse
                        else :
                            boss.rect.y -= boss.vitesse
                    else :
                        if character.rect.x > boss.rect.x :
                            boss.rect.x += boss.vitesse
                        else :
                            boss.rect.x -= boss.vitesse
                else :
                    if character.rect.y - boss.rect.y < character.rect.x - boss.rect.x :
                        if character.rect.y > boss.rect.y:
                            boss.rect.y += boss.vitesse
                        else :
                            boss.rect.y -= boss.vitesse
                    else :
                        if character.rect.x > boss.rect.x :
                            boss.rect.x += boss.vitesse
                        else :
                            boss.rect.x -= boss.vitesse
        else :
            if random() > 0.5 and boss.hp < boss.hp_lim:
                boss.hp += 20
            else :
                FIREEEEE_BALLLLLLL = 0
    if touche(boss, character):
        character.hp -= 0.2
    return""


#=================================================
#                    leveling
#=================================================

def leveling(character):
    global xp
    global lvl
    global lvl_rank
    if xp >= lvl_rank:
        print("")
        while xp >= lvl_rank:
            xp = xp-lvl_rank
            lvl = lvl + 1
            lvl_rank = int(lvl_rank*1.125)+4
            character.pts += 4
            character.force = int(character.force*1.12)
            character.hp_lim = int(character.hp_lim*1.07)
            if int(character.pm_lim*1.15) == character.pm_lim :
                character.pm_lim += 1
            else :
                character.pm_lim = int(character.pm_lim*1.15)
            if lvl == 2:
                print(" 'pm' obtenus !")
                character.pm_lim = 5
        print('-vous montez de niveau, nouveau niveau:', lvl)
        return""
    return ""


#=================================================
#                   events
#=================================================

event_anette = [[True, False, False, False], [False, False, False]]
event_mimic = True
event_dragon = True
print(len(event_anette[0]))

#=================================================
#                 Maisons ect
#=================================================

def maison(character):
    global lieu_actuel
    global lieux
    global active
    global activebg
    global new_son
    active.stop()
    active = ost_house
    active.play(-1)
    activebg = bg_house
    boucle = False
    event_talk = False
    
    
    if lieu_actuel == lieux[0]:
        character.rect.x, character.rect.y = 164,186
        all_parler = [False, False, False, False]
    
    elif lieu_actuel == lieux[3]:
        all_parler = [False, False, False, False]
        
    while not boucle:
        
            
        screen.blit(activebg,(0,0))
        
        if event_talk :
            if lieu_actuel == lieux[3]:
            
                screen.blit(activebg,(0,0))
                forgeronne = pygame.image.load('0-nain-removebg-preview.png')
                screen.blit(forgeronne, (230, 150))
                screen.blit(box_text, (200,350))
                write("Bordiln",(350,560), 18, "white")
                
                if all_parler[0]:
                    write("La bière c'est la vie ! Chez nous",(400, 595), 14, "black")
                    write("les nains, soit on creuse soit on boit,",(400, 615), 14, "black")
                    write("c'est la meilleure tradition au monde !",(400, 635), 14, "black")
                elif all_parler[1]:
                    write("La forgerrone est très douée, si vous partez",(400, 605), 14, "black")
                    write("à l'aventure je vous conseille d'y faire un tour.",(400, 630), 14, "black")
                elif all_parler[2]:
                    write("N'oubliez pas de vous reposez pendant votre aventure.",(420, 615), 15, "black")
                elif all_parler[3]:
                    write("J'ai croisé quelqu'un de louche la dernière fois",(400, 595), 14, "black")
                    write("il est passé rapidement est est reparti vers le sud.",(400, 615), 14, "black")
                    write("Je me demande qui c'était...              ",(400, 635), 14, "black")
        
        talk = Tool("box", 50, 150)
        quiter = Tool("box", 50, 300)
        screen.blit(talk.image, talk.rect)
        screen.blit(quiter.image, quiter.rect)
        
        boxes = [talk, quiter]
        
        write("parler",(230,200), 34, "white")
        write("sortir",(230,350), 34, "white")
        

        pygame.display.flip()
        
        character.hp, character.pm = character.hp_lim, character.pm_lim
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 : # MOUSEMOTION
                x,y = event.pos
                for box in boxes:
                    if box.rect.collidepoint(x,y):
                        if box == talk:
                            event_talk = True
                            for i in range(len(all_parler)):
                                all_parler[i] = False
                            all_parler[randint(0,3)] = True
                        elif box == quiter :
                            boucle = True
                            
    new_son = 1
    change_lieu()
    return ""

def anette_help():
    global lieu_actuel
    global lieux
    global active
    global activebg
    global event_anette
    global character
    boucle = False
    if event_anette[0][0]:
        event_talk = True
    else :
        event_talk = False
        
        
    while not boucle:
        screen.blit(activebg,(0,0))
        if event_talk:
            
            debug_talk = True
            
            anette = pygame.image.load('anette.png')
            screen.blit(anette, (320, 280))
            screen.blit(box_text, (200,350))
            write("Anette",(350,560), 18, "white")
            
            
            if True in event_anette[0]:
                if event_anette[0][0]:
                    write("Bonjour ! Je suis Anette, je suis là pour",(400, 590), 12, "black")
                    write("vous aidez à mieux prendre le jeu en main.",(400, 605), 12, "black")
                    write("J'espère que vous l'apprécierez !         ",(400, 620), 12, "black")
                    write("Passez un dialogue en appuyant sur une touche.",(400, 635), 12, "black")
                elif event_anette[0][1]:
                    write("Dans ce jeu, vous pouvez affrontez des monstres,",(400, 595), 14, "black")
                    write("explorez des lieux faits sur paint ou encore acheter    ",(400, 615), 14, "black")
                    write("des items hors de prix, bref un parfait rpg.    ",(400, 635), 14, "black")
                elif event_anette[0][2]:
                    write("Mais au fait, savez vous vous battre ?",(400, 595), 14, "black")
                    write("Les combats se lancent automatiquement",(400, 615), 14, "black")
                    write("quand vous rencontrez un ennemi.      ",(400, 635), 14, "black")
                elif event_anette[0][3]:
                    write("Après vos combats, vous perdrez surement",(400, 595), 14, "black")
                    write("des points de vie. Pour récupérer complètement,",(400, 615), 14, "black")
                    write("vous pouvez entrer dans votre maison ou a l'auberge.",(400, 635), 14, "black")
            elif True in event_anette[1]:
                if event_anette[1][0]:
                    write("rebonjour ! Même dans un jeu pourri comme",(400, 595), 14, "black")
                    write("celui-ci, il est possible de soigner votre",(400, 615), 14, "black")
                    write("personnage.         ",(400, 635), 14, "black")
                elif event_anette[1][1]:
                    write("Vous avez 3 moyens de vous soigner dans ce jeu :",(400, 590), 12, "black")
                    write(" - Utiliser une potion de soins",(400, 605), 12, "black")
                    write(" - Lancer un sort de soins",(400, 620), 12, "black")
                    write(" - Entrer chez vous où à l'auberge",(400, 635), 12, "black")
                elif event_anette[1][2]:
                    write("La premère façon n'est pas encore implémentée,",(400, 595), 14, "black")
                    write("mais vous pouvez lancer un sort de soin à partir",(400, 615), 14, "black")
                    write("du niveau 2 avec un clic droit.",(400, 635), 14, "black")
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN :
                    for i in event_anette:
                        for j in range(len(i)):
                            if i[j] and i[j] == i[-1]:
                                if debug_talk :
                                    i[j] = False
                                    event_talk = False
                                    debug_talk = False
                            elif i[j] :
                                if debug_talk :
                                    i[j] = False
                                    i[j+1] = True
                                    debug_talk = False
        else :  
            soigner = Tool("box", 50, 150)
            quitter = Tool("box", 50, 300)
            screen.blit(soigner.image, soigner.rect)
            screen.blit(quitter.image, quitter.rect)
            
                
            boxes = [soigner, quitter]
        
            write("se soigner",(230,200), 34, "white")
            write("sortir",(230,350), 34, "white")
            
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 : # MOUSEMOTION
                    x,y = event.pos
                    for box in boxes:
                        if box.rect.collidepoint(x,y):
                            if box == soigner:
                                event_talk = True
                                event_anette[1][0] = True
                            elif box == quitter :
                                boucle = True
    
    return ""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def librairie(character):
    global lieu_actuel
    global lieux
    global active
    global activebg
    global new_son
    global hiver
    hiver = True
    lieu_actuel = lieux[9]
    new_son = 1
    change_lieu()
    musique()
    boucle = False
    event_talk = False
    while not boucle:
        screen.blit(activebg, (0,0))
        screen.blit(character.image, (character.rect.x, character.rect.y))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP :
                boucle = True
    lieu_actuel = lieux[3]
    change_lieu()
    new_son = 1
    return""
        
        




#=================================================
#                creation perso
#=================================================






#self.pseudo = mc_var[0]
#self.force = mc_var[1]
#self.defense = mc_var[2]
#self.def_lim = mc_var[3]
#self.pm = mc_var[4]
#self.pm_lim = mc_var[5]
#self.crit = mc_var[6]
#self.esquive = mc_var[7]

#=================================================
#               réglages de base
#=================================================


play = {}
debut = 0

def write(text, rect, police, color):
    if color == "white":
        color_use = (255,255,255)
    elif color == "red":
        color_use = (250,0,0)
    elif color == "green":
        color_use = (111,210,46)
    else:
        color_use = (0,0,0)
    font = pygame.font.Font('freesansbold.ttf', police)
    text_surf = font.render(text, True, color_use, None)
    text_rect = text_surf.get_rect()
    text_rect.center = rect
    screen.blit(text_surf, text_rect)
    
    
def musique():
    global son
    global new_son
    global sound
    global active
    global lieu_actuel
    global lieux
    if son == 1:
        if new_son == 1:
            new_son = 0
            if sound == 1:
                if lieu_actuel == lieux[5]:
                    if active != ost_Hiver:
                        active.stop()
                        active = ost_Hiver
                        active.play(-1)
                elif lieu_actuel == lieux[6]:
                    if active != ost_Hiver:
                        active.stop()
                        active = ost_Hiver
                        active.play(-1)
                else :
                    active.stop()
            if lieu_actuel == lieux[7]:
                active = ost_yggdrasil
                active.play(-1)
            elif lieu_actuel == lieux[0]:
                active = ost_village
                active.play(-1)
            elif lieu_actuel == lieux[1]:
                active = ost_Spring
                active.play(-1)
            elif lieu_actuel == lieux[2]:
                active = ost_Ruines
                active.play(-1)
            elif lieu_actuel == lieux[3]:
                active = ost_citadelle
                active.play(-1)
            elif lieu_actuel == lieux[4]:
                active = ost_autumn
                active.play(-1)
            elif lieu_actuel == lieux[8]:
                active = ost_garden
                active.play(-1)
            elif lieu_actuel == lieux[9]:
                active = ost_library
                active.play(-1)
            sound = 1

def change_lieu():
    global character
    global lieux
    global lieu_actuel
    global new_son
    global activebg
    global debut
    if lieu_actuel == lieux[0]:
        character.vitesse = 3
        activebg = bg_Village
        screen.blit(activebg,(0,0))
    elif lieu_actuel == lieux[1]:
        character.vitesse = 4
        activebg = bg_Spring
        screen.blit(activebg,(0,0))
    elif lieu_actuel == lieux[2]:
        character.vitesse = 3
        activebg = bg_Ruines
        screen.blit(activebg,(0,0))
    elif lieu_actuel == lieux[3]:
        character.vitesse = 3
        activebg = bg_citadelle
        screen.blit(activebg,(0,0))
    elif lieu_actuel == lieux[4]:
        character.vitesse = 4
        activebg = bg_autumn
        screen.blit(activebg,(0,0))
    elif lieu_actuel == lieux[5]:
        character.vitesse = 3
        activebg = bg_winter1
        screen.blit(activebg,(0,0))
    elif lieu_actuel == lieux[6]:
        character.vitesse = 3
        activebg = bg_winter2
        screen.blit(activebg,(0,0))
    elif lieu_actuel == lieux[7]:
        character.vitesse = 4
        activebg = bg_Ygg
        screen.blit(activebg, (0,0))
    elif lieu_actuel == lieux[8]:
        activebg = bg_jardins
        screen.blit(activebg, (0,0))
    elif lieu_actuel == lieux[9]:
        character.vitesse = 3
        activebg = bg_librairie
        screen.blit(activebg, (0,0))
    pygame.display.flip()
    new_son = 1
    debut = 0
    
def touche (x,y):
    return pygame.sprite.spritecollide(x,y.all_char,False,pygame.sprite.collide_mask)
    
def bouge(x):
    vitesse = 10
    if x.char_type != "slime" :
        vitesse = 15
    direct = randint(-vitesse, vitesse)
    rand = random()
    if rand <0.4 and x.rect.x > 0 and direct < 0 :
        x.rect.x += direct
    elif rand <0.4 and x.rect.x < 830 and direct > 0 :
        x.rect.x += direct
    elif rand > 0.4 and x.rect.y > 0 and direct < 0 :
        x.rect.y += direct
    elif rand > 0.4 and x.rect.y < 700 and direct > 0 :
        x.rect.y += direct
  
    
  
important_chest = [False, False, False]

def loot(x):
    global important_chest
    global lieu_actuel
    global lieux
    global gold
    if x.char_type == "tombe":
        if not important_chest[2]:
            print("vous obtenez un 'fragement de pendentif démoniaque' !")
            pendentif_dé = equipment("fragement de pendentif démoniaque", "artéfact", "A", 0, 4, ("feu", None))
            inventory.append(pendentif_dé)
            important_chest[2] = True
    elif x.char_type == "chest":
        if lieu_actuel == lieux[0] :
            if not important_chest[0]:
                print("vous obtenez une 'épée de fer' !")
                épée_fer = equipment("épée de fer", "arme", "C", 10, 0, None)
                inventory.append(épée_fer)
                important_chest[0] = True
            else:
                if random() > 0.5 :
                    more = randint(5,25)
                    print("vous obtenez", more, "gold !")
                    gold += more
        elif lieu_actuel == lieux[1] :
            if not important_chest[1]:
                print("vous obtenez une 'cotte de mailles' !")
                cotte = equipment("cotte de mailles", "armure", "C", 0, 4, None)
                inventory.append(cotte)
                important_chest[1] = True
            else:
                if random() > 0.5 :
                    more = randint(5,25)
                    print("vous obtenez", more, "gold !")
                    gold += more
        if lieu_actuel == lieux[2] :
                if random() > 0.5 :
                    more = randint(5,25)
                    print("vous obtenez", more, "gold !")
                    gold += more
        if lieu_actuel == lieux[3] :
            more = randint(10,30)
            print("vous obtenez", more, "gold !")
            gold += more
    elif x.char_type == "boite":
        if random() > 0.3 :
            more = randint(1,5)
            print("vous obtenez", more, "gold !")
            gold += more
    return ""

def death (character):
    global gold
    global xp
    global activebg
    global active
    global lieu_actuel
    xp = 0
    gold = 0
    boucle = True
    active.stop()
    active = ost_Ruines
    active.play(-1)
    while boucle:
        activebg = bg_death
        screen.blit(activebg, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.type == pygame.QUIT:
                    pygame.quit()
                else:
                    boucle = False
    lieu_actuel = lieux[0]
    print(maison(character))
    change_lieu()
    
    
slime1 = 0
hiver = False
magie = None
    
#=================================================
#              programme principal
#=================================================


def in_game(lvl, xp, gold, lvl_rank):
    global character
    global activebg
    global lieux
    global lieu_actuel
    global new_son
    global debut
    global enter
    global enemy_lvl
    
    global slime_event
    global hiver
    global magie
    
    items = []
    enemies = []
    
    time_1 = perf_counter()
    time_dgts = perf_counter()
    clef = 0
    debut = 0
    objet = (False, None)
    talk = (False, None)
    direction = "haut"
    while clef == 0:
        anette = Tool("anette", 730, 10)
        
        #print(character.rect)
        
        
        time_2 = perf_counter()
        if character.hp <= 0:
            print(death(character))
        up, down, right, left = True, True, True, True
        musique()
        if lieu_actuel == lieux[6]:
            screen.blit(activebg, (0,0)) #L-600,-330,330,530
        else:
            screen.blit(activebg, (0,0))
            if debut == 0:
                items = []
                enemies = []
                if lieu_actuel == lieux[0]:
                    chest = Tool("chest", 80, 200)
                    house = Tool("house", 80,22)
                    boite1 = Tool("boite", 245, 410)
                    boite2 = Tool("boite", 660, 80)
                    enemy_lvl = 1
                    if slime_event == 0 :
                        slime = Chara("slime", 20, 20, 10, None)
                        slime.rect.x, slime.rect.y = 489, 193
                        enemies.append(slime)
                    items.append(chest)
                    items.append(house)
                    items.append(boite1)
                    items.append(boite2)
                elif lieu_actuel == lieux[1]:
                    chest = Tool("chest", 640, 110)
                    eau = Tool("eau", 160, 520)
                    boite = Tool("boite", 400, 620)
                    panneau = Tool("pan", 257, 94)
                    slime1 = Chara("slime", 25, 25, 11, None)
                    slime2 = Chara("slime", 25, 25, 11, None)
                    slime3 = Chara("slime", 25, 25, 11, None)
                    enemy_lvl = randint(1,5)
                    enemies.append(slime1)
                    enemies.append(slime2)
                    enemies.append(slime3)
                    for i in enemies:
                        i.rect.x, i.rect.y = randint(10,800), randint(10,650)
                    items.append(chest)
                    items.append(eau)
                    items.append(boite)
                    items.append(panneau)
                elif lieu_actuel == lieux[2]:
                    chest = Tool("chest", 180, 540)
                    tombe = Tool("tombe", 370, 200)
                    boite = Tool("boite", 100, 200)
                    wall = Tool("wall", 575, 104)
                    wall2 = Tool("wall", 150, 450)
                    slime1 = Chara("slime", 35, 35, 13, None)
                    slime2 = Chara("slime", 35, 35, 13, None)
                    slime3 = Chara("slime", 35, 35, 13, None)
                    enemy_lvl = randint(5,10)
                    enemies.append(slime1)
                    enemies.append(slime2)
                    enemies.append(slime3)
                    for i in enemies:
                        i.rect.x, i.rect.y = randint(10,800), randint(10,650)
                        
                    if event_mimic :
                        mimic = Chara("mimic", 80, 80, 24, None)
                        mimic.image = pygame.image.load('livre.png')
                        enemies.append(mimic)
                        mimic.rect.x, mimic.rect.y = 640, 180
                    else :
                        livre = Tool("livre", 640, 170)
                        
                    items.append(chest)
                    items.append(tombe)
                    items.append(boite)
                    items.append(wall)
                    items.append(wall2)
                elif lieu_actuel == lieux[3]:
                    chest = Tool("chest", 60, 30)
                    house1 = Tool("house", 30, 185)
                    house2 = Tool("shop", 495, 0)
                    panneau = Tool("pan", 345, 245)
                    mairie = Tool("mairie", 555, 260)
                    puit = Tool("puit", 280, 450)
                    tronc = Tool("tronc", 770, 150)
                    freddy = Chara("fred", 120, 120, 32, None)
                    tronc.image = pygame.transform.rotate(tronc.image, 90)
                    items.append(chest)
                    items.append(house1)
                    items.append(house2) 
                    items.append(mairie)
                    items.append(puit)
                    items.append(tronc)
                    items.append(panneau)
                    enemies.append(freddy)
                    freddy.rect.x, freddy.rect.y = 200, 410
                elif lieu_actuel == lieux[4]:
                    tronc = Tool("eau", 600, 260)
                    slime1 = Chara("slime", 50, 50, 15, None)
                    slime2 = Chara("slime", 50, 50, 15, None)
                    slime3 = Chara("slime", 50, 50, 15, None)
                    mimic = Chara("mimic", 80, 80, 22, None)
                    enemy_lvl = randint(10,15)
                    enemies.append(slime1)
                    enemies.append(slime2)
                    enemies.append(slime3)
                    enemies.append(mimic)
                    for i in enemies:
                        i.rect.x, i.rect.y = randint(10,800), randint(10,650)
                    items.append(tronc)
                elif lieu_actuel == lieux[5]:
                    slime1 = Chara("slime", 60, 60, 20, None)
                    slime2 = Chara("slime", 60, 60, 20, None)
                    slime3 = Chara("slime", 60, 60, 20, None)
                    poison = Tool("poison", 550, 250)
                    enemy_lvl = randint(15,20)
                    enemies.append(slime1)
                    enemies.append(slime2)
                    enemies.append(slime3)
                    items.append(poison)
                    for i in enemies:
                        i.rect.x, i.rect.y = randint(10,800), randint(10,650)
                        
                    if event_dragon :
                        dragon = Chara("dragon", 180,180, 35, None)
                        enemies.append(dragon)
                        dragon.rect.x, dragon.rect.y = 640, 180
                elif lieu_actuel == lieux[6]:
                    slime1 = Chara("slime", 60, 60, 20, None)
                    slime2 = Chara("slime", 60, 60, 20, None)
                    slime3 = Chara("slime", 60, 60, 20, None)
                    enemy_lvl = randint(15,20)
                    enemies.append(slime1)
                    enemies.append(slime2)
                    enemies.append(slime3)
                    for i in enemies:
                        i.rect.x, i.rect.y = randint(10,800), randint(10,650)
                elif lieu_actuel == lieux[7]:
                    chest = Tool("chest", 180, 540)
                    bourgeon = Tool("bourgeon", 410, 440)
                    for i in enemies:
                        i.rect.x, i.rect.y = (410, 440)
                    items.append(chest)
                    items.append(bourgeon)
                elif lieu_actuel == lieux[9]:
                    chest = Tool("chest", 500, 370)
                    livre = Tool("livre", 330, 330)
                    boite1 = Tool("boite", 345, 0)
                    boite2 = Tool("boite", 0, 0)
                    bib1 = Tool("bib", 300, 230)
                    bib2 = Tool("bib", 300, 420)
                    bib3 = Tool("bib2", 790, 0)
                    bib4 = Tool("bib", 200, 0)
                    bib5 = Tool("bib", 400, 0)
                    bib6 = Tool("bib", 523, 0)
                    bib7 = Tool("bib", 646, 0)
                    bib8 = Tool("bib", 423, 230)
                    bib9 = Tool("bib", 546, 230)
                    bib10 = Tool("bib", 546, 420)
                    bib11 = Tool("bib2", 790, 123)
                    bib12 = Tool("bib2", 790, 246)
                    bib13 = Tool("bib2", 790, 369)
                    bib14 = Tool("bib", 77, 0)
                    chest.image = pygame.transform.rotate(chest.image, 90)
                    items.append(chest)
                    items.append(livre)
                    items.append(boite1)
                    items.append(boite2)
                    items.append(bib1) 
                    items.append(bib2) 
                    items.append(bib3) 
                    items.append(bib4)
                    items.append(bib5)
                    items.append(bib6)
                    items.append(bib7)
                    items.append(bib8)
                    items.append(bib9)
                    items.append(bib10)
                    items.append(bib11)
                    items.append(bib12)
                    items.append(bib13)
                    items.append(bib14)
            else:
                if lieu_actuel != lieux[0]:
                    for i in enemies:
                        if i.char_type != "mimic" and i.char_type != "dragon" and i.char_type != "fred" :
                            bouge(i)
            debut = 1
            
            
        for i in items:
            screen.blit(i.image, i.rect)
        for i in enemies:
            screen.blit(i.image, i.rect)
        if objet[0] == True:
            screen.blit(enter, objet[1].rect)
            
        if lieu_actuel != lieux[8]:
            screen.blit(character.image, character.rect)
            character.health_bar(screen, "health")
            character.health_bar(screen, "mp")
            screen.blit(anette.image, anette.rect)
            if character.pm_lim > 0 :
                screen.blit(magic, (730, 600))
                if magie == "heal" or magie == None:
                    magie_act = heal
                elif magie == "fireball":
                    magie_act = fireball
                screen.blit(magie_act, (742,615))
            if time_2 - time_1 <= 2:
                screen.blit(box_lieux, (250, 550))
                write(lieu_actuel.nom,(430,600), 34, "white")
            if talk[0]:
                screen.blit(box_text, (200, 350))
                if talk[1] == "tombe" :
                    write("C'est une tombe, des inscriptions effacées", (400, 600), 14, "black")
                    write("par le temps y sont visibles.              ", (400, 630), 14, "black")
                elif talk[1] == "pan" :
                    if lieu_actuel == lieux[1]:
                        write("Citadelle     >", (400, 600), 14, "black")
                        write("Ruines        ^", (400, 630), 14, "black")
                    elif lieu_actuel == lieux[3]:
                        write("Champs d'automne     >", (400, 600), 14, "black")
                        write("Sentier enneigé      v", (400, 630), 14, "black")
            if lieu_actuel == lieux[5] or lieu_actuel == lieux[6]:
                if équipé[1] != None :
                    if équipé[1].bonus != None :
                        if not "gel" in équipé[1].bonus:
                            if int(time_2 - time_dgts) >= 1:
                                time_dgts = perf_counter()
                                character.hp -= 2
                else :
                    if int(time_2 - time_dgts) >= 1:
                        time_dgts = perf_counter()
                        character.hp -= 2
                        
        pygame.display.flip()
        
        
        stat_item = False
        talk = (False, None)
        for i in items:
            if touche(character, i):
                stat_item = True
                if i.char_type == "house" or i.char_type == "chest" or i.char_type == "mairie" or i.char_type == "shop" or i.char_type == "livre" or i.char_type == "bourgeon" :
                    objet = (True, i)
                elif i.char_type == "tombe":
                    loot(i)
                    talk = (True, "tombe")
                elif i.char_type == "pan":
                    loot(i)
                    talk = (True, "pan")
                elif i.char_type == "bourgeon":
                    talk = (True, "bourgeon")
                if i.char_type == "poison" :
                    character.hp -= 0.25
                else :
                    if character.rect.y <= i.rect.y :
                        down = False
                    else:
                        up = False
                    if character.rect.x >= i.rect.x :
                        left = False
                    else:
                        right = False
        if not stat_item:
            objet = (False, None)
        for i in enemies:
            if i.char_type == "alraune":
                boss(i, character)
            elif touche(character, i) :
                if lieu_actuel.diff == 0:
                    print(battle(randint(1,5), i, character))
                    change_lieu()
                    debut = 0
                    slime_event = 1
                else:
                    if i.char_type == "mimic":
                        if lieu_actuel == lieux[2]:
                            enemy_lvl = 25
                        else:
                            enemy_lvl += 10
                    print(battle(enemy_lvl, i, character))
                    change_lieu()
                    debut = 0
                    
                    
        if lieu_actuel == lieux[0]:
            if character.rect.x >= 755:
                lieu_actuel = lieux[1]
                change_lieu()
                character.rect.x = 11
                time_1 = perf_counter()
            if (character.rect.y <= 180 or character.rect.y >= 210) and character.rect.x >= 410 and character.rect.x <= 500 :
                right = False
            if (character.rect.y <= 180 or character.rect.y >= 210) and character.rect.x >= 500 and character.rect.x <= 570 :
                left = False
                
        elif lieu_actuel == lieux[1]:
            if character.rect.x <= 10:
                lieu_actuel = lieux[0]
                change_lieu()
                character.rect.x = 754
                time_1 = perf_counter()
            elif character.rect.y <= 10:
                lieu_actuel = lieux[2]
                change_lieu()
                character.rect.y = 639
                time_1 = perf_counter()
            elif character.rect.x >= 755:
                lieu_actuel = lieux[3]
                change_lieu()
                character.rect.x = 17
                character.rect.y = 355
                time_1 = perf_counter()
                
        elif lieu_actuel == lieux[2]:
            if character.rect.y >= 640:
                lieu_actuel = lieux[1]
                change_lieu()
                character.rect.y = 11
                time_1 = perf_counter()
                
        elif lieu_actuel == lieux[3]:
            if character.rect.y >= 640:
                lieu_actuel = lieux[5]
                change_lieu()
                character.rect.y, character.rect.x = 11,80
                time_1 = perf_counter()
            elif character.rect.x >= 755:
                lieu_actuel = lieux[4]
                change_lieu()
                character.rect.x = 11
                time_1 = perf_counter()
            elif character.rect.x <= 10:
                lieu_actuel = lieux[1]
                change_lieu()
                character.rect.x = 754
                time_1 = perf_counter()
                
        elif lieu_actuel == lieux[4]:
            if character.rect.x >= 755:
                lieu_actuel = lieux[4]
                change_lieu()
                character.rect.x = 11
                time_1 = perf_counter()
            elif character.rect.x <= 10:
                lieu_actuel = lieux[3]
                change_lieu()
                character.rect.x = 743
                character.rect.y = 169
                time_1 = perf_counter()
            elif character.rect.x < 715 and character.rect.x > 645 and character.rect.y <= 5:
                lieu_actuel = lieux[8]
                change_lieu()
                time_1 = perf_counter()
                
        elif lieu_actuel == lieux[5]:
            if character.rect.y <= 10:
                lieu_actuel = lieux[3]
                change_lieu()
                character.rect.x = 452
                character.rect.y = 642
                time_1 = perf_counter()
            elif character.rect.x >= 755:
                lieu_actuel = lieux[6]
                change_lieu()
                character.rect.x = 11
                time_1 = perf_counter()
                
        elif lieu_actuel == lieux[6]:
            if character.rect.x <= 10:
                lieu_actuel = lieux[5]
                change_lieu()
                character.rect.x = 754
                time_1 = perf_counter()
            elif character.rect.y >= 640:
                lieu_actuel = lieux[7]
                change_lieu()
                character.rect.y = 11
                time_1 = perf_counter()
                
        elif lieu_actuel == lieux[7]:
            if character.rect.y <= 10:
                lieu_actuel = lieux[6]
                change_lieu()
                character.rect.y = 639
                time_1 = perf_counter()
            
        elif lieu_actuel == lieux[9]:
            if character.rect.x <= 10:
                lieu_actuel = lieux[3]
                character.rect.x, character.rect.y = 485, 360
                change_lieu()
                time_1 = perf_counter()
                
                
        if (play.get(pygame.K_UP) or play.get(pygame.K_z)) and character.rect.y > 0 and up:
            character.rect.y -= character.vitesse -0.4
            direction = "haut"
        elif (play.get(pygame.K_DOWN) or play.get(pygame.K_s)) and character.rect.y < 655 and down:
            character.rect.y = character.rect.y + character.vitesse
            direction = "bas"
        elif (play.get(pygame.K_RIGHT) or play.get(pygame.K_d)) and character.rect.x < 765 and right:
            character.rect.x = character.rect.x + character.vitesse
            direction = "droite"
        elif (play.get(pygame.K_LEFT) or play.get(pygame.K_q)) and character.rect.x > 0 and left:
            character.rect.x -= character.vitesse - 0.4
            direction = "gauche"
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                arme = Attacks(character, character.weapon_type, character.rect.x + 20, character.rect.y - 70)
                x,y = event.pos
                if anette.rect.collidepoint(x,y):
                    anette_help()
                elif direction == "droite":
                    arme.image = pygame.transform.rotate(arme.image, -90)
                    arme.rect.x, arme.rect.y = character.rect.x + 60, character.rect.y +20 
                elif direction == "gauche":
                    arme.image = pygame.transform.rotate(arme.image, 90)
                    arme.rect.x, arme.rect.y = character.rect.x - 70, character.rect.y +20 
                elif direction == "bas":
                    arme.image = pygame.transform.rotate(arme.image, 180)
                    arme.rect.y = character.rect.y + 50 
                screen.blit(arme.image, (arme.rect.x, arme.rect.y))
                pygame.display.flip()
                a_touché = False
                for i in items :
                    if i.char_type == "boite" or i.char_type == "tronc" :
                        if touche(arme, i):
                            a_touché = True
                            sound_crush.play(0)
                            print(loot(i))
                            items.remove(i)
                for i in enemies :
                    if touche(arme, i):
                        a_touché = True
                        sound_critical.play(0)
                        slime_event = 1
                        if i.char_type != "alraune" :
                            i.hp -= character.force
                            if i.char_type == "mimic":
                                if lieu_actuel == lieux[2]:
                                    enemy_lvl = 25
                                else:
                                    enemy_lvl += 10
                        else :
                            i.hp -= character.dgts
                        print(battle(enemy_lvl, i, character))
                if not a_touché :
                    sound_slash.play(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if magie == "heal" :
                    if character.pm >= 4 :
                        character.pm -= 4
                        bonus_pv = 25
                        if character.hp + bonus_pv > character.hp_lim :
                            bonus_pv = character.hp + bonus_pv - character.hp_lim
                        character.hp += bonus_pv
                        screen.blit(heal, (character.rect.x, character.rect.y))
                        pygame.display.flip()
            elif event.type == event.type == pygame.KEYUP:
                play[event.key] = False
                if event.key == pygame.K_SPACE:
                    if character.pm_lim > 0:
                        if magie == None or magie == "fireball":
                            magie = "heal"
                        elif magie == "heal" :
                            magie = "fireball"
                elif event.key == pygame.K_RETURN and objet[0]:
                    if objet[1].char_type == "chest":
                        print(loot(objet[1]))
                        items.remove(objet[1])
                        objet = (False, None)
                    elif objet[1].char_type == "house":
                        maison(character)
                    elif objet[1].char_type == "mairie":
                        lieu_actuel = lieux[9]
                        character.rect.x, character.rect.y = 15, 300
                        change_lieu()
                        time_1 = perf_counter()
                    elif objet[1].char_type == "shop":
                        shop()
                    elif objet[1].char_type == "livre":
                        hiver = True
                    elif objet[1].char_type == "bourgeon":
                        fog1 = Tool("fog", 440, 440)
                        screen.blit(fog1.image, fog1.rect)
                        pygame.display.flip()
                        sleep(0.5)
                        fog2 = Tool("fog", 410, 480)
                        fog3 = Tool("fog", 455, 495)
                        screen.blit(fog2.image, fog2.rect)
                        screen.blit(fog3.image, fog3.rect)
                        pygame.display.flip()
                        sleep(0.5)
                        fog4 = Tool("fog", 400, 525)
                        fog5 = Tool("fog", 445, 530)
                        fog5 = Tool("fog", 425, 500)
                        screen.blit(fog4.image, fog4.rect)
                        screen.blit(fog5.image, fog5.rect)
                        pygame.display.flip()
                        sleep(0.5)
                        screen.blit(activebg, (0,0))
                        items.remove(bourgeon)
                        for i in items:
                            screen.blit(i.image, i.rect)
                        alraune = Chara("alraune", 200, 200, 40, None)
                        enemies.append(alraune)
                        for i in enemies:
                            screen.blit(i.image, i.rect)
                        pygame.display.flip()
                elif event.key == pygame.K_ESCAPE:
                    clef = 1
                    accueil(lvl, xp, gold, lvl_rank)
            elif event.type == pygame.KEYDOWN:
                if lieu_actuel == lieux[8]:
                    lieu_actuel = lieux[4]
                    change_lieu()
                    character.rect.y = 11
                play[event.key] = True
            elif event.type == pygame.QUIT:
                clef =1
                pygame.quit()
                
                
def accueil(lvl, xp, gold, lvl_rank):
    what = ""
    global character
    global activebg
    global son
    global new_son
    global sound
    global active
    global daycounter
    global day
    global Character_class
    global base
    active.stop()
    active = ost_house
    active.play(-1)
    activebg = bg_house
    while what != "stop":
        
        while perf_counter() > daycounter:
            daycounter = daycounter + 90
            if daycounter % 180 == 0:
                hour = "night"
            else:
                hour = "day"
                day = day + 1
                
                
        screen.blit(activebg,(0,0))
        game = Tool("box", 30, 150)
        inventaire = Tool("box", 30, 300)
        équiper_im = Tool("box", 30, 450)
        temps = Tool("box", 30, 600)
        
        status = Tool("box", 440, 150)
        points = Tool("box", 440, 300)
        lieu = Tool("box", 440, 450)
        credit = Tool("box", 440, 600)
        
        screen.blit(game.image, game.rect)
        screen.blit(inventaire.image, inventaire.rect)
        screen.blit(équiper_im.image, équiper_im.rect)
        screen.blit(temps.image, temps.rect)
        
        screen.blit(status.image, status.rect)
        screen.blit(points.image, points.rect)
        screen.blit(lieu.image, lieu.rect)
        screen.blit(credit.image, credit.rect)
        boxes = [game, inventaire, équiper_im, temps, status, points, lieu, credit]
        
        write("game",(220,200), 34, "white")
        write("inventaire",(220,350), 34, "white")
        write("équiper",(220,500), 34, "white")
        write("temps",(220,650), 34, "white")
        
        write("stats",(615,200), 34, "white")
        write("points",(615,350), 34, "white")
        write("lieux",(615,500), 34, "white")
        write("credits",(615,650), 34, "white")
        

        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 : # MOUSEMOTION
                x,y = event.pos
                for box in boxes:
                    if box.rect.collidepoint(x,y):
                        if box == game:
                            what = "stop"
                        elif box == inventaire :
                            print(" Quel inventaire voulez vous vérifier ?")
                            print("  0 équipements     1 objets cons    2 objets spéciaux")
                            eq = int(input())
                            if eq == 0:
                                print(recherche_inv(inventory))
                            elif eq == 1:
                                print("non fini")  ############################
                            elif eq == 2:
                                print(inv_spe)
                        elif box == équiper_im :
                            print(équiper(inventory, équipé))
                            stats_load(character)
                        elif box == temps:
                            print(time())
                        elif box == status:
                            print(stats(character))
                        elif box == points:
                            print(character.points())
                        elif box == lieu:
                            var = lieu_actuel
                            print(lieu_actuel)
                            print(voyage(lieux))
                            if lieu_actuel != var :
                                what = "stop"
                        elif box == credit:
                            print(credits())
        
        
        
        """
        elif what == "music":
            if sound == 1:
                active.stop()
                sound = 0
                son = 0
            elif sound == 0:
                active.play(-1)
                sound = 1
                son = 1
        elif what == "cheat":
            cheat = input("cheatcode: ")
            if cheat == "tensura":
                print("force, or, hp")
                cheat_1 = input("que voulez vous améliorer: ")
                if cheat_1 == "force":
                    force = int(input("quelle valeur donner à la force: "))
                elif cheat_1 == "or":
                    gold = int(input("quelle valeur donner à votre or: "))
                elif cheat_1 == "hp":
                    pv = int(input("quelle valeur donner à vos hp: "))
            else:
                print("wrong cheat-code")
         """
                
                
                
    new_son = 1
    change_lieu()
    return in_game(lvl, xp, gold, lvl_rank)



def creation_perso():
    global activebg
    global active
    active.play(-1)
    boucle_end = False
    name = ""
    while not boucle_end :
        
        screen.blit(activebg,(0,0))
        valider = Tool("box", 225, 450)
        screen.blit(valider.image, valider.rect)
        
        write(name,(410,185), 34, "white")
        write("valider",(410,500), 34, "white")
        

        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 : # MOUSEMOTION
                x,y = event.pos
                if valider.rect.collidepoint(x,y):
                    boucle_end = True
            elif event.type == event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    new_name = ""
                    for i in range(len(name)-1):
                        new_name += name[i]
                    name = new_name
                elif len(name) < 24:
                    if event.key == pygame.K_SPACE:
                        name += " "
                    elif event.key == pygame.K_a:
                        name += "a"
                    elif event.key == pygame.K_b:
                        name += "b"
                    elif event.key == pygame.K_c:
                        name += "c"
                    elif event.key == pygame.K_d:
                        name += "d"
                    elif event.key == pygame.K_e:
                        name += "e"
                    elif event.key == pygame.K_f:
                        name += "f"
                    elif event.key == pygame.K_g:
                        name += "g"
                    elif event.key == pygame.K_h:
                        name += "h"
                    elif event.key == pygame.K_i:
                        name += "i"
                    elif event.key == pygame.K_j:
                        name += "j"
                    elif event.key == pygame.K_k:
                        name += "k"
                    elif event.key == pygame.K_l:
                        name += "l"
                    elif event.key == pygame.K_m:
                        name += "m"
                    elif event.key == pygame.K_n:
                        name += "n"
                    elif event.key == pygame.K_o:
                        name += "o"
                    elif event.key == pygame.K_p:
                        name += "p"
                    elif event.key == pygame.K_q:
                        name += "q"
                    elif event.key == pygame.K_r:
                        name += "r"
                    elif event.key == pygame.K_s:
                        name += "s"
                    elif event.key == pygame.K_t:
                        name += "t"
                    elif event.key == pygame.K_u:
                        name += "u"
                    elif event.key == pygame.K_v:
                        name += "v"
                    elif event.key == pygame.K_w:
                        name += "w"
                    elif event.key == pygame.K_x:
                        name += "x"
                    elif event.key == pygame.K_y:
                        name += "y"
                    elif event.key == pygame.K_z:
                        name += "z"
                        
                    
    return name           

    

character = Chara("mc", 60, 60, 10, (creation_perso(), 10, 0, 0, 0, 0, 1, 1))
active.stop()
activebg = bg_Village
in_game(lvl, xp, gold, lvl_rank)
       

pygame.quit()       