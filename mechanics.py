import pygame
import random

pygame.init()

x = random.randint(1,11)

foehealth = 100
cathealth = 100

font = pygame.font.Font("Baskies.ttf", 30)

pink = (203, 51, 137)
gold = (203, 162, 51)
lpink = (249, 71, 142)
lgold = (246, 211, 50)
black = (0, 0, 0)
white = (255, 255, 255)

#def crit(self):
 #   return (self.health - 55)

#def punch(self):
 #   def __init__(self,health = 100):
  #      self.health = z
   # if x >= 9:
    #    crit()
        #self.health -= 55
     #   text1 = font.render("Critical hit!", True, black)
      #  window.blit(text, (100, 700))
    #elif x <= 8 and x >=2:
     #   self.health -= 35
     #   text2 = font.render("Nice shot", True, black)
      #  window.blit(text, (100, 700))
    #else:
     #   print (self.health)
      #  text3 = font.render("Oh no! You missed!", True, black)
       # window.blit(text, (100, 700))

#def kick:
    
def taunts():
    if x == 1:
        text2 = font.render("It is scary to think people like you can vote", True, black)
        window.blit(text2, (100, 700))
    elif x == 2:
        text4 = font.render("This pussy fights back", True, black)
        window.blit(text4, (100, 700))
    elif x > 3 and x < 5:
        text5 = font.render("Grow a pair... of ovaries", True, black)
        window.blit(text5, (100, 700))
    elif x > 6 and x < 7:
        text6 = font.render("Your face, your butt. What is the difference", True, black)
        window.blit(text6, (100, 700))
    else:
        text7 = font.render("I would like to see things from your point of view", True, black)
        window.blit(text7, (100, 700))
