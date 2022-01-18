#Text-based role playing game with turn-based combat

#characters can be added when there are less than 2 players
#player input values
number_of_characters = 0
player_list = {'Player 1':{'Character Profile':"",'Secondary Stats':"",'Inventory':"", 'Combat Stats':""}, 
               'Player 2':{'Character Profile':"",'Secondary Stats':"",'Inventory':"", 'Combat Stats':""}}
races = ['Human','Elf','Dwarf','Orc']
genders = ['Male', 'Female', 'Unknown']
while number_of_characters < 2:
    player_number = number_of_characters + 1
    character_profile = {'Name':"", 'Description':"",'Race':"",'Sex':"",'Strength':0,'Intellect':0,'Dexterity':0,'Charisma':0}
    print('What is your name? ')
    character_profile['Name'] = input()
    print('Describe your character: ')
    character_profile['Description'] = input()
    print('What is your race? (Human, Elf, Dwarf, Orc) ')
    race = input()
    if race not in races:
        while race not in races:
            print('Invalid race. Please choose again from (Human, Elf, Dwarf, Orc). ')
            race = input()
    else:
        character_profile['Race'] = race
    print('What is your gender? (Male, Female, Unknown) ')
    gender = input()
    if gender not in genders:
        while gender not in genders:
            print('Invalid gender. Please choose again from (Male, Female, Unknown). ')
            gender = input()
    else:
        character_profile['Sex'] = gender
    print('Is your information correct? (Yes or No) ')
    user_confirmation = input()
    if user_confirmation == 'Yes':
        if player_number == 1:
            player_list['Player 1']['Character Profile'] = character_profile
        elif player_number == 2:
            player_list['Player 2']['Character Profile'] = character_profile
        number_of_characters += 1
    elif user_confirmation == 'No':
        print('Which section would you like to change? (Name, Description, Race, or Sex) ')
        edit = input()
        print('Please make desired changes. ')
        character_profile[edit] = input()
        print('Is your information correct? (Yes or No) ')
        user_confirmation = input()
        if user_confirmation == 'Yes':
            if player_number == 1:
                player_list['Player 1']['Character Profile'] = character_profile
            elif player_number == 2:
                player_list['Player 2']['Character Profile'] = character_profile
    else:
        while user_confirmation not in ['Yes', 'No']:
            print('Invalid input. Please type "Yes" or "No". ')
            user_confirmation = input()
        if user_confirmation == 'Yes':
            if player_number == 1:
                player_list['Player 1']['Character Profile'] = character_profile
            elif player_number == 2:
                player_list['Player 2']['Character Profile'] = character_profile
            number_of_characters += 1
    print("\n")
    
#Randomized Character Stats
import random
player_list['Player 1']['Character Profile']['Strength'] = random.randint(1,100)
player_list['Player 1']['Character Profile']['Intellect'] = random.randint(1,100)
player_list['Player 1']['Character Profile']['Dexterity'] = random.randint(1,100)
player_list['Player 1']['Character Profile']['Charisma'] = random.randint(1,100)
player_list['Player 2']['Character Profile']['Strength'] = random.randint(1,100)
player_list['Player 2']['Character Profile']['Intellect'] = random.randint(1,100)
player_list['Player 2']['Character Profile']['Dexterity'] = random.randint(1,100)
player_list['Player 2']['Character Profile']['Charisma'] = random.randint(1,100)

#Adjusting for Character types
for i in [1,2]:
    player_number = 'Player ' + str(i)
#Elf Changes
    if player_list[player_number]['Character Profile']['Race'] == 'Elf':
        if (player_list[player_number]['Character Profile']['Dexterity'] + 5) <= 100:
            player_list[player_number]['Character Profile']['Dexterity'] += 5
        else:
            player_list[player_number]['Character Profile']['Dexterity'] = min((player_list[player_number]['Character Profile']['Dexterity'] + 5), 100)
        if (player_list[player_number]['Character Profile']['Intellect'] + 9) <= 100:
            player_list[player_number]['Character Profile']['Intellect'] += 9
        else:
            player_list[player_number]['Character Profile']['Intellect'] = min((player_list[player_number]['Character Profile']['Intellect'] + 9), 100)
        if (player_list[player_number]['Character Profile']['Strength'] - 9) >= 0:
            player_list[player_number]['Character Profile']['Strength'] -= 9
        else:
            player_list[player_number]['Character Profile']['Strength'] = max((player_list[player_number]['Character Profile']['Strength'] - 9), 0)

#Dwarf Changes    
    elif player_list[player_number]['Character Profile']['Race'] == 'Dwarf':
        if (player_list[player_number]['Character Profile']['Dexterity'] + 8) <= 100:
            player_list[player_number]['Character Profile']['Dexterity'] += 8
        else:
            player_list[player_number]['Character Profile']['Dexterity'] = min((player_list[player_number]['Character Profile']['Dexterity'] + 8), 100)
        if (player_list[player_number]['Character Profile']['Strength'] + 15) <= 100:
            player_list[player_number]['Character Profile']['Strength'] += 15
        else:
            player_list[player_number]['Character Profile']['Strength'] = min((player_list[player_number]['Character Profile']['Strength'] + 15), 100)
        if (player_list[player_number]['Character Profile']['Intellect'] - 9) >= 0:
            player_list[player_number]['Character Profile']['Intellect'] -= 9
        else:
            player_list[player_number]['Character Profile']['Intellect'] = max((player_list[player_number]['Character Profile']['Intellect'] - 9), 0)

#Orc Changes    
    elif player_list[player_number]['Character Profile']['Race'] == 'Orc':
        if (player_list[player_number]['Character Profile']['Dexterity'] + 18) <= 100:
            player_list[player_number]['Character Profile']['Dexterity'] += 18
        else:
            player_list[player_number]['Character Profile']['Dexterity'] = min((player_list[player_number]['Character Profile']['Dexterity'] + 18), 100)
        if (player_list[player_number]['Character Profile']['Strength'] + 25) <= 100:
            player_list[player_number]['Character Profile']['Strength'] += 25
        else:
            player_list[player_number]['Character Profile']['Strength'] = min((player_list[player_number]['Character Profile']['Strength'] + 25), 100)
        if (player_list[player_number]['Character Profile']['Intellect'] - 18) >= 0:
            player_list[player_number]['Character Profile']['Intellect'] -= 18
        else:
            player_list[player_number]['Character Profile']['Intellect'] = max((player_list[player_number]['Character Profile']['Intellect'] - 18), 0)
        if (player_list[player_number]['Character Profile']['Charisma'] - 30) >= 0:
            player_list[player_number]['Character Profile']['Charisma'] -= 30
        else:
            player_list[player_number]['Character Profile']['Charisma'] = max((player_list[player_number]['Character Profile']['Charisma'] - 30), 0)

#Male changes
    if player_list[player_number]['Character Profile']['Sex'] == 'Male':
        if (player_list[player_number]['Character Profile']['Strength'] + 3) <= 100:
            player_list[player_number]['Character Profile']['Strength'] += 3
        else:
            player_list[player_number]['Character Profile']['Strength'] = min((player_list[player_number]['Character Profile']['Strength'] + 3), 100)
        if (player_list[player_number]['Character Profile']['Charisma'] - 5) >= 0:
            player_list[player_number]['Character Profile']['Charisma'] -= 5
        else:
            player_list[player_number]['Character Profile']['Charisma'] = max((player_list[player_number]['Character Profile']['Charisma'] - 5), 0)

#Female changes
    elif player_list[player_number]['Character Profile']['Sex'] == 'Female':
        if (player_list[player_number]['Character Profile']['Dexterity'] + 3) <= 100:
            player_list[player_number]['Character Profile']['Dexterity'] += 3
        else:
            player_list[player_number]['Character Profile']['Dexterity'] = min((player_list[player_number]['Character Profile']['Dexterity'] + 3), 100)
        if (player_list[player_number]['Character Profile']['Charisma'] + 2) <= 100:
            player_list[player_number]['Character Profile']['Charisma'] += 2
        else:
            player_list[player_number]['Character Profile']['Charisma'] = min((player_list[player_number]['Character Profile']['Charisma'] + 2), 100)
        if (player_list[player_number]['Character Profile']['Strength'] - 5) >= 0:
            player_list[player_number]['Character Profile']['Strength'] -= 5
        else:
            player_list[player_number]['Character Profile']['Strength'] = max((player_list[player_number]['Character Profile']['Strength'] - 5), 0)

#Secondary character stats
for i in [1,2]:
    player_number = 'Player ' + str(i)
    Secondary_Stats = {'Health':100,'Mana':100,'Armor':0,'Gold':0}
    player_list[player_number]['Secondary Stats'] = Secondary_Stats
    player_list[player_number]['Secondary Stats']['Gold'] = random.randint(50,80)
    

#Display Character Stats
for i in [1,2]:
    player_number = 'Player ' + str(i)
    for key in player_list[player_number]['Character Profile']:
        print(key + ': ' + str(player_list[player_number]['Character Profile'][key]))
    print("\n")
    for key in player_list[player_number]['Secondary Stats']:
        print(key + ': ' + str(player_list[player_number]['Secondary Stats'][key]))
    print("\n")

#trader's inventory
#weapons of the form (price, attack damage, speed)
trader = {'Items':"",'Inventory':""}
stapler = (10, 10, 'Regular')
lunch_box = (20, 25, 'Slow')
hair_straightner = (40, 50, 'Slow')
pencil = (5, 5, 'Fast')
trader['Items'] = {'Stapler':stapler, 'Lunch Box':lunch_box,'Hair Straightner':hair_straightner,'Pencil':pencil}
trader['Inventory'] = {'Stapler':random.randint(1,2),'Lunch Box':random.randint(1,2),'Hair Straightner':random.randint(1,2),'Pencil':random.randint(1,2)}
print('Available items: ')
print(trader['Inventory'])
print("\n")
print('Item stats: ')
print('Item stats displayed as (price, attack damage, speed)')
print(trader['Items'])
print("\n")

#Ask players to purchase items
purchase_counter = 1
print('Please purchase items from the trader or type "no" to stop.')
print('If player charisma is below 20, actual costs are 10% higher than standard (truncated to nearest whole number).')
print('If player charisma exceeds 80, actual costs are 10% lower than standard (trunacted to nearest whole number).')
print("\n")
player_1_inventory = []
player_2_inventory = []
print(player_list['Player 1']['Character Profile']['Name'] + ' available gold ' + str(player_list['Player 1']['Secondary Stats']['Gold']))
purchase_prompt = player_list['Player 1']['Character Profile']['Name'] + ' please purchase an item. ' 
print(purchase_prompt)
purchase = input()
print("\n")
while True:
# player 1 purchases
    if purchase_counter % 2 == 1:   
        if purchase not in trader['Inventory'] and purchase != 'no':
            while purchase not in trader['Inventory'] and purchase != 'no':
                print('Invalid input. Please try again. ')
                purchase = input()
                print("\n")
        elif purchase == 'no':
             print(player_list['Player 2']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
             print("\n")
             purchase_prompt = player_list['Player 2']['Character Profile']['Name'] + ' please purchase your last item. '
             print(purchase_prompt)
             purchase = input()
             if purchase not in trader['Inventory'] and purchase != 'no':
                while purchase not in trader['Inventory'] and purchase != 'no':
                    print('Invalid input. Please try again. ')
                    purchase = input()
                    print("\n")
             elif purchase == 'no':
                 break
             else:
                cost = trader['Items'][purchase][0]
                if player_list['Player 2']['Character Profile']['Charisma'] < 20:
                    cost = int(cost * 1.1)
                elif player_list['Player 2']['Character Profile']['Charisma'] > 80:
                    cost = int(cost * 0.9)
                if player_list['Player 2']['Secondary Stats']['Gold'] >  cost and trader['Inventory'][purchase] > 0:
                   player_2_inventory.append(purchase)
                   player_list['Player 2']['Secondary Stats']['Gold'] -= cost
                   trader['Inventory'][purchase] -= 1
                elif player_list['Player 2']['Secondary Stats']['Gold'] < cost:
                    while player_list['Player 2']['Secondary Stats']['Gold'] < cost:
                        print('You don\'t have enough money for that! ')
                        print('Buy something you can afford. ')
                        purchase = input()
                elif trader['Inventory'][purchase] <= 0:
                    while trader['Inventory'][purchase] <= 0:
                        print('Desired item is out of stock.')
                        print('Buy something else. ')
                        purchase = input()
                print(player_2_inventory)
                break
        else:
            cost = trader['Items'][purchase][0]
            if player_list['Player 1']['Character Profile']['Charisma'] < 20:
                 cost = int(cost * 1.1)
            elif player_list['Player 1']['Character Profile']['Charisma'] > 80:
                 cost = int(cost * 0.9)
            if player_list['Player 1']['Secondary Stats']['Gold'] > cost and trader['Inventory'][purchase] > 0:
                player_1_inventory.append(purchase)
                player_list['Player 1']['Secondary Stats']['Gold'] -= cost
                trader['Inventory'][purchase] -= 1
            elif player_list['Player 1']['Secondary Stats']['Gold'] < cost:
                while player_list['Player 1']['Secondary Stats']['Gold'] < cost:
                    print('You can\'t afford that!')
                    print('Buy something you can afford. ')
                    purchase = input()
            elif trader['Inventory'][purchase] <= 0:
                while trader['Inventory'][purchase] <= 0:
                    print('Desired item is out of stock.')
                    print('Buy something else. ')
                    purchase = input()
        print(player_1_inventory)
        print(player_list['Player 1']['Character Profile']['Name'] + ' Available gold: ' + str(player_list['Player 1']['Secondary Stats']['Gold']))
        print("\n")

# player 2 purchases
    elif purchase_counter % 2 == 0:   
        if purchase not in trader['Inventory'] and purchase != 'no':
            while purchase not in trader['Inventory'] and purchase != 'no':
                print('Invalid input. Please try again. ')
                purchase = input()
        elif purchase == 'no':
            break
        else:
            cost = trader['Items'][purchase][0]
            if player_list['Player 2']['Character Profile']['Charisma'] < 20:
                 cost = int(cost * 1.1)
            elif player_list['Player 2']['Character Profile']['Charisma'] > 80:
                 cost = int(cost * 0.9)
            if player_list['Player 2']['Secondary Stats']['Gold'] > cost and trader['Inventory'][purchase] > 0:
                player_2_inventory.append(purchase)
                player_list['Player 2']['Secondary Stats']['Gold'] -= cost
                trader['Inventory'][purchase] -= 1
            elif player_list['Player 2']['Secondary Stats']['Gold'] < cost:
                while player_list['Player 2']['Secondary Stats']['Gold'] < cost:
                    print('You can\'t afford that!')
                    print('Buy something you can afford. ')
                    purchase = input()
            elif trader['Inventory'][purchase] <= 0:
                while trader['Inventory'][purchase] <= 0:
                    print('Desired item is out of stock.')
                    print('Buy something else. ')
                    purchase = input()
        print(player_2_inventory)
        print(player_list['Player 2']['Character Profile']['Name'] + ' Available gold: ' + str(player_list['Player 2']['Secondary Stats']['Gold']))
        print("\n")

# Regardless of player
    purchase_counter += 1
    print('Available items: ')
    print(trader['Inventory'])
    print("\n")
    print('Item stats displayed as (price, attack damage, speed)')
    print(trader['Items'])
    print("\n")
    if trader['Inventory']['Stapler'] == 0 and trader['Inventory']['Lunch Box'] == 0 and trader['Inventory']['Hair Straightner'] == 0 and trader['Inventory']['Pencil'] == 0:
        break
    if purchase_counter % 2 == 0:
        purchase_prompt = player_list['Player 2']['Character Profile']['Name'] + ' please purchase an item. '
        gold = 'Available gold: ' + str(player_list['Player 2']['Secondary Stats']['Gold'])
    elif purchase_counter % 2 == 1:
        purchase_prompt = player_list['Player 1']['Character Profile']['Name'] + ' please purchase an item. '
        gold = 'Available gold: ' + str(player_list['Player 1']['Secondary Stats']['Gold'])
    print(gold)
    print(purchase_prompt)
    purchase = input()
    print("\n")  

#convert player inventories from lists to dictionaries and assign to inventory section of player list
temp_inventory_1 = dict.fromkeys(player_1_inventory)
for key in temp_inventory_1:
    temp_inventory_1[key] = trader['Items'][key]
player_list['Player 1']['Inventory'] = temp_inventory_1
temp_inventory_2 = dict.fromkeys(player_2_inventory)
for key in temp_inventory_2:
    temp_inventory_2[key] = trader['Items'][key]
player_list['Player 2']['Inventory'] = temp_inventory_2

#introducing combat stats
print("\n")
print('combat stats consist of hits, misses, damage taken, and health update')
print('hits records the number of successful strikes on the enemy')
print('misses records the number of successfully dodged enemy attacks')
print('damage taken reflects all damage taken throughout the battle')
print('health update is your character\'s current health')
print('Character strength affects damage dealt.')
print('Character dexterity affects chance of hitting target.')
print('Character intellect affects mana costs.')
print("\n")
for i in [1,2]:
    player_number = 'Player ' + str(i)
    Combat_Stats = {'hits':0,'misses':0,'damage taken':0,'health update':""}
    player_list[player_number]['Combat Stats'] = Combat_Stats

#Starting Combat
turn_counter = 1
while True:
    player_1_combat_inventory = dict.fromkeys(player_list['Player 1']['Inventory'].keys())
    player_2_combat_inventory = dict.fromkeys(player_list['Player 2']['Inventory'].keys())
    for key in player_list['Player 1']['Inventory']:
        player_1_combat_inventory[key] = (player_list['Player 1']['Inventory'][key][1] , player_list['Player 1']['Inventory'][key][2])
    for key in player_list['Player 2']['Inventory']:
        player_2_combat_inventory[key] = (player_list['Player 2']['Inventory'][key][1] , player_list['Player 2']['Inventory'][key][2])
    
#Player 1 attacks        
    if turn_counter % 2 == 1:
        if turn_counter != 1:
            player_list['Player 1']['Secondary Stats']['Mana'] += 3
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s stats')
        for i in ['Health','Mana','Armor']:
            print(i + ': ' + str(player_list['Player 1']['Secondary Stats'][i]))
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s combat stats')
        for key in player_list['Player 1']['Combat Stats']:
            print(key + ': ' + str(player_list['Player 1']['Combat Stats'][key]))
        print("\n")
        print(player_list['Player 1']['Character Profile']['Name'] + ' please equip a weapon from your inventory. (type none for default weapon)')
        print('Weapon stats displayed as "name":(damage, speed).')
        print(player_1_combat_inventory)
        equip = input()
        if equip not in player_1_combat_inventory or equip == 'none':
            equipped_name = 'Fist'
            equipped = (2, 'regular')
        else:
            equipped_name = equip
            equipped = player_1_combat_inventory[equip]
        print('Equipped weapon: ')
        print(equipped_name)
        print(equipped)
        print("\n")
        if player_list['Player 1']['Secondary Stats']['Mana'] <= 0:
            print(player_list['Player 1']['Characater Profile']['Name'] + ' missed!')
            player_list['Player 1']['Combat Stats']['misses'] += 1    
        else:
            if player_list['Player 1']['Character Profile']['Dexterity'] < 30:
                hit_chance = random.randint(-5,1)
            elif player_list['Player 1']['Character Profile']['Dexterity'] > 70:
                hit_chance = random.randint(-1,5)
            else:
                hit_chance = random.randint(-3,3)
            if player_list['Player 1']['Character Profile']['Intellect'] < 30:
                mana_cost = 15
            elif player_list['Player 1']['Character Profile']['Intellect'] > 70:
                mana_cost = 5
            else:
                mana_cost = 10
            damage_dealt = equipped[0]
            if player_list['Player 1']['Character Profile']['Strength'] < 15:
                damage_dealt = int(damage_dealt * 0.8)
            elif player_list['Player 1']['Character Profile']['Strength'] > 85:
                damage_dealt = int(damage_dealt * 1.2)
            if equipped[1] == 'Slow':
                damage_dealt += 5
                player_list['Player 1']['Secondary Stats']['Health'] -= 2
            elif equipped[1] == 'Fast':
                damage_dealt -= 2
                mana_cost = int(mana_cost * 0.95)
            if hit_chance >= 0:
                print(player_list['Player 1']['Character Profile']['Name'] + '\'s attack hit!')
                player_list['Player 2']['Secondary Stats']['Health'] -= damage_dealt
                player_list['Player 2']['Combat Stats']['damage taken'] = damage_dealt
                player_list['Player 1']['Secondary Stats']['Mana'] -= mana_cost
                player_list['Player 1']['Combat Stats']['hits'] += 1
            else:
                print(player_list['Player 1']['Character Profile']['Name'] + ' missed!')
                player_list['Player 1']['Secondary Stats']['Mana'] -= int(mana_cost*0.4)
                player_list['Player 1']['Combat Stats']['misses'] += 1
        print('End of ' + player_list['Player 1']['Character Profile']['Name'] + '\'s turn.')
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s stats')
        for i in ['Health','Mana','Armor']:
            print(i + ': ' + str(player_list['Player 1']['Secondary Stats'][i]))
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s combat stats')
        for key in player_list['Player 1']['Combat Stats']:
            print(key + ': ' + str(player_list['Player 1']['Combat Stats'][key]))
        print("\n")
        if player_list['Player 2']['Secondary Stats']['Health'] <= 0:
            print(player_list['Player 1']['Character Profile']['Name'] + ' the ' + player_list['Player 1']['Character Profile']['Description'] + ' ' + player_list['Player 1']['Character Profile']['Sex'] + ' ' + player_list['Player 1']['Character Profile']['Race'] + ' won the battle!')
            break
        turn_counter += 1

#Player 2 attacks
    elif turn_counter % 2 == 0:
        if turn_counter != 2:
            player_list['Player 2']['Secondary Stats']['Mana'] += 3
        print(player_list['Player 2']['Character Profile']['Name'] + '\'s stats')
        for i in ['Health','Mana','Armor']:
            print(i + ': ' + str(player_list['Player 2']['Secondary Stats'][i]))
        print(player_list['Player 2']['Character Profile']['Name'] + '\'s combat stats')
        for key in player_list['Player 2']['Combat Stats']:
            print(key + ': ' + str(player_list['Player 2']['Combat Stats'][key]))
        print("\n")
        print(player_list['Player 2']['Character Profile']['Name'] + ' please equip a weapon from your inventory. (type none for default weapon)')
        print('Weapon stats displayed as "name":(damage, speed).')
        print(player_2_combat_inventory)
        equip = input()
        if equip not in player_2_combat_inventory or equip == 'none':
            equipped_name = 'Fist'
            equipped = (2, 'regular')
        else:
            equipped_name = equip
            equipped = player_2_combat_inventory[equip]
        print('Equipped weapon: ')
        print(equipped_name)
        print(equipped)
        print("\n")
        if player_list['Player 2']['Secondary Stats']['Mana'] <= 0:
            print(player_list['Player 2']['Character Profile']['Name'] + ' missed!')
            player_list['Player 2']['Combat Stats']['misses'] += 1    
        else:
            if player_list['Player 2']['Character Profile']['Dexterity'] < 30:
                hit_chance = random.randint(-5,1)
            elif player_list['Player 2']['Character Profile']['Dexterity'] > 70:
                hit_chance = random.randint(-1,5)
            else:
                hit_chance = random.randint(-3,3)
            if player_list['Player 2']['Character Profile']['Intellect'] < 30:
                mana_cost = 15
            elif player_list['Player 2']['Character Profile']['Intellect'] > 70:
                mana_cost = 5
            else:
                mana_cost = 10
            damage_dealt = equipped[0]
            if player_list['Player 2']['Character Profile']['Strength'] < 15:
                damage_dealt = int(damage_dealt * 0.8)
            elif player_list['Player 2']['Character Profile']['Strength'] > 85:
                damage_dealt = int(damage_dealt * 1.2)
            if player_list['Player 2']['Character Profile']['Strength'] < 15:
                damage_dealt = int(damage_dealt * 0.8)
            elif player_list['Player 2']['Character Profile']['Strength'] > 85:
                damage_dealt = int(damage_dealt * 1.2)
            if equipped[1] == 'Slow':
                damage_dealt += 5
                player_list['Player 2']['Secondary Stats']['Health'] -= 2
            elif equipped[1] == 'Fast':
                damage_dealt -= 2
                mana_cost = int(mana_cost * 0.95)
            if hit_chance >= 0:
                print(player_list['Player 2']['Character Profile']['Name'] + '\'s attack hit!')
                player_list['Player 1']['Secondary Stats']['Health'] -= damage_dealt
                player_list['Player 1']['Combat Stats']['damage taken'] = damage_dealt
                player_list['Player 2']['Secondary Stats']['Mana'] -= mana_cost
                player_list['Player 2']['Combat Stats']['hits'] += 1
            else:
                print(player_list['Player 2']['Character Profile']['Name'] + ' missed!')
                player_list['Player 2']['Secondary Stats']['Mana'] -= int(mana_cost*0.4)
                player_list['Player 2']['Combat Stats']['misses'] += 1
        print('End of ' + player_list['Player 2']['Character Profile']['Name'] + '\'s turn.')
        print(player_list['Player 2']['Character Profile']['Name'] + '\'s stats')
        for i in ['Health','Mana','Armor']:
            print(i + ': ' + str(player_list['Player 2']['Secondary Stats'][i]))
        print(player_list['Player 2']['Character Profile']['Name'] + '\'s combat stats')
        for key in player_list['Player 2']['Combat Stats']:
            print(key + ': ' + str(player_list['Player 2']['Combat Stats'][key]))
        print("\n")
        if player_list['Player 1']['Secondary Stats']['Health'] <= 0:
            print(player_list['Player 2']['Character Profile']['Name'] + ' the ' + player_list['Player 2']['Character Profile']['Description'] + ' ' + player_list['Player 2']['Character Profile']['Sex'] + ' ' + player_list['Player 2']['Character Profile']['Race'] + ' won the battle!')
            break
        turn_counter += 1
print("\n")
print('Thank you for playing!')