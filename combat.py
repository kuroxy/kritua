import math
import random
# turn based!

# Actions

# light (always damage )
# heavy

# block

# push


# player || light | heavy | block | push | Detect
# enemy
# light  ||  11   | 12   | 10     | 44   | 15
# heavy  ||  21   | 22   | 03     | 20   | 25
# block  ||  01   | 30   | 00     | 44   | 05
# push   ||  44  | 02    | 44     | 44   | 44


# Heal doesnt take a turn but can only use 1 per turn

# Detect type - see's what the most used action is a and will show the next 2 moves | (only if already scaned, does take an action can only be used once)
# Scan - scan the enemy learn new type

# heavy does twice as much as light
# if stunned .5x damage amount for 2 turns

# first char is player second enemy
#0 does no damage
#1 does lightdamage
#2 does heavy damage
#3 does block == stun
#4 does pushed (fight will end)
#5 does detect

# first player then enemy
STUNTIME = 2
actionchart = {"light" : {"light": "11", "heavy" : "12", "block" : "10", "push": "04"},
               "heavy" : {"light": "21", "heavy" : "22", "block" : "03", "push": "20"},
               "block" : {"light": "01", "heavy" : "30", "block" : "00", "push": "04"},
               "push" : {"light": "40", "heavy" : "02", "block" : "40", "push": "44"},
               "detect" : {"light": "51", "heavy" : "52", "block" : "50", "push": "04"}}

def getdamage(obj, type):   # 1 == light 2 = heavy attack
    dm = obj.attack * type
    if obj.isStunned:
        dm*=.5
    return math.floor(dm)


def executeaction(executer,receiver,type):
    if type == "0":
        print("Nothing happend to the {}".format(receiver.type))

    elif type == "1":
        damage = getdamage(executer,1)
        print("The {0} did {1} damage points to the {2}".format(executer.type, damage, receiver.type))
        receiver.health -= damage

    elif type == "2":
        damage = getdamage(executer,2)
        print("The {0} did {1} damage points to the {2}".format(executer.type, damage, receiver.type))
        receiver.health -= damage

    elif type == "3":
        print("The {0} got stunned".format(receiver.type))
        receiver.isStunned = STUNTIME

    elif type == "4":
        print("The {0} escaped".format(executer.type))
        executer.enemy = None
        receiver.enemy = None

    elif type == "5":
        print("The {0} has scanned the {1}".format(executer.type, receiver.type))
        print("Bzzzbbzbzzz here are the stats")


def action(playerobj, enemyobj):
    playerobj.stunnedtime = max(0, playerobj.stunnedtime-1)
    enemyobj.stunnedtime = max(0, enemyobj.stunnedtime-1)

    outcome = actionchart[playerobj.action][enemyobj.action]
    paction = outcome[0]
    eaction = outcome[1]
    executeaction(playerobj, enemyobj, paction)
    executeaction(enemyobj, playerobj, eaction)

    print("The {0} has {1} health left".format(playerobj.type, playerobj.health))
    print("The {0} has {1} health left".format(enemyobj.type, enemyobj.health))


def getplayeraction():
    paction = None
    while True:


class player(object):
    type = "player"
    def __init__(self, hp, att):
        # stats
        self.maxhealth = hp
        self.health = hp
        self.xp = 0
        self.attack = att

        # modifiers
        self.stunnedtime = 0

        # fighting
        self.action = None
        self.enemy = None #


class enemy(object):
    type = "enemy"
    attacktypes = ["light","heavy","block"]
    def __init__(self, hp, att):
        # stats
        self.maxhealth = hp
        self.health = hp
        self.attack = att

        # modifiers
        self.stunnedtime = False

        #fighting
        self.action = None
        self.enemy = None

    def randomattack(self):
        self.action random.choice(attacktypes)


while True:
