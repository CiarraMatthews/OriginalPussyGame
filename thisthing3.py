import pygame, sys, time
from texturescript import *
from mechanics import *
#import random





x = random.randint(1,11)


#def animate():
#    global Walkcount
 #   window.fill(gold)

 #   if Walkcount + 1 >27:
 #       Walkcount = 0
##        win.blit(punchem[Walkcount//3], (1000,370))
##        Walkcount += 1
##    pygame.display.update()
##
##class foeinfo():
##    foehealth = 100
##
##    def gethealth():
##        global foehealth
##        return foehealth
##
##    def resethealth():
##        global foehealth
##        foehealth = 100
##
##    def changehealth(n):
##        global foehealth
##        foehealth += n
#global foehealth = 100

#from guiing import *
#from globby import *

#Colors
pink = (203, 51, 137)
gold = (203, 162, 51)
lpink = (249, 71, 142)
lgold = (246, 211, 50)
black = (0, 0, 0)
white = (255, 255, 255)

font = pygame.font.Font("Baskies.ttf", 30)



class Scene():
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        print("Hmmm.") 

    def update(self):
        print("Hmmm.")
        
    def render(self, window):
        print("Hmmm.") 
    
    def switchscene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.switchscene(None)

def create_window():
    pygame.init()
    global window, window_height, window_width, window_title
    window_height, window_width = 800, 1400
    window_title = 'First Game'
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def run(Starting):
    create_window()
    clock = pygame.time.Clock()
    #clock.tick(27)
    pygame.time.delay(50)

    c_scene = Starting

    while c_scene != None:
        pressed_keys = pygame.key.get_pressed()
    
        #Event filtering
        filtered_events = []
        for event in pygame.event.get():
            try_quit = False
            if event.type == pygame.QUIT:
                try_quit = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT]
                if event.key == pygame.K_ESCAPE:
                    try_quit = True
            if try_quit:
                c_scene.Terminate()
            
            else:
                filtered_events.append(event)

        c_scene.ProcessInput(filtered_events, pressed_keys)
        c_scene.update()
        c_scene.render(window)

        c_scene = c_scene.next

        pygame.display.flip()
        clock.tick(3)


class Starting(Scene):
    def __init__(self):
        Scene.__init__(self)
        #self.health = 100
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.switchscene(Map())
    
    def update(self):
        pass

    def render(self, window):
        window.blit(bg, (0, 0,))
        text = font.render("Press Enter to Start", True, black)
        window.blit(text, (window_width/2, window_height/2))

        mouse = pygame.mouse.get_pos()
        if 245+100 > mouse [0] > 150 and 498+35 > mouse [1] > 450:
            window.blit(start_button2, (245,490))
        else:
            window.blit(start_button, (245,490))
        #print (mouse)
        if 850+100 > mouse [0] > 150 and 498+35 > mouse [1] > 450:
            window.blit(quit_button2, (850,490))
        else:
            window.blit(quit_button, (850,490))

class Map(Scene):
    def __init__(self):
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.switchscene(Battle())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.switchscene(Map2())
        
    def update(self):
        pass

    def render(self, window):
        window.blit(mapplz, (0, 0,))
        text2 = font.render("Choose where you want to go. The Crime filled streets or the store. C for crime. S for Store", True, white)
        window.blit(text2, (100, 700))

class Map2(Scene):
    def __init__(self):
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                foehealth = 100
                self.switchscene(Battle())
        
    def update(self):
        pass

    def render(self, window):
        window.blit(mapplz, (0, 0,))
        text0 = font.render("Sorry, the shop is closed", True, white)
        window.blit(text0, (100, 670))
        text2 = font.render("Choose where you want to go. The Crime filled streets or the store. C for crime.", True, white)
        window.blit(text2, (100, 700))

class Battle(Scene):    
    def __init__(self):
        #foeinfo.resethealth()
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.switchscene(Battle_attack())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.switchscene(Battle_items())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.switchscene(Battle_taunts())
        
    def update(self):
        pass

    def render(self, window):
        window.fill(gold)
        window.blit(cat,(1000,370))
        text = font.render("Press a for attack and i for items and t for taunt", True, black)
        window.blit(text, (100, 750))
        window.blit(attackb, (800, 705))
        window.blit(items, (950, 710))
        window.blit(taunt, (1100, 710))
        window.blit(dudebroskyguy, (200,100))
        #pygame.draw.rect(window, (255, 0, 0))
        #window.blit(shooter,(100,370))

class Battle_attack(Scene):
    def __init__(self):
        Scene.__init__(self)
        #self.health = 100

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.switchscene(Battle_punch())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                self.switchscene(Battle_kick())
        
    def update(self):
        pass

    def render(self, window):
        window.fill(gold)
        window.blit(cat,(1000,370))
        window.blit(punch1,(800,710))
        window.blit(kick,(950,710))
        text = font.render("Press p to punch or k to kick", True, black)
        window.blit(text, (100, 750))
        #window.blit(items, (700, 700))
        #window.blit(taunt, (900, 700))
        window.blit(dudebroskyguy, (200,100))
        
class Battle_punch(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.width = 644
        self.height = 570
        self.images = hit
        self.numImages = 9
        self.cImage = 0
        #self.health = 100

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.switchscene(Battle())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                self.switchscene(Battle_items())
        
        
    def update(self):
        if (self.cImage>=self.numImages-1):
            selfcImage = 0
        else:
            self.cImage+=1
            

    def render(self, window):
        #animate()
        #punchem = [cf2, cf3, cf4, cf5, cf6, cf7, cf8]
        window.fill(gold)
        #window.blit(punchem,(1000, 370))
        window.blit(self.images, (300, 200), (self.cImage*self.width, 0, self.width, self.height))
        #window.blit(cat,(1000,370))
        text = font.render("Press enter to continue", True, black)
        window.blit(text, (100, 750))
        if x >= 6:
            text = font.render("Critical hit!", True, black)
            window.blit(text, (100, 700))
        elif x <= 5 and x >= 2:
         #   foeinfo.changehealth(-35)
            text = font.render("Nice shot", True, black)
            window.blit(text, (100, 700))
        elif  foehealth <= 0:
            text = font.render("Your oppenent has been defeated", True, black)
            window.blit(text, (100, 700))
        else:
            text = font.render("Oh no! You missed!", True, black)
  #      print (foehealth)
        #window.blit(items, (700, 700))
        #window.blit(taunt, (900, 700))
        #window.blit(dudebroskyguy, (200,100))

class Battle_kick(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.width = 644
        self.height = 570
        self.images = hit
        self.numImages = 9
        self.cImage = 0
        #self.health = 100

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.switchscene(Battle())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                self.switchscene(Battle_items())
        
        
    def update(self):
        if (self.cImage>=self.numImages-1):
            selfcImage = 0
        else:
            self.cImage+=1
            

    def render(self, window):
        #animate()
        #punchem = [cf2, cf3, cf4, cf5, cf6, cf7, cf8]
        window.fill(gold)
        #window.blit(punchem,(1000, 370))
        window.blit(self.images, (300, 200), (self.cImage*self.width, 0, self.width, self.height))
        #window.blit(cat,(1000,370))
        text = font.render("Press enter to continue", True, black)
        window.blit(text, (100, 750))
        if x >= 6:
            text = font.render("Critical hit!", True, black)
            window.blit(text, (100, 700))
        elif x <= 5 and x >= 2:
         #   foeinfo.changehealth(-35)
            text = font.render("Nice shot", True, black)
            window.blit(text, (100, 700))
        elif  foehealth <= 0:
            text = font.render("Your oppenent has been defeated", True, black)
            window.blit(text, (100, 700))
        else:
            text = font.render("Oh no! You missed!", True, black)
  #      print (foehealth)
        #window.blit(items, (700, 700))
        #window.blit(taunt, (900, 700))
        #window.blit(dudebroskyguy, (200,100))
        
class Battle_taunts(Scene):
    def __init__(self):
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.switchscene(Battle_attack())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.switchscene(Battle_items())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.switchscene(Battle_taunts())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                self.switchscene(taunt1())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                self.switchscene(taunt2())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                self.switchscene(taunt3())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                self.switchscene(taunt4())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                self.switchscene(taunt5())     
        
        
    def update(self):
        pass

    def render(self, window):
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
        window.fill(gold)
        window.blit(cat,(1000,370))
        text = font.render("Pick a number from 1 to 5, and press it", True, black)
        window.blit(text, (100, 700))
        window.blit(attackb, (800, 705))
        window.blit(items, (950, 710))
        window.blit(taunt, (1100, 710))
        window.blit(dudebroskyguy, (200,100))

class taunt1(Scene):
    def __init__(self):
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.switchscene(Battle_attack())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.switchscene(Battle_items())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.switchscene(Battle_taunts())
        
    def update(self):
        pass

    def render(self, window):
        window.fill(gold)
        window.blit(cat,(1000,370))
        text1 = font.render("It is scary to think people like you can vote", True, black)
        window.blit(text1, (100, 730))
        window.blit(attackb, (800, 705))
        window.blit(items, (950, 710))
        window.blit(taunt, (1100, 710))
        window.blit(dudebroskyguy, (200,100))

class taunt2(Scene):
    def __init__(self):
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.switchscene(Battle_attack())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.switchscene(Battle_items())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.switchscene(Battle_taunts())
        
    def update(self):
        pass

    def render(self, window):
        window.fill(gold)
        window.blit(cat,(1000,370))
        text1 = font.render("This pussy fights back", True, black)
        window.blit(text1, (100, 730))
        window.blit(attackb, (800, 705))
        window.blit(items, (950, 710))
        window.blit(taunt, (1100, 710))
        window.blit(dudebroskyguy, (200,100))

class taunt3(Scene):
    def __init__(self):
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.switchscene(Battle_attack())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.switchscene(Battle_items())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.switchscene(Battle_taunts())
        
    def update(self):
        pass

    def render(self, window):
        window.fill(gold)
        window.blit(cat,(1000,370))
        text1 = font.render("Grow a pair... of ovaries", True, black)
        window.blit(text1, (100, 730))
        window.blit(attackb, (800, 705))
        window.blit(items, (950, 710))
        window.blit(taunt, (1100, 710))
        window.blit(dudebroskyguy, (200,100))

class taunt4(Scene):
    def __init__(self):
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.switchscene(Battle_attack())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.switchscene(Battle_items())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.switchscene(Battle_taunts())
        
    def update(self):
        pass

    def render(self, window):
        window.fill(gold)
        window.blit(cat,(1000,370))
        text1 = font.render("Your face, your butt. What is the difference", True, black)
        window.blit(text1, (100, 730))
        window.blit(attackb, (800, 705))
        window.blit(items, (950, 710))
        window.blit(taunt, (1100, 710))
        window.blit(dudebroskyguy, (200,100))

class taunt5(Scene):
    def __init__(self):
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.switchscene(Battle_attack())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.switchscene(Battle_items())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.switchscene(Battle_taunts())
        
    def update(self):
        pass

    def render(self, window):
        window.fill(gold)
        window.blit(cat,(1000,370))
        text1 = font.render("FUS RO DAH", True, black)
        window.blit(text1, (100, 730))
        window.blit(attackb, (800, 705))
        window.blit(items, (950, 710))
        window.blit(taunt, (1100, 710))
        window.blit(dudebroskyguy, (200,100))

class Battle_items(Scene):
    def __init__(self):
        Scene.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.switchscene(Battle_attack())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.switchscene(Battle_items())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.switchscene(Battle_taunts())
        
    def update(self):
        pass

    def render(self, window):
        window.fill(gold)
        window.blit(cat,(1000,370))
        text = font.render("Press a for attack and i for items and t for taunt", True, black)
        texti = font.render("Sorry, no items, yet", True, black)
        window.blit(texti, (100, 730))
        window.blit(text, (100, 700))
        window.blit(attackb, (800, 705))
        window.blit(items, (950, 710))
        window.blit(taunt, (1100, 710))
        window.blit(dudebroskyguy, (200,100))

#while y != True:
 #   Battle()
  #  if foehealth <= 0:
   #     y = True
    #    text = font.render("Your oppenent has been defeated", True, black)
     #   window.blit(text, (100, 700))
        
run(Starting())
