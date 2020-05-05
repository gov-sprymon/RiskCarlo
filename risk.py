import countries
import random
import copy
random.seed(a = None)
def get_player_action():
    got_good_input = False
    while not got_good_input:
        action =  input("Enter country to attack from and to attack(ie Afghanistan Middle_East): ")
        actions = action.split()
        if(actions[0] == "show"):
            show_country(actions[1])
            continue
        if(len(actions) != 2):
            print("Need exactly 2 territories for a battle")
            continue
        if(actions[0] not in countries.countries_dict or actions[1] not in countries.countries_dict):
            print("Try naming a territory that exists")
            continue
        if(actions[0] not in player1_countries):
            print("Cant attack from countries you dont own")
            continue
        if(actions[1] in player1_countries):
            print("Cant attack yourself")
            continue
        if(countries.countries_dict[actions[0]][1] == 1):
            print("Need atleast 2 units to attack")
            continue
        if(actions[1] not in countries.countries_dict[actions[0]][0]):
            print("Must attack adjacent countries")
            continue
        return action
def get_player_place(bonus):
    got_good_input = False
    while  bonus > 0:
        print("Troop Bonus of %d" %(bonus))
        action = input("Enter country to add bonus to and amount:")
        actions = action.split()
        if(actions[0] == "show"):
            show_country(actions[1])
            continue
        if(countries.countries_dict[actions[0]][2] == 0):
            if(int(actions[1]) > bonus ):
                countries.countries_dict[actions[0]][1] += bonus
                bonus = 0
            else:
                countries.countries_dict[actions[0]][1] += int(actions[1])
                bonus -= int(actions[1])
            continue


def show_country(territory):
    print("\n")
    print(territory)
    if(countries.countries_dict[territory][2] == 0):
        print("Owner: YOU")
    else:
        print("Owner: AI")
    print("Troop Count: %d" %(countries.countries_dict[territory][1]))
    print("Adjacent Territories:")
    for adj in countries.countries_dict[territory][0]:
        if(countries.countries_dict[adj][2] == 1 ):
            print("--%s(AI)" %(adj))
        else:
            print("--%s(YOU)" %(adj))
#initialize countries
def make_action(action):
    attacker = action.split()[0]
    defender = action.split()[1]

    attacker_units = countries.countries_dict[attacker][1]
    defender_units = countries.countries_dict[defender][1]

    battle_result =  battle(attacker_units,defender_units)


    if (battle_result[1] == 0):
        #move all but 1 units to won territory and swap owner
        countries.countries_dict[defender][1] = battle_result[0] - 1
        if(countries.countries_dict[defender][2] == 0):
            countries.countries_dict[defender][2] = 1
        else:
            countries.countries_dict[defender][2] = 0
        countries.countries_dict[attacker][1] = 1
    else:
        countries.countries_dict[attacker][1] = battle_result[0]
        countries.countries_dict[defender][1] = battle_result[1]
    return battle_result
def get_continent_bonus(territories):
    bonus = 0
    if(all(x in territories for x in countries.SouthAmerica)):
        bonus += 2
    if(all(x in territories for x in countries.NorthAmerica)):
        bonus += 5
    if(all(x in territories for x in countries.Africa)):
        bonus += 3
    if(all(x in territories for x in countries.Australia)):
        bonus += 2
    if(all(x in territories for x in countries.Asia)):
        bonus += 7
    if(all(x in territories for x in countries.Europe)):
        bonus += 5
    return bonus

def battle(attacker_units,defender_units):
    battle_over = False

    while attacker_units > 1  and defender_units > 0:
        attacker_dice_count = 0
        defender_dice_count = 0
        attacker_die = []
        defender_die = []

        if(attacker_units > 3):
            attacker_dice_count = 3
            attacker_die.append(random.randint(1,6))
            attacker_die.append(random.randint(1,6))
            attacker_die.append(random.randint(1,6))
        elif(attacker_units == 3):
            attacker_dice_count = 2
            attacker_die.append(random.randint(1,6))
            attacker_die.append(random.randint(1,6))
        elif(attacker_units == 2):
            attacker_dice_count = 1
            attacker_die.append(random.randint(1,6))

        if(defender_units > 1):
            defender_dice_count = 2
            defender_die.append(random.randint(1,6))
            defender_die.append(random.randint(1,6))
        elif(defender_units == 1):
            defender_dice_count = 1
            defender_die.append(random.randint(1,6))
        attacker_die.sort(reverse=True)
        defender_die.sort(reverse=True)
        #print(attacker_die)
        #print(defender_die)

        for i in range(0,min(len(defender_die),len(attacker_die))):
            if(attacker_units == 0 | defender_units == 0):
                break
            if(defender_die[i] >= attacker_die[i]):
                attacker_units -= 1
            else:
                defender_units -= 1

    return [attacker_units,defender_units]



def get_owners():
    player1_countries = []
    player2_countries = []
    #turn 0 = player1 = human

    #NORTH AMERICA
    #print("Your territories:")
    for country in countries.countries_dict:
        if countries.countries_dict[country][2] == 0:
            #print("--%s" %(country))
            player1_countries.append(country)

    #print("\n\n")
    #print("AI territories:")
    for country in countries.countries_dict:
        if countries.countries_dict[country][2] == 1:
            #print("--%s" %(country))
            player2_countries.append(country)
    #print("\n\n")
    return [player1_countries,player2_countries]


def print_owners():
    player1_countries = []
    player2_countries = []
    #turn 0 = player1 = human

    #NORTH AMERICA

    for country in countries.countries_dict:
        if countries.countries_dict[country][2] == 0:
            player1_countries.append(country)

    for country in countries.countries_dict:
        if countries.countries_dict[country][2] == 1:
            player2_countries.append(country)

    player1_countries.sort()
    player2_countries.sort()
    print("Your territories: %d" %(len(player1_countries)))
    for country in player1_countries:
        if countries.countries_dict[country][2] == 0:
            print("--%s(%d)" %(country,countries.countries_dict[country][1]))
    print("\n\n")
    print("AI territories: %d" %(len(player2_countries)))
    for country in player2_countries:
        if countries.countries_dict[country][2] == 1:
            print("--%s(%d)" %(country,countries.countries_dict[country][1]))
    print("\n\n")
    #return [player1_countries,player2_countries]

def get_AI_action(country_dict):
    print(country_dict["Iceland"])
turn = 0
game_over = False
while not game_over:
    print_owners()
    player1_countries = get_owners()[0]
    player2_countries = get_owners()[1]
    #
    #HUMANS TURN
    #
    if(turn == 0):
        get_player_place(   (len(player1_countries)/3)  + get_continent_bonus(player1_countries))
        action = get_player_action()
        initial_self_troop_strength = countries.countries_dict[action.split()[0]][1]
        initial_enemy_strength = countries.countries_dict[action.split()[1]][1]
        battle_result = make_action(action)

        #print(battle_result)
        if(battle_result[1] == 0):
            print("You took %s and lost %d units\n" %(action.split()[1], initial_self_troop_strength-1- countries.countries_dict[action.split()[1]][1]) )
        else:
            print("You lost %d units, AI lost %d units\n" %(initial_self_troop_strength - battle_result[0],initial_enemy_strength - battle_result[1]))
        turn = 1
    #
    #AI TURN
    #
    if(turn == 1):
        b = copy.deepcopy(countries.countries_dict)
        get_AI_action(b)
        player1_countries = get_owners()[0]
        player2_countries = get_owners()[1]
        place = random.randint(0,len(player2_countries)-1)
        countries.countries_dict[player2_countries[place]][1] += (len(player2_countries) / 3) + get_continent_bonus(player2_countries)
        print("AI placed %d units on %s" %(len(player2_countries) / 3,player2_countries[place]))
        enemy_count = len(player1_countries)

        found = False
        while not found:
            attack_from = random.randint(0,len(player2_countries)-1)
            for opponent_country in player1_countries:
                if(player2_countries[attack_from] in countries.countries_dict[opponent_country][0]):
                    action = player2_countries[attack_from]  +" "+ opponent_country
                    battle_result = make_action(action)
                    print("AI attacked %s from %s" %(opponent_country,player2_countries[attack_from]))
                    if(battle_result[1] == 0):
                        print("AI took %s \n" %(opponent_country))
                    else:
                        print("AI lost to %s \n" %(opponent_country))
                    found = True
                    turn = 0
                    break
    player1_countries = get_owners()[0]
    if(len(player1_countries) == 42 or len(player1_countries) == 0):
        game_over = True
