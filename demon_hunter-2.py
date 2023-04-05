import pickle
import re

class Status:
    def __init__(self, name:str, duration:int): 
        self.name = name
        self.duration = duration

class Talent: 
    def __init__(self, name, damage=0, fury=0, dur=0, desc=None, reqs:str=None, cd=0, ranks=1): 
        self.name = name
        self.damage = damage
        self.fury = fury
        self.duration = dur
        self.desc = desc
        self.reqs = reqs
        self.rm_cd = 0
        self.max_cd = cd
        self.points = 0
        self.ranks = ranks
    
    def toggle(self): 
        if self.points == self.ranks: self.points = 0
        else: self.points += 1

class Player: 
    def __init__(self, hp = 200, fury = 100): 
        self.hp = hp
        self.max_hp = hp
        self.fury = 0
        self.max_fury = fury
        self.abilities = []
        self.statuses = []
    
    def find_ability(self, name:str) -> Talent: 
        for ability in self.abilities: 
            if isinstance(ability.name, list): 
                if name == ability.name[0]: return ability
                elif name == ability.name[1]: return ability
            else: 
                if name == ability.name: return ability
        return None
    
    def find_status(self, name:str) -> Talent: 
        for status in self.statuses: 
            if name == status.name: return status
        return False

    def add_status(self, name:str, duration:int): 
        self.statuses.append(Status(name, duration))

    def remove_status(self, name:str): 
        for ind in range(len(self.statuses)): 
            if name == self.statuses[ind].name: 
                self.statuses.pop(ind)
                return
    
def find_talent(name:str, list_talents:list) -> int: 
    if len(list_talents) == 0: return None
    for ind,talent in enumerate(list_talents): 
        if talent.name.lower() == name.lower(): return ind

def roll(dice:str, mult:int) -> int: 
    import random
    num_dice, dice_size = dice.split('d')
    result = 0
    for _ in range(int(num_dice)): 
        result += random.randint(1, int(dice_size))
    result = result * mult / 100
    return round(result)

base_abilities = []
base_abilities.append(Talent(name='Demon\'s Bite',damage=['122%'],fury=0,dur=0,desc='Quickly attack for 122% Physical damage. Generates 25 Fury.',reqs='1 action',cd=0,ranks=1))
base_abilities.append(Talent(name=['Chaos Strike', 'Annihilation'],damage=['210%', '272%'],fury=0,dur=0,desc=['Slice your target for 210% Chaos damage.','Slice your target for 272% Chaos damage.'],reqs='1 action',cd=0,ranks=1))
base_abilities.append(Talent(name=['Blade Dance','Death Sweep'],damage=['168%','290%'],fury=0,dur=0,desc=['Strike up to 5 nearby enemies for 168% Physical damage.','Strike up to 5 nearby enemies for 290% Physical damage.'],reqs='1 action, 1 round cooldown',cd=1,ranks=1))
base_abilities.append(Talent(name='Immolation Aura',damage=['120%'],fury=0,dur=1,desc='Deal 120% Fire damage to all nearby enemies on the next round. Generates 20 Fury.',reqs='Free action, 2 round cooldown',cd=2,ranks=1))
base_abilities.append(Talent(name='Throw Glaive',damage=['80%'],fury=0,dur=0,desc='Throw a demonic glaive at the target, dealing 80% Physical damage. The glaive can ricochet to an additional enemy within 10 yards.',reqs='Free action, 30 yard range',cd=0,ranks=1))
base_abilities.append(Talent(name='Metamorphosis',damage=['76%', '10%'],fury=0,dur=0,desc='Leap into the air and land with explosive force, dealing 76% magic damage to enemies within 10 yards. Upon landing, you\'re transformed into a hellish demon for 2 rounds, upgrading Chaos Strike into Annihilation, and Blade Dance into Death Sweep. Lifesteal for 10% of damage dealt.',reqs='Free action, 1 / combat',cd=-1,ranks=1))
base_abilities.append(Talent(name='Blur',damage=['25%'],fury=0,dur=0,desc='Reduce all damage taken by 25% for 1 round.',reqs='Free action, 4 round cooldown',cd=4,ranks=1))
base_abilities.append(Talent(name='Fel Rush',damage=['50%'],fury=0,dur=0,desc='Rush forward, incinerating anything in your path for 50% Chaos damage.',reqs='Free action, 1 round cooldown',cd=1,ranks=1))
base_abilities.append(Talent(name='Disrupt',damage=None,fury=0,dur=0,desc='Interrupt an enemy\'s spellcast.',reqs='Free action',cd=0,ranks=1))
base_abilities.append(Talent(name='Spectral Sight',damage=None,fury=0,dur=0,desc='Allows you to see enemies and treasures through physical barriers, as well as enemies that are stealthed and invisible. Cannot be cast in combat.',reqs='Free action',cd=0,ranks=1))
base_abilities.append(Talent(name='Glide',damage=None,fury=0,dur=0,desc='You\'re immune to fall damage.',reqs=None,cd=0,ranks=1))
base_abilities.append(Talent(name='Double Jump',damage=None,fury=0,dur=0,desc='You are able to jump again while near the apex of your first jump.',reqs=None,cd=0,ranks=1))
base_abilities.append(Talent(name='Shattered Souls',damage=['5%', '20%'],fury=0,dur=0,desc='Killing an enemy has a 5% chance to heal you for 20% of your maximum health.',reqs=None,cd=0,ranks=1))
base_abilities.append(Talent(name='Vengeful Retreat',damage=['28%'],fury=0,dur=0,desc='Remove all snares and vault away, dealing 28% physical damage to all nearby enemies. Learned automatically if in Havoc spec.',reqs='Free action, 2 round cooldown',cd=2,ranks=1))

dh_talents = []
dh_talents.append(Talent(name='Blazing Path',damage=None,fury=0,dur=0,desc='Fel Rush has no cooldown.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Sigil of Flame',damage=['32%', '90%'],fury=0,dur=1,desc='Place a Sigil of Flame at the target location, dealing 32% Fire damage immediately to all nearby enemies, and another 90% damage on the next round. Generates 30 Fury.  Learned automatically if in Vengeance spec.',reqs='Free action, 30 yard range, 2 round cooldown',cd=2,ranks=1))
dh_talents.append(Talent(name='Unrestrained Fury',damage=None,fury=0,dur=0,desc='Increase maximum Fury by 10 / 20.',reqs=None,cd=0,ranks=2))
dh_talents.append(Talent(name='Imprison',damage=None,fury=0,dur=0,desc='Imprison a demon, beast, or humanoid, incapacitating them for 4 rounds. Damage cancels the effect. Limit 1.',reqs='Free action / reaction, 20 yard range, 3 round cooldown',cd=3,ranks=1))
dh_talents.append(Talent(name='Shattered Restoration',damage=['5%', '10%'],fury=0,dur=0,desc='The healing of Shattered Souls is increased by 5% / 10%.',reqs=None,cd=0,ranks=2))
dh_talents.append(Talent(name='Vengeful Bonds',damage=['70%'],fury=0,dur=0,desc='Vengeful Retreat reduces the movement speed of all nearby enemies by 70% for 1 round.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Improved Disrupt',damage=None,fury=0,dur=0,desc='Increases the range of Disrupt to 10 yards.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Bouncing Glaives',damage=None,fury=0,dur=0,desc='Throw Glaive ricochets to 1 additional target.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Consume Magic',damage=None,fury=0,dur=0,desc='Consume 1 beneficial Magic effect, removing it from the target.',reqs='Free action, 1 round cooldown',cd=1,ranks=1))
dh_talents.append(Talent(name='Flames of Fury',damage=None,fury=0,dur=0,desc='Sigil of Flame generates 2 additional Fury per target hit.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Pursuit',damage=None,fury=0,dur=0,desc='Movement speed increased to 40 yards / round.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Disrupting Fury',damage=None,fury=0,dur=0,desc='Disrupt generates 30 Fury on a successful interrupt.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Aura of Pain',damage=['15%'],fury=0,dur=0,desc='Increases the critical strike chance of Immolation Aura to 15%.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Felblade',damage=['144%'],fury=0,dur=0,desc='Charge to your target, dealing 144% magic damage. Generates 40 Fury.',reqs='1 action, flourish',cd=0,ranks=1))
dh_talents.append(Talent(name='Swallowed Anger',damage=None,fury=0,dur=0,desc='Consume Magic generates 20 Fury when a beneficial Magic effect is successfully removed from the target.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Charged Warblades',damage=['5%'],fury=0,dur=0,desc='You heal for 5% of all magic damage you deal.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Eye Beam',damage=['280%'],fury=0,dur=0,desc='Blast all enemies in front of you, dealing 280% magic damage. Deals reduced damage beyond 5 targets.',reqs='1 action, 20 yard range, 3 round cooldown',cd=3,ranks=1))
dh_talents.append(Talent(name='Improved Chaos Strike',damage=['10%'],fury=0,dur=0,desc='Chaos Strike damage increased by 10%.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Insatiable Hunger',damage=['50%'],fury=0,dur=0,desc='Demon\'s Bite deals 50% more damage and generates 5 to 10 additional Fury.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Demon Blades',damage=None,fury=0,dur=0,desc='You can now cast Demon Bite twice per action.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Felfire Heart',damage=None,fury=0,dur=0,desc='Increase the duration of Immolation Aura and Sigil of Flame by 1 round.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Demonic Appetite',damage=['25%'],fury=0,dur=0,desc='Chaos Strike has a 25% chance to refund 30 additional Fury.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Improved Fel Rush',damage=['20%'],fury=0,dur=0,desc='Fel Rush damage increased by 20%.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='First Blood',damage=['294%'],fury=0,dur=0,desc='Blade Dance deals 294% magic damage to the first target struck.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Furious Throws',damage=None,fury=0,dur=0,desc='Throw Glaive now costs 25 Fury and throws a second glaive at the target.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Burning Hatred',damage=None,fury=0,dur=0,desc='Immolation Aura generates an additional 30 Fury.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Critical Chaos',damage=['10%'],fury=0,dur=0,desc='The chance that Chaos Strike will refund 20 Fury is increased by 5 / 10%.',reqs=None,cd=0,ranks=2))
dh_talents.append(Talent(name='Mortal Dance',damage=['50%'],fury=0,dur=0,desc='Blade Dance now reduces targets\' healing received by 50% for 1 round.',reqs=None,cd=0,ranks=1))
dh_talents.append(Talent(name='Dancing with Fate',damage=['20%'],fury=0,dur=0,desc='The final slash of Blade Dance deals an additional 20% damage.',reqs=None,cd=0,ranks=2))

active_talents = [i for i in """
Vengeful Retreat
Unrestrained Fury
Unrestrained Fury
Vengeful Bonds
Improved Disrupt
Pursuit
Disrupting Fury
Felblade
Blazing Path
Eye Beam
Improved Chaos Strike
Demon Blades
Felfire Heart
Demonic Appetite
First Blood
Critical Chaos
Dancing with Fate
""".split('\n') if i]

Unicorn = Player()

for talent in active_talents: 
    result_dh = find_talent(talent, dh_talents)
    if result_dh is not None: dh_talents[result_dh].toggle()

Unicorn.abilities.extend(base_abilities)
for talent in dh_talents: 
    if talent.points != 0: 
        Unicorn.abilities.append(talent)

if Unicorn.find_ability('Blazing Path'): 
    fel_rush = Unicorn.find_ability('Fel Rush')
    fel_rush.max_cd = 0
    fel_rush.reqs = 'Free action'

if Unicorn.find_ability('Unrestrained_Fury') is not None: 
    Unicorn.max_fury = 100 + Unicorn.find_ability('Unrestrained_Fury').points * 10
    
if Unicorn.find_ability('Shattered Restoration'): 
    shattered_souls = Unicorn.find_ability('Shattered Souls')
    damage = f"{(20 + 5 * Unicorn.find_ability('Shattered Restoration').points)}%"
    shattered_souls.damage[1] = damage
    shattered_souls.desc = re.sub(r"\b\d{1,3})\%", damage, shattered_souls.desc)

if Unicorn.find_ability('Improved Disrupt'): 
    disrupt = Unicorn.find_ability('Disrupt')
    disrupt.reqs += ", 10 yard range"

if Unicorn.find_ability('Disrupting Fury'): 
    disrupt = Unicorn.find_ability('Disrupt')
    disrupt.desc += ' Generates 30 Fury.'
    disrupt.fury = 30

if Unicorn.find_ability('Improved Chaos Strike'): 
    chaos_strike = Unicorn.find_ability('Chaos Strike')
    damage = [f"{round(int(dmg[:-1]) * 1.1)}%" for dmg in chaos_strike.damage]
    chaos_strike.damage = damage
    chaos_strike.desc = [re.sub(r"\b\d{1,3}\%", damage[i], chaos_strike.desc[i]) for i in range(len(damage))]

if Unicorn.find_ability('Felfire Heart'): 
    immolation_aura = Unicorn.find_ability('Immolation Aura')
    immolation_aura.duration = 2
    immolation_aura.desc = 'Deal 120% Fire damage to all nearby enemies on the next two rounds.'

if Unicorn.find_ability('Improved Fel Rush'): 
    fel_rush = Unicorn.find_ability('Fel Rush')
    damage = f"{round(int(fel_rush.damage[:-1]) * 1.2)}%"
    fel_rush.damage = damage
    fel_rush.desc = re.sub(r"\b\d{1,3})\%", damage, fel_rush.desc)

def cast_ability(): 
    ind = 0
    for ability in Unicorn.abilities: 
        if ability.reqs is None: continue
        if ind == 1 or ind == 2: 
            if Unicorn.find_status('Metamorphosis'): print(f'[{ind+1}] {ability.name[1]} ({ability.reqs})', end = '')
            else: print(f'[{ind+1}] {ability.name[0]} ({ability.reqs})', end = '')
        else: print(f'[{ind+1}] {ability.name} ({ability.reqs})', end = '')
        if ability.rm_cd != 0: print(' [ability.rm_cd]')
        else: print('')
        ind += 1
    print('')

def output_all():
    for ind,ability in enumerate(Unicorn.abilities): 
        print(f'[{ind+1}] {ability.name}', end = '')
        if ability.ranks > 1: print(f' ({ability.points} / {ability.ranks})')
        else: print('')
    print('')

def add_status(): 
    print('List of statuses: ')
    print('1) Metamorphosis')
    sel = int(input('Selection: '))
    print('')
    if sel == 1: 
        if Unicorn.find_status('Metamorphosis'): Unicorn.remove_status('Metamorphosis')
        else: Unicorn.add_status('Metamorphosis', 2)

def save_player():
    with open('Unicorn.pkl', 'wb') as output:
        pickle.dump(Unicorn, output, pickle.HIGHEST_PROTOCOL)

def load_player():
    with open('Unicorn.pkl', 'rb') as input:
        return pickle.load(input)


while True: 
    print('---- Demon Hunter Simulation ----')
    print('Select an option: ')
    print('1) Cast ability')
    print('2) Show all active abilities and talents')
    print('3) Get a detailed description of a given ability')
    print('4) Add statuses')
    print('9) Exit')
    sel = int(input("Selection: "))
    print('')

    if sel == 1: cast_ability()
    elif sel == 2: output_all()
    elif sel == 4: add_status()
    elif sel == 9: break


    