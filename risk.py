import countries
import random
import copy
random.seed(a = None)

class Node:
    action = None
    board = None
    left = None
    right = None
    def __init__(self,board = None, action = None,left = None,right = None):
        self.board = board
        self.action = action #ex ["Great_Britain", "Iceland"]
        self.right = right   #board state from winning parent battle
        self.left = left     #board state from losing parent battle

def get_player_action():
    got_good_input = False
    while not got_good_input:
        action =  input("Enter country to attack from and to attack(ie Afghanistan Middle_East): ")
        print(action)
        if(action != ""):
            actions = action.split()
            if(actions[0] == "show"):
                if(actions[1] in countries.countries_dict):
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
        if(actions[1].isnumeric()):
            if(actions[0] == "show" or actions[0] == "Show"):
                if(actions[1] in countries.countries_dict):
                    show_country(actions[1])
                continue
            if(actions[0] in countries.countries_dict):
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
def make_action(action,country_dict = countries.countries_dict):
    attacker = action.split()[0]
    defender = action.split()[1]
    #print(attacker + "(%d) --> " + defender + "(%d)" %(country_dict[attacker][1],country_dict[defender][1]))
    #print("%s(%d) --> %s(%d)" %(attacker,country_dict[attacker][1],defender,country_dict[defender][1]))
    attacker_units = country_dict[attacker][1]
    defender_units = country_dict[defender][1]

    battle_result =  battle(attacker_units,defender_units)

    #print("IN make")
    if (battle_result[1] == 0):
        #move all but 1 units to won territory and swap owner
        country_dict[defender][1] = battle_result[0] - 1
        if(country_dict[defender][2] == 0):
            country_dict[defender][2] = 1
        else:
            country_dict[defender][2] = 0
        country_dict[attacker][1] = 1
    else:
        country_dict[attacker][1] = battle_result[0]
        country_dict[defender][1] = battle_result[1]
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
def battle(A,D):
    while A > 1 and D > 0:
        ADice = 0
        DDice = 0
        ARoll = []
        DRoll = []
        if(A > 3):
            ADice =  3
        else:
            ADice = A - 1

        if(D > 1):
            DDice = 2
        else:
            DDice = 1

        for i in range(0,ADice):
            ARoll.append(random.randint(1,6))
        for j in range(0,DDice):
            DRoll.append(random.randint(1,6))

        ARoll.sort(reverse=True)
        DRoll.sort(reverse=True)

        for i in range(0, min(ADice,DDice)):
            if(ARoll[i] > DRoll[i]):
                A -= 1
            else:
                D -= 1
    return [A,D]
def get_continent(country):
    if(country in countries.NorthAmerica):
        return "NorthAmerica"
    if(country in countries.Australia):
        return "Australia"
    if(country in countries.Africa):
        return "Africa"
    if(country in countries.Europe):
        return "Europe"
    if(country in countries.Asia):
        return "Asia"
    if(country in countries.SouthAmerica):
        return "SouthAmerica"
def get_owners(countries_dict = countries.countries_dict):
    player1_countries = []
    player2_countries = []

    for country in countries_dict:
        if countries_dict[country][2] == 0:
            player1_countries.append(country)
    for country in countries_dict:
        if countries_dict[country][2] == 1:
            player2_countries.append(country)

    return [player1_countries,player2_countries]
def print_owners():
    player1_countries = []
    player2_countries = []
    for country in countries.countries_dict:
        if countries.countries_dict[country][2] == 0:
            player1_countries.append(country)

    for country in countries.countries_dict:
        if countries.countries_dict[country][2] == 1:
            player2_countries.append(country)

    player1_countries.sort()
    player2_countries.sort()

    print("YOUR TERRITORIES: %d:\n" %(len(player1_countries)))


    for country in player1_countries :
        continent = get_continent(country)
        if(continent == "NorthAmerica"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player1_countries:
        continent = get_continent(country)
        if(continent == "SouthAmerica"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player1_countries:
        continent = get_continent(country)
        if(continent == "Europe"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player1_countries:
        continent = get_continent(country)
        if(continent == "Africa"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player1_countries:
        continent = get_continent(country)
        if(continent == "Asia"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player1_countries:
        continent = get_continent(country)
        if(continent == "Australia"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    print("\n\n")
    print("AI TERRITORIES: %d:\n" %(len(player2_countries)))
    for country in player2_countries :
        continent = get_continent(country)
        if(continent == "NorthAmerica"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player2_countries:
        continent = get_continent(country)
        if(continent == "SouthAmerica"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player2_countries:
        continent = get_continent(country)
        if(continent == "Europe"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player2_countries:
        continent = get_continent(country)
        if(continent == "Africa"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player2_countries:
        continent = get_continent(country)
        if(continent == "Asia"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))
    print("\n")
    for country in player2_countries:
        continent = get_continent(country)
        if(continent == "Australia"):
            print("--%s(%d)(%s)" %(country,countries.countries_dict[country][1],continent))

    print("\n\n")
def get_possible_targets(player,country_dict = countries.countries_dict):
    possible_targets = []
    if( player == 0):
        owners = get_owners(country_dict)
        #for every enemy territory
        for i in range(0, len(owners[1])):
            #for every AI(us) territory
            for j in range(0, len(owners[0])):
                #if AI country in enemy adjaceny list
                if(owners[0][j] in country_dict[owners[1][i]][0]):
                    #add our country and theres to possible targets
                    #if(country_dict[owners[0][j]][1] > 1 ):
                        #MAKE SURE IT CAN ACTUALLY ATTACK....except not really since it could place there...
                    possible_targets.append([owners[0][j], owners[1][i]])
        #print( str(len(possible_targets)) + " possible attacks" )
    else:
        owners = get_owners(country_dict)
        #for every enemy territory
        for i in range(0, len(owners[0])):
            #for every AI(us) territory
            for j in range(0, len(owners[1])):
                #if AI country in enemy adjaceny list
                if(owners[1][j] in country_dict[owners[0][i]][0]):
                    #add our country and theres to possible targets
                    #if(country_dict[owners[1][j]][1] > 1 ):
                        #MAKE SURE IT CAN ACTUALLY ATTACK
                    possible_targets.append([owners[1][j], owners[0][i]])
        #print( str(len(possible_targets)) + " possible attacks" )
    return possible_targets
def place_random(turn,country_dict = countries.countries_dict):
    if(turn == 0):
        player1_countries = get_owners(country_dict)[0]
        place = random.randint(0,len(player1_countries)-1)
        country_dict[player1_countries[place]][1] += (len(player1_countries) // 4) + get_continent_bonus(player1_countries)
    else:
        player2_countries = get_owners(country_dict)[1]
        place = random.randint(0,len(player2_countries)-1)
        country_dict[player2_countries[place]][1] += (len(player2_countries) // 4) + get_continent_bonus(player2_countries)
def get_bonus(countries_dict = countries.countries_dict):
    owners = get_owners(countries_dict)
    player1_countries = owners[0]
    player2_countries = owners[1]
    player1_bonus = get_continent_bonus(player1_countries) + len(player1_countries) // 4
    player2_bonus = get_continent_bonus(player2_countries) + len(player2_countries) // 4

    return [player1_bonus,player2_bonus]
def place(country, units,country_dict = countries.countries_dict):
    print("PLacing %d units on %s" %(units,country))
    country_dict[country][1] += units
def get_AI_action(max_depth,current_depth,country_dict,turn):
    possible_targets = get_possible_targets(turn,country_dict)
    #if(len(possible_targets) == 0):
        #print("returning -1")
    #    return -1
    if(current_depth < max_depth):
        #print("Current depth: %d" %(current_depth))
        current_depth += 1

        owners = get_owners(country_dict)
        if(len(owners[0]) == 0):
            #AI won
            #print("returning 1")
            #max_depth - current_depth
            return 1
        if(len(owners[1]) == 0):
            #print("returning 0")
            return -1
        #place_random(turn,country_dict)
        if(turn == 0):
            if(len(possible_targets) == 0):
                #random_attack = 0
                place_random(0,country_dict)
                #make_action(possible_targets[random_attack][0] + " " + possible_targets[random_attack][1],country_dict)
            else:
                random_attack = random.randint(0,len(possible_targets) - 1)

                person_bonus = get_bonus(country_dict)[0]
                add_bonus_to = possible_targets[random_attack][0]
                country_dict[add_bonus_to][1] += person_bonus
                #print(add_bonus_to)
                #country_dict[ possible_targets[random_attack][0][] ]   [1]  += person_bonus
                make_action(possible_targets[random_attack][0] + " " + possible_targets[random_attack][1],country_dict)
            turn = 1
            return get_AI_action(max_depth,current_depth,country_dict,turn)
        if(turn == 1):
            if(len(possible_targets) == 0):
                #random_attack = 0
                place_random(1,country_dict)
                #make_action(possible_targets[random_attack][0] + " " + possible_targets[random_attack][1],country_dict)
            else:
                random_attack = random.randint(0,len(possible_targets) - 1)

                #potentials = get_AI_actions(50,copy.deepcopy(country_dict))
                #for i in range(0, len(potentials)):
                #    if(potentials[i] == 1):
            #            random_attack = i
            #            break

                ai_bonus = get_bonus(country_dict)[1]
                add_bonus_to = possible_targets[random_attack][0]
                country_dict[add_bonus_to][1] += ai_bonus
                #country_dict[possible_targets[random_attack][0]]  [1] += person_bonus
                #place(possible_targets[random_attack][0],get_bonus(country_dict)[1],country_dict)
                make_action(possible_targets[random_attack][0] + " " + possible_targets[random_attack][1],country_dict)
            turn = 0
            return get_AI_action(max_depth,current_depth,country_dict,turn)
    else:
        return 0
def get_AI_actions(max_depth,country_dict = countries.countries_dict):
    #run random sim on every current possible choice
    #print("Getting AI Actions")
    poss = get_possible_targets(1,country_dict)
    poss_results = []
    for i in range(0, len(poss)):

        action = poss[i][0] + " " + poss[i][1]
        t = copy.deepcopy(country_dict)

        ai_bonus = get_bonus(t)[1]
        add_bonus_to = poss[i][0]
        t[add_bonus_to][1] += ai_bonus

        make_action(action,t)
        poss_results.append(get_AI_action(max_depth,0,t,0))
    return poss_results



turn = 0
game_over = False
winners = []
turns = 1


#HADNICAP RANDOM
#countries.countries_dict["Iceland"][2] = 0
#countries.countries_dict["Scandinavia"][2] = 1
#countries.countries_dict["Great_Britain"][2] = 1
#countries.countries_dict["Southern_Europe"][2] = 1
while not game_over:
    print_owners()
    player1_countries = get_owners()[0]
    player2_countries = get_owners()[1]
    #
    #HUMANS TURN
    #
    if(turn == 0):
        turns += 1
        #place_random(0)
        print("----------------------------------Player1(Human) Turn %d-----------------------------------------" %(turns))
        #possible_targets = get_possible_targets(0)

        #random_attack = random.randint(0,len(possible_targets) - 1)


        #person_bonus = get_bonus(countries.countries_dict)[0]
        #add_bonus_to = possible_targets[random_attack][0]
        #countries.countries_dict[add_bonus_to][1] += person_bonus

        #battle_result = make_action(possible_targets[random_attack][0] + " " + possible_targets[random_attack][1],countries.countries_dict)
        #print("Placing/Attacking random for human\n\n")
        #print( possible_targets[random_attack][0] + " --> " + possible_targets[random_attack][1]+ "\n\n")
        #print_owners()

        b = get_player_place(   (len(player1_countries)//4)  + get_continent_bonus(player1_countries))

        action = get_player_action()
        print(action)
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
        print("----------------------------------Player2(AI) Turn %d-----------------------------------------" %(turns))
        #print("AHHHH")
        possible_targets = get_possible_targets(1)
        if(possible_targets != 0):

            options_options = []
            count = [0] * len(possible_targets)
            sims = 60
            depth = 220
            print("running %d sims with max depth %d" %(sims,depth))
            for i in range(0,sims):
                if( i == int( sims * .1)):
                    print("10%")
                if( i == int( sims * .5)):
                    print("50%")
                if( i == int( sims * .9)):
                    print("90%")

                options_options.append((get_AI_actions(depth,copy.deepcopy(countries.countries_dict))))
            all_equal = None
            all_equal_bool =True
            for i in range(0, len(possible_targets)):
                for j in range(0, len(options_options)):
                    #print(options_options[j][i])
                    count[i] += options_options[j][i]
                    if(all_equal == None):
                        all_equal = count[i]

                    if(count[i] != all_equal):
                        all_equal_bool = False
                    #if(count[i] == None):
                    #    count[i] = options_options[j][i]
                    #elif(count[i] < options_options[j][i]):
                    #    count[i] = options_options[j][i]
                #print("\n\n")
            #print(count)
            #print(possible_targets)
            #ya dont need both idiot
            max = None
            max_ind = None
            for i in range(0, len(possible_targets)):
                if(i == 0):
                    max_ind = i
                    max = count[i]
                else:
                    if (max < count[i]):
                        max_ind = i
                        max = count[i]
                print("%s %d" %(possible_targets[i],count[i]))
            best_action = possible_targets[max_ind]
            print("\nBest action %s %d" %(best_action,count[max_ind]))
            #place_random(turn)
            #AB = best_action.split()
            #place_at = AB[0]
            ai_bonus =  get_bonus()[1]
            countries.countries_dict[best_action[0]][1] += ai_bonus
            print("AI Bonus %d\n" %(ai_bonus))
            make_action(best_action[0] + " " + best_action[1])
        else:
            print("AI out of moves")
            place_random(1)
        turn = 0
    player1_countries = get_owners()[0]
    if(len(player1_countries) == 42 or len(player1_countries) == 0):
        if(len(player1_countries) == 0):
            winners.append(1)
        else:
            winners.append(0)

        game_over = True
    for i in range(0,len(winners)):
        if(winners[i] == 0):
            print("game %d winner: bad player" %(i))
        else:
            print("game %d winner: AI" %(i))
