import random
import math
x = random.randint(1,11)
y = False

print 'Preliminary Pussy'

print 'In this city full of crime, one cat cleans up these streets, by punching people'
print 'Choose where you want this hero to go next. North, East, West?'

foehealth = 100
cathealth = 100

def choose():
    choice = raw_input('Pick a location on the map: ').lower()
    if choice == str('north'):
        print 'North it is'
        north()
    elif choice == str('south'):
       print 'Nobody told you to pick South. Try again.'
    else:
        print 'Try again.'

def north():
    print 'You are going to have to fight the Don of New York'
    battle()


def battle():
    print 'Your attacker approaches'
    print 'Get ready!'
    pick = raw_input('Pick attack, items or taunt: ')
    if pick == str('attack'):
        attack()
    if pick == str('items'):
        item()
    if pick == str('taunt'):
        taunt()

def taunt():
    if x == 1:
        print 'This pussy fights back'
        battle()
    elif x == 2:
        print 'It is scary to think people like you are allowed to vote'
        battle()
    elif x > 3 and x < 5:
        print 'I would like to see things from your point of view..'
        print 'but I cannot stick my head that far up my arse'
        battle()
    elif x > 6 and x < 7:
        print 'Your face, your butt. What is the difference?'
    elif x > 8 and x < 9:
        print 'Grow a pair... of ovaries'
    elif x == 10:
        print 'Why do you cater to a shrinking demographic?'

def attack():
    global foehealth
    wattack = raw_input('Pick either punch or kick: ').lower()
    if wattack == str('punch'):
        if x >= 9:
            print 'Critical hit! The punch landed'
            foehealth = foehealth - 50
            print foehealth
        elif x <= 8 and x >= 2:
            print 'The punch landed'
            foehealth = foehealth - 35
            print foehealth
        else:
            print 'Oh no! You missed'
    if wattack == str('kick'):
        if x >= 9:
            print 'Wow! The kick landed 10 times!'
            foehealth = foehealth - 70
            print foehealth
        elif x <= 8 and x>= 6:
            print 'The kick landed 5 times!'
            foehealth = foehealth - 28
            print foehealth
        elif x <= 5 and x >= 3:
            print 'The kick landed 5 times!'
            foehealth = foehealth - 14
            print foehealth
        elif x <= 2 and x >=1:
            print 'The kick landed'
            foehealth = foehealth - 7
            print foehealth

def opponent():
    global cathealth


def item():
    print 'Sorry. No items in inventory yet'
    battle()


choose()


while y != True:
        battle()
        if foehealth <= 0:
            y = True
            print 'Your opponent has been defeated'
            print 'You got another criminal off these streets.'
            print 'People everywhere are safer now'
