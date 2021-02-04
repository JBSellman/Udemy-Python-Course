# cannot comma separate imports but can use that for variables within a module
import os
import sys
import random
# another example has been commented out below
# from JamesModule import a,b,foobar

# Firstly, we will build a city battle program to emulate some cool wars

##new comment to test ssh key

population = 520
player_atk_l = 35
player_atk_h = 50
player_speed = 8

enemy_pop_l = 420
enemy_pop_h = 460
enemy_atk_l = 40
enemy_atk_h = 60
enemy_speed = 10
enemy_population = random.randrange(enemy_pop_l, enemy_pop_h)

while population >=0:
    player_dmg = random.randrange(enemy_atk_l, enemy_atk_h)
    enemy_dmg = random.randrange(player_atk_l, player_atk_h)

    population = population-player_dmg
    enemy_population = enemy_population-enemy_dmg

    if population <=30:
        population = 30

    if enemy_population <= 30:
        enemy_population = 30

    print('Enemy attacks for ', player_dmg, '. Your population is ', population)
    print('You attacks for ', enemy_dmg, '. The enemy\'s population is ', enemy_population)

    if population == 30:
        print('Your numbers are low, you retreat to fight another day')
        break
    # An alternative way to end this program is using a continue rather than break. Example below.
    # if population > 30:
    #     continue
    # print('Your numbers are low, you retreat to fight another day')
    # break

    if enemy_population == 30:
        print('Their numbers are low so they retreat. Victory is yours')
        break


'''
This method of defining a class is quite fixed. Each time an object is created it will have the same attack
These variables are known as class variables
'''

class village:
    tech = 'bronze'  # these are known as class variables
    atk_l = 40
    atk_h = 60

    def gettech(self):
        print (self.tech)


guildford = village()

tech = 'iron'
guildford.gettech()

'''
It is better to create a class with input variables to improve the flexibility. This requires a __init__ function
These variables are known as instance variables
'''

class village2():

    def __init__(self, tech2, atk_l2, atk_h2):
        self.tech2 = tech2  # these are instance variables
        self.atk_l2 = atk_l2
        self.atk_h2 = atk_h2

    def gettech2(self):
        print(self.tech2)


bolton = village2('bone',12,18)

bolton.gettech2()