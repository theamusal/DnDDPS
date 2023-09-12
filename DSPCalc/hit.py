import numpy as np
import random

def turn(rolls, enemyac, gwm):
    
    _damage = 0
    tohit = 10
    todamage = 6
    turncrit = False
    manouvers = 5
    
    # Reaction
    adv = True
    att1 = rolls[0] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[1] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[0] == 20 or (adv and rolls[1] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
          
    # First hit
    adv = False
    att1 = rolls[2] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[3] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[2] == 20 or (adv and rolls[3] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
    
    # Second hit    
    adv = False
    att1 = rolls[4] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[5] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[4] == 20 or (adv and rolls[5] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
    
    
    # AS First Hit
    adv = False
    att1 = rolls[6] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[7] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[6] == 20 or (adv and rolls[7] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
    
    
    # AS Second hit
    adv = False
    att1 = rolls[8] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[9] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[8] == 20 or (adv and rolls[9] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
        
    # Bonus Action
    hd = 4 + (turncrit * 6)
    adv = False
    att1 = rolls[10] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[11] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[10] == 20 or (adv and rolls[11] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,hd)            # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,hd))# extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
            
    return _damage

def advturn(rolls, enemyac, enemystrsave):
    
    _damage = 0
    tohit = 10
    todamage = 6
    turncrit = False
    gwm = False
    prone = False
    manouvers = 5
    dc = 15
    
    # Reaction
    adv = True
    gwm = adv
    att1 = rolls[0] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[1] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[0] == 20 or (adv and rolls[1] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
        # attempt manouver
        if manouvers > 0:
            _damage += random.randint(1,8)
            prone = prone or (random.randint(1,20) + enemystrsave) < dc
            manouvers -= 1
          
    # First hit
    adv = prone
    gwm = adv
    att1 = rolls[2] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[3] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[2] == 20 or (adv and rolls[3] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
        # attempt manouver
        if manouvers > 0:
            _damage += random.randint(1,8)
            prone = prone or (random.randint(1,20) + enemystrsave) < dc
            manouvers -= 1
          
    # Second hit  
    adv = prone
    gwm = adv
    att1 = rolls[4] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[5] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[4] == 20 or (adv and rolls[5] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
        # attempt manouver
        if manouvers > 0:
            _damage += random.randint(1,8)
            prone = prone or (random.randint(1,20) + enemystrsave) < dc
            manouvers -= 1
          
    
    # AS First Hit
    adv = prone
    gwm = adv
    att1 = rolls[6] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[7] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[6] == 20 or (adv and rolls[7] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
        # attempt manouver
        if manouvers > 0:
            _damage += random.randint(1,8)
            prone = prone or (random.randint(1,20) + enemystrsave) < dc
            manouvers -= 1
          
    
    # AS Second hit
    adv = prone
    gwm = adv
    att1 = rolls[8] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[9] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[8] == 20 or (adv and rolls[9] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,10)                 # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,10))     # extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
        # attempt manouver
        if manouvers > 0:
            _damage += random.randint(1,8)
            prone = prone or (random.randint(1,20) + enemystrsave) < dc
            manouvers -= 1
          
    # Bonus Action
    hd = 4 + (turncrit * 6)
    adv = prone
    gwm = adv
    att1 = rolls[10] + tohit + (gwm * -5) >= enemyac
    att2 = rolls[11] + tohit + (gwm * -5) >= enemyac
    attcrit = rolls[10] == 20 or (adv and rolls[11] == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        _damage += random.randint(1,hd)            # initial dice roll
        _damage += todamage                             # damage bonus
        _damage += (attcrit * random.randint(1,hd))# extra hit dice if crit
        _damage += (gwm * 10)                           # add 10 if great weapon master
        # attempt manouver
        if manouvers > 0:
            _damage += random.randint(1,8)
            prone = prone or (random.randint(1,20) + enemystrsave) < dc
            manouvers -= 1
          
    return _damage
def gapturn(rolls, enemyac, enemystrsave, tohit, todamage, dc):
    
    _damage = 0
    hd = 10
    turncrit = False
    prone = False
    manouvers = 5
    
    # Reaction
    dmg, prone, turncrit, manouvers = hit(rolls[0], rolls[1], hd, tohit, todamage, dc, enemyac, enemystrsave, True, True, prone, turncrit, manouvers)
    _damage += dmg
          
    # First hit
    dmg, prone, turncrit, manouvers = hit(rolls[2], rolls[3], hd, tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg
          
    # Second hit  
    dmg, prone, turncrit, manouvers = hit(rolls[4], rolls[5], hd, tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg          
    
    # AS First Hit
    dmg, prone, turncrit, manouvers = hit(rolls[6], rolls[7], hd, tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg
    
    # AS Second hit
    dmg, prone, turncrit, manouvers = hit(rolls[8], rolls[9], hd, tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg
          
    # Bonus Action
    dmg, prone, turncrit, manouvers = hit(rolls[10], rolls[11], 4 + (turncrit * 6), tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg
          
    return _damage

def hasteturn(rolls, enemyac, enemystrsave, tohit, todamage, dc):
    
    _damage = 0
    hd = 10
    turncrit = False
    prone = False
    manouvers = 5
    
    # Reaction
    dmg, prone, turncrit, manouvers = hit(rolls[0], rolls[1], hd, tohit, todamage, dc, enemyac, enemystrsave, True, True, prone, turncrit, manouvers)
    _damage += dmg
          
    # First hit
    dmg, prone, turncrit, manouvers = hit(rolls[2], rolls[3], hd, tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg
          
    # Second hit  
    dmg, prone, turncrit, manouvers = hit(rolls[4], rolls[5], hd, tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg          
    
    # AS First Hit
    dmg, prone, turncrit, manouvers = hit(rolls[6], rolls[7], hd, tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg
    
    # AS Second hit
    dmg, prone, turncrit, manouvers = hit(rolls[8], rolls[9], hd, tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg
    
    # Haste hit
    dmg, prone, turncrit, manouvers = hit(rolls[12], rolls[13], hd, tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg
          
    # Bonus Action
    dmg, prone, turncrit, manouvers = hit(rolls[10], rolls[11], 4 + (turncrit * 6), tohit, todamage, dc, enemyac, enemystrsave, prone, prone, prone, turncrit, manouvers)
    _damage += dmg
          
    return _damage

def hit(roll1, roll2, hd, tohit, todamage, dc, enemyac, enemystrsave, adv, gwm, prone, turncrit, manouvers):
    damage = 0
    att1 = roll1 + tohit + (gwm * -5) >= enemyac
    att2 = roll2 + tohit + (gwm * -5) >= enemyac
    attcrit = roll1 == 20 or (adv and roll2 == 20)
    turncrit = turncrit or attcrit
    if att1 or (adv and att2):
        damage += random.randint(1,hd)              # initial dice roll
        damage += damage + (damage * attcrit)       # double if crit
        damage += todamage                          # damage bonus
        damage += (gwm * 10)                        # add 10 if great weapon master
        # attempt manouver
        if manouvers > 0:
            damage += random.randint(1,8)
            prone = prone or (random.randint(1,20) + enemystrsave) < dc
            manouvers -= 1
          
    return damage, prone, turncrit, manouvers