#Text-based role playing game with turn-based combat

#character creation
#characters can be added when there are less than 2 players
#initializing values
number_of_characters = 0
player_list = {'Player 1':{'Character Profile':"",'Secondary Stats':"",'Inventory':"", 'Combat Stats':""}, 
               'Player 2':{'Character Profile':"",'Secondary Stats':"",'Inventory':"", 'Combat Stats':""}}
races = ['Human','Elf','Dwarf','Orc']
genders = ['Male', 'Female', 'Unknown']

#player input values
while number_of_characters < 2:
    player_number = number_of_characters + 1
    character_profile = {'Name':"", 'Description':"",'Race':"",'Sex':"",'Strength':0,'Intellect':0,'Dexterity':0,'Charisma':0}

#name and descripion can take any value
    print('What is your name? ')
    character_profile['Name'] = input()
    print('Describe your character: ')
    character_profile['Description'] = input()

#race and gender can only take on prescified values as they affect game play
#check values against list of possible values
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

#allow users to go back and change character information
    print('Is your information correct? (Yes or No) ')
    user_confirmation = input()
    if user_confirmation not in ['Yes', 'No']:
        while user_confirmation not in ['Yes', 'No']:
            print('Invalid input. Please type "Yes" or "No". ')
            user_confirmation = input()
        if user_confirmation == 'Yes':
            if player_number == 1:
                player_list['Player 1']['Character Profile'] = character_profile
            elif player_number == 2:
                player_list['Player 2']['Character Profile'] = character_profile
            number_of_characters += 1
        else:
            continue
    elif user_confirmation == 'Yes':
        if player_number == 1:
            player_list['Player 1']['Character Profile'] = character_profile
        elif player_number == 2:
            player_list['Player 2']['Character Profile'] = character_profile
        number_of_characters += 1
    elif user_confirmation == 'No':
        continue
    print("\n")
    
#Randomized Character Stats
import random
for i in [1,2]:
    player_number = 'Player ' + str(i)
    for j in ['Strength','Intellect','Dexterity','Charisma']:
        player_list[player_number]['Character Profile'][j] = random.randint(1,100)

#Adjusting for Character types
for i in [1,2]:
    player_number = 'Player ' + str(i)

#Elf Changes
    if player_list[player_number]['Character Profile']['Race'] == 'Elf':
        player_list[player_number]['Character Profile']['Dexterity'] = min((player_list[player_number]['Character Profile']['Dexterity'] + 5), 100)
        player_list[player_number]['Character Profile']['Intellect'] = min((player_list[player_number]['Character Profile']['Intellect'] + 9), 100)
        player_list[player_number]['Character Profile']['Strength'] = max((player_list[player_number]['Character Profile']['Strength'] - 9), 0)

#Dwarf Changes    
    elif player_list[player_number]['Character Profile']['Race'] == 'Dwarf':
        player_list[player_number]['Character Profile']['Dexterity'] = min((player_list[player_number]['Character Profile']['Dexterity'] + 8), 100)
        player_list[player_number]['Character Profile']['Strength'] = min((player_list[player_number]['Character Profile']['Strength'] + 15), 100)
        player_list[player_number]['Character Profile']['Intellect'] = max((player_list[player_number]['Character Profile']['Intellect'] - 9), 0)

#Orc Changes    
    elif player_list[player_number]['Character Profile']['Race'] == 'Orc':
        player_list[player_number]['Character Profile']['Dexterity'] = min((player_list[player_number]['Character Profile']['Dexterity'] + 18), 100)
        player_list[player_number]['Character Profile']['Strength'] = min((player_list[player_number]['Character Profile']['Strength'] + 25), 100)
        player_list[player_number]['Character Profile']['Intellect'] = max((player_list[player_number]['Character Profile']['Intellect'] - 18), 0)
        player_list[player_number]['Character Profile']['Charisma'] = max((player_list[player_number]['Character Profile']['Charisma'] - 30), 0)

#Male changes
    if player_list[player_number]['Character Profile']['Sex'] == 'Male':
        player_list[player_number]['Character Profile']['Strength'] = min((player_list[player_number]['Character Profile']['Strength'] + 3), 100)
        player_list[player_number]['Character Profile']['Charisma'] = max((player_list[player_number]['Character Profile']['Charisma'] - 5), 0)

#Female changes
    elif player_list[player_number]['Character Profile']['Sex'] == 'Female':
        player_list[player_number]['Character Profile']['Dexterity'] = min((player_list[player_number]['Character Profile']['Dexterity'] + 3), 100)
        player_list[player_number]['Character Profile']['Charisma'] = min((player_list[player_number]['Character Profile']['Charisma'] + 2), 100)
        player_list[player_number]['Character Profile']['Strength'] = max((player_list[player_number]['Character Profile']['Strength'] - 5), 0)

#Secondary character stats
for i in [1,2]:
    player_number = 'Player ' + str(i)
    Secondary_Stats = {'Health':100,'Mana':100,'Armor':0,'Gold':0}
    player_list[player_number]['Secondary Stats'] = Secondary_Stats
    player_list[player_number]['Secondary Stats']['Gold'] = random.randint(80,110)
    

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
#armor of the form (price, armor)
#healing items of the form (price, amount of health/mana restored)

trader = {'Weapons':"", 'Weapons Inventory':"", 'Armor':"", 'Armor Inventory':"", 'Healing Items':"", 'Healing Items Inventory':""}

#Weapons section
stapler = (10, 10, 'Regular')
lunch_box = (20, 25, 'Slow')
hair_straightner = (40, 50, 'Slow')
pencil = (5, 5, 'Fast')
trader['Weapons'] = {'Stapler':stapler, 'Lunch Box':lunch_box,'Hair Straightner':hair_straightner,'Pencil':pencil}
trader['Weapons Inventory'] = {'Stapler':random.randint(1,2),'Lunch Box':random.randint(1,2),'Hair Straightner':random.randint(0,2),'Pencil':random.randint(1,4)}

#Armor section
woolen_hat = (8,10)
pasta_strainer = (15, 20)
winter_coat = (40,50)
pot_lid = (3,6)
trader['Armor'] = {'Woolen Hat':woolen_hat, 'Pasta Strainer':pasta_strainer, 'Winter Coat':winter_coat, 'Pot Lid':pot_lid}
trader['Armor Inventory']  = {'Woolen Hat':random.randint(0,4), 'Pasta Strainer':random.randint(1,2), 'Winter Coat':random.randint(0,2), 'Pot Lid':random.randint(1,3)}
 
#Healing items section
band_aid = (1,3)
steak = (20,30)
vinegar = (10,15)
trader['Healing Items'] = {'Band Aid':band_aid, 'Steak':steak, 'Vinegar':vinegar}
trader['Healing Items Inventory'] = {'Band Aid':random.randint(4,8), 'Steak':random.randint(0,2), 'Vinegar':random.randint(1,4)}
 
#Display different item types/inventories
for item_type in ['Weapons', 'Armor', 'Healing Items']:
    print('Available ' + item_type + ': ')
    inventory = item_type + ' Inventory'
    print(trader[inventory])
    print("\n")
    print(item_type + ' stats: ')
    if item_type == 'Weapons':
        print('Weapon stats displayed as (price, attack damage, speed)')
    elif item_type == 'Armor':
        print('Armor stats displayed as (price, armor)')
    elif item_type == 'Healing Items':
        print('Healing Item stats displayed as (price, amount of health/mana restored)')
    print(trader[item_type])
    print("\n")

#purchasing items to prepare for battle
#Initial purchase
purchase_counter = random.randint(1,2)
first = purchase_counter
print('Please purchase items from the trader or type "no" to stop.')
print('If player charisma is below 20, actual costs are 10% higher than standard (truncated to nearest whole number).')
print('If player charisma exceeds 80, actual costs are 10% lower than standard (trunacted to nearest whole number).')
print("\n")
player_1_inventory = []
player_2_inventory = []
if purchase_counter % 2 == 1:
    print(player_list['Player 1']['Character Profile']['Name'] + ' available gold ' + str(player_list['Player 1']['Secondary Stats']['Gold']))
    print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
    print(player_1_inventory)
    item_type = player_list['Player 1']['Character Profile']['Name'] + ' please select a type of item to purchase (Weapons, Armor, Healing Items). ' 
    purchase_prompt = player_list['Player 1']['Character Profile']['Name'] + ' which item would you like to buy?'
else:
    print(player_list['Player 2']['Character Profile']['Name'] + ' available gold ' + str(player_list['Player 2']['Secondary Stats']['Gold']))
    print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
    print(player_2_inventory)
    item_type = player_list['Player 2']['Character Profile']['Name'] + ' please select a type of item to purchase (Weapons, Armor, Healing Items). ' 
    purchase_prompt = player_list['Player 2']['Character Profile']['Name'] + ' which item would you like to buy?' 
print(item_type)
print(purchase_prompt)
category = input()
print("\n")

#Continued purchasing
while True:

#player 1 stops purchasing items and player 1 made first purchase
    if category == 'no' and purchase_counter % 2 == 1 and first % 2 == 1:
        print(player_list['Player 2']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
        print("\n")
        print(player_list['Player 2']['Character Profile']['Name'] + ' please purchase your last item. ')
        print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
        print(player_2_inventory)

        print('What type of item would you like to buy?')
        category = input()

#player 2 ends purchasing at category selection
        if category == 'no':
            break

        if category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
            while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                print('Invalid input. Please try again. ')
                category = input()
                print("\n")
        
        if category == 'no':
            break

        elif category == 'Weapons':
            print(trader['Weapons Inventory'])
        elif category == 'Armor':
            print(trader['Armor Inventory'])
        elif category == 'Healing Items':
            print(trader['Healing Items Inventory'])

        print('Make your selection.')
        purchase = input()
        inventory = category + ' Inventory'

#player 2 ends purchasing at item selection stage
        if purchase == 'no':
            break

        if purchase not in trader[inventory].keys() and purchase != 'no':
            while purchase not in trader[inventory].keys() and purchase != 'no':
                print('Invalid purchase.')
                purchase = input()

        if purchase == 'no':
            break

#player 2 purchases one last item
        cost = trader[category][purchase][0]

#cost adjustments to reflect charisma
        if player_list['Player 2']['Character Profile']['Charisma'] < 20:
            cost = int(cost * 1.1)
        elif player_list['Player 2']['Character Profile']['Charisma'] > 80:
            cost = int(cost * 0.9)

#player 2 successfully purchases an item
        if player_list['Player 2']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
            player_2_inventory.append(purchase)
            player_list['Player 2']['Secondary Stats']['Gold'] -= cost
            trader[inventory][purchase] -= 1

#failed purchase due to insufficient funds
        elif player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
            while player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                print('You don\'t have enough money for that! ')
                print('Buy something you can afford. ')
                purchase = input()

        if purchase == 'no':
            break

#failed purchase due to lack of inventory
        elif trader[inventory][purchase] <= 0 and purchase != 'no':
            while trader[inventory][purchase] <= 0 and purchase != 'no':
                print('Desired item is out of stock.')
                print('Buy something else. ')
                purchase = input()

        if purchase == 'no':
            break

#player 2 end of purchasing
        print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
        print(player_2_inventory)
        break

#player 2 can automatically end purchasing for both players if player 1 made initial purchase
    elif category == 'no' and purchase_counter % 2 == 0 and first % 2 == 1:
        break

#player 2 stops purchasing items and player 2 made first purchase
    elif category == 'no' and purchase_counter % 2 == 0 and first % 2 == 0:
        print(player_list['Player 1']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
        print("\n")
        print(player_list['Player 1']['Character Profile']['Name'] + ' please purchase your last item. ')
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
        print(player_1_inventory)

        print('What type of item would you like to buy?')
        category = input()

        if category == 'no':
            break

        elif category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
            while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                print('Invalid input. Please try again. ')
                category = input()
                print("\n")

        if category == 'no':
            break
        
        elif category == 'Weapons':
            print(trader['Weapons Inventory'])
        elif category == 'Armor':
            print(trader['Armor Inventory'])
        elif category == 'Healing Items':
            print(trader['Healing Items Inventory'])

        print('Make your selection.')
        purchase = input()
        inventory = category + ' Inventory'

        if purchase == 'no':
            break

        if purchase not in trader[inventory].keys() and purchase != 'no':
            while purchase not in trader[inventory].keys() and purchase != 'no':
                print('Invalid purchase.')
                purchase = input()

        if purchase == 'no':
            break

#player 1 purchases one last item
        cost = trader[category][purchase][0]

#cost adjustments to reflect charisma
        if player_list['Player 1']['Character Profile']['Charisma'] < 20:
            cost = int(cost * 1.1)
        elif player_list['Player 1']['Character Profile']['Charisma'] > 80:
            cost = int(cost * 0.9)

#player 1 successfully purchases an item
        if player_list['Player 1']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
            player_1_inventory.append(purchase)
            player_list['Player 1']['Secondary Stats']['Gold'] -= cost
            trader[inventory][purchase] -= 1

#failed purchase due to insufficient funds
        elif player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
            while player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                print('You don\'t have enough money for that! ')
                print('Buy something you can afford. ')
                purchase = input()
        
        if purchase == 'no':
            break

#failed purchase due to lack of inventory
        elif trader[inventory][purchase] <= 0 and purchase != 'no':
            while trader[inventory][purchase] <= 0 and purchase != 'no':
                print('Desired item is out of stock.')
                print('Buy something else. ')
                purchase = input()

        if purchase == 'no':
            break

#player 1 end of purchasing
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
        print(player_1_inventory)
        break

#player 1 can automatically end purchasing for both players if player 2 made initial purchase
    elif category == 'no' and purchase_counter % 2 == 1 and first % 2 == 0:
        break

#player 1 or player 2 go through with purchase
    else:
        if category == 'Weapons':
            print('Weapon stats as (price, attack damage, speed): ')
            print(trader['Weapons'])
            print(trader['Weapons Inventory'])
        elif category == 'Armor':
            print('Armor stats as (price, armor): ')
            print(trader['Armor'])
            print(trader['Armor Inventory'])
        elif category == 'Healing Items':
            print('Healing item stats as (price, amount of health/mana restored): ')
            print(trader['Healing Items'])
            print(trader['Healing Items Inventory'])

#accessing specific item from selected category
        print('Make your selection.')
        purchase = input()
        print("\n")
        inventory = category + ' Inventory'

#validate user selections against possible values
        if purchase == 'no' or purchase not in trader[inventory].keys():
            if purchase not in trader[inventory].keys() and purchase != 'no':
                while purchase not in trader[inventory].keys() and purchase != 'no':
                    print('Invalid Input')
                    purchase = input()

            elif purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 1:
                print(player_list['Player 2']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                print("\n")
                print(player_list['Player 2']['Character Profile']['Name'] + ' please purchase your last item. ')
                print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                print(player_2_inventory)

                print('What type of item would you like to buy?')
                category = input()

                if category == 'no':
                    break

                if category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                    while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        print('Invalid input. Please try again. ')
                        category = input()
                        print("\n")
        
                if category == 'no':
                    break

                elif category == 'Weapons':
                    print(trader['Weapons Inventory'])
                elif category == 'Armor':
                    print(trader['Armor Inventory'])
                elif category == 'Healing Items':
                    print(trader['Healing Items Inventory'])

                print('Make your selection.')
                purchase = input()
                inventory = category + ' Inventory'

                if purchase == 'no':
                    break

                if purchase not in trader[inventory].keys() and purchase != 'no':
                    while purchase not in trader[inventory].keys() and purchase != 'no':
                        print('Invalid purchase.')
                        purchase = input()

                if purchase == 'no':
                    break

                cost = trader[category][purchase][0]

                if player_list['Player 2']['Character Profile']['Charisma'] < 20:
                    cost = int(cost * 1.1)
                elif player_list['Player 2']['Character Profile']['Charisma'] > 80:
                    cost = int(cost * 0.9)

                if player_list['Player 2']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                    player_2_inventory.append(purchase)
                    player_list['Player 2']['Secondary Stats']['Gold'] -= cost
                    trader[inventory][purchase] -= 1

                elif player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                    while player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        print('You don\'t have enough money for that! ')
                        print('Buy something you can afford. ')
                        purchase = input()

                if purchase == 'no':
                    break

                elif trader[inventory][purchase] <= 0 and purchase != 'no':
                    while trader[inventory][purchase] <= 0 and purchase != 'no':
                        print('Desired item is out of stock.')
                        print('Buy something else. ')
                        purchase = input()

                if purchase == 'no':
                    break

                print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                print(player_2_inventory)
                break

            elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 1:
                break

            elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 0:
                print(player_list['Player 1']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                print("\n")
                print(player_list['Player 1']['Character Profile']['Name'] + ' please purchase your last item. ')
                print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                print(player_1_inventory)

                print('What type of item would you like to buy?')
                category = input()

                if category == 'no':
                    break

                elif category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                    while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        print('Invalid input. Please try again. ')
                        category = input()
                        print("\n")

                if category == 'no':
                    break
        
                elif category == 'Weapons':
                    print(trader['Weapons Inventory'])
                elif category == 'Armor':
                    print(trader['Armor Inventory'])
                elif category == 'Healing Items':
                    print(trader['Healing Items Inventory'])

                print('Make your selection.')
                purchase = input()
                inventory = category + ' Inventory'

                if purchase == 'no':
                    break

                if purchase not in trader[inventory].keys() and purchase != 'no':
                    while purchase not in trader[inventory].keys() and purchase != 'no':
                        print('Invalid purchase.')
                        purchase = input()

                if purchase == 'no':
                    break

                cost = trader[category][purchase][0]

                if player_list['Player 1']['Character Profile']['Charisma'] < 20:
                    cost = int(cost * 1.1)
                elif player_list['Player 1']['Character Profile']['Charisma'] > 80:
                    cost = int(cost * 0.9)

                if player_list['Player 1']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                    player_1_inventory.append(purchase)
                    player_list['Player 1']['Secondary Stats']['Gold'] -= cost
                    trader[inventory][purchase] -= 1

                elif player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                    while player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        print('You don\'t have enough money for that! ')
                        print('Buy something you can afford. ')
                        purchase = input()
        
                if purchase == 'no':
                    break

                elif trader[inventory][purchase] <= 0 and purchase != 'no':
                    while trader[inventory][purchase] <= 0 and purchase != 'no':
                        print('Desired item is out of stock.')
                        print('Buy something else. ')
                        purchase = input()

                if purchase == 'no':
                    break

                print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                print(player_1_inventory)
                break

            elif purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 0:
                break
            
        elif purchase in trader[inventory].keys():
            cost = trader[category][purchase][0]

#player 1 specific purchases
        if purchase_counter % 2 == 1:
            print(player_1_inventory)

            if player_list['Player 1']['Character Profile']['Charisma'] < 20:
                cost = int(cost * 1.1)
            elif player_list['Player 1']['Character Profile']['Charisma'] > 80:
                cost = int(cost * 0.9)

            if player_list['Player 1']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                player_1_inventory.append(purchase)
                player_list['Player 1']['Secondary Stats']['Gold'] -= cost
                trader[inventory][purchase] -= 1

            elif player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                while player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                    print('You don\'t have enough money for that! ')
                    print('Buy something you can afford. ')
                    purchase = input()

                if purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 1:
                    print(player_list['Player 2']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                    print("\n")
                    print(player_list['Player 2']['Character Profile']['Name'] + ' please purchase your last item. ')
                    print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_2_inventory)

                    print('What type of item would you like to buy?')
                    category = input()

                    if category == 'no':
                        break

                    if category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                            print('Invalid input. Please try again. ')
                            category = input()
                            print("\n")
        
                    if category == 'no':
                        break

                    elif category == 'Weapons':
                        print(trader['Weapons Inventory'])
                    elif category == 'Armor':
                        print(trader['Armor Inventory'])
                    elif category == 'Healing Items':
                        print(trader['Healing Items Inventory'])

                    print('Make your selection.')
                    purchase = input()
                    inventory = category + ' Inventory'

                    if purchase == 'no':
                        break

                    if purchase not in trader[inventory].keys() and purchase != 'no':
                        while purchase not in trader[inventory].keys() and purchase != 'no':
                            print('Invalid purchase.')
                            purchase = input()

                    if purchase == 'no':
                        break

                    cost = trader[category][purchase][0]

                    if player_list['Player 2']['Character Profile']['Charisma'] < 20:
                        cost = int(cost * 1.1)
                    elif player_list['Player 2']['Character Profile']['Charisma'] > 80:
                        cost = int(cost * 0.9)

                    if player_list['Player 2']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                        player_2_inventory.append(purchase)
                        player_list['Player 2']['Secondary Stats']['Gold'] -= cost
                        trader[inventory][purchase] -= 1

                    elif player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        while player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                            print('You don\'t have enough money for that! ')
                            print('Buy something you can afford. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    elif trader[inventory][purchase] <= 0 and purchase != 'no':
                        while trader[inventory][purchase] <= 0 and purchase != 'no':
                            print('Desired item is out of stock.')
                            print('Buy something else. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_2_inventory)
                    break

                elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 1:
                    break

                elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 0:
                    print(player_list['Player 1']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                    print("\n")
                    print(player_list['Player 1']['Character Profile']['Name'] + ' please purchase your last item. ')
                    print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_1_inventory)

                    print('What type of item would you like to buy?')
                    category = input()

                    if category == 'no':
                        break

                    elif category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                            print('Invalid input. Please try again. ')
                            category = input()
                            print("\n")

                    if category == 'no':
                        break
        
                    elif category == 'Weapons':
                        print(trader['Weapons Inventory'])
                    elif category == 'Armor':
                        print(trader['Armor Inventory'])
                    elif category == 'Healing Items':
                        print(trader['Healing Items Inventory'])

                    print('Make your selection.')
                    purchase = input()
                    inventory = category + ' Inventory'

                    if purchase == 'no':
                        break

                    if purchase not in trader[inventory].keys() and purchase != 'no':
                        while purchase not in trader[inventory].keys() and purchase != 'no':
                            print('Invalid purchase.')
                            purchase = input()

                    if purchase == 'no':
                        break

                    cost = trader[category][purchase][0]

                    if player_list['Player 1']['Character Profile']['Charisma'] < 20:
                        cost = int(cost * 1.1)
                    elif player_list['Player 1']['Character Profile']['Charisma'] > 80:
                        cost = int(cost * 0.9)

                    if player_list['Player 1']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                        player_1_inventory.append(purchase)
                        player_list['Player 1']['Secondary Stats']['Gold'] -= cost
                        trader[inventory][purchase] -= 1

                    elif player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        while player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                            print('You don\'t have enough money for that! ')
                            print('Buy something you can afford. ')
                            purchase = input()
        
                    if purchase == 'no':
                        break

                    elif trader[inventory][purchase] <= 0 and purchase != 'no':
                        while trader[inventory][purchase] <= 0 and purchase != 'no':
                            print('Desired item is out of stock.')
                            print('Buy something else. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_1_inventory)
                    break

                elif purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 0:
                    break
                
            elif trader[inventory][purchase] <= 0 and purchase != 'no':
                while trader[inventory][purchase] <= 0 and purchase != 'no':
                    print('Desired item is out of stock.')
                    print('Buy something else. ')
                    purchase = input()

                if purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 1:
                    print(player_list['Player 2']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                    print("\n")
                    print(player_list['Player 2']['Character Profile']['Name'] + ' please purchase your last item. ')
                    print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_2_inventory)

                    print('What type of item would you like to buy?')
                    category = input()

                    if category == 'no':
                        break

                    if category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                            print('Invalid input. Please try again. ')
                            category = input()
                            print("\n")
        
                    if category == 'no':
                        break

                    elif category == 'Weapons':
                        print(trader['Weapons Inventory'])
                    elif category == 'Armor':
                        print(trader['Armor Inventory'])
                    elif category == 'Healing Items':
                        print(trader['Healing Items Inventory'])

                    print('Make your selection.')
                    purchase = input()
                    inventory = category + ' Inventory'

                    if purchase == 'no':
                        break

                    if purchase not in trader[inventory].keys() and purchase != 'no':
                        while purchase not in trader[inventory].keys() and purchase != 'no':
                            print('Invalid purchase.')
                            purchase = input()

                    if purchase == 'no':
                        break

                    cost = trader[category][purchase][0]

                    if player_list['Player 2']['Character Profile']['Charisma'] < 20:
                        cost = int(cost * 1.1)
                    elif player_list['Player 2']['Character Profile']['Charisma'] > 80:
                        cost = int(cost * 0.9)

                    if player_list['Player 2']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                        player_2_inventory.append(purchase)
                        player_list['Player 2']['Secondary Stats']['Gold'] -= cost
                        trader[inventory][purchase] -= 1

                    elif player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        while player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                            print('You don\'t have enough money for that! ')
                            print('Buy something you can afford. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    elif trader[inventory][purchase] <= 0 and purchase != 'no':
                        while trader[inventory][purchase] <= 0 and purchase != 'no':
                            print('Desired item is out of stock.')
                            print('Buy something else. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_2_inventory)
                    break

                elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 1:
                    break

                elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 0:
                    print(player_list['Player 1']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                    print("\n")
                    print(player_list['Player 1']['Character Profile']['Name'] + ' please purchase your last item. ')
                    print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_1_inventory)

                    print('What type of item would you like to buy?')
                    category = input()

                    if category == 'no':
                        break

                    elif category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                            print('Invalid input. Please try again. ')
                            category = input()
                            print("\n")

                    if category == 'no':
                        break
        
                    elif category == 'Weapons':
                        print(trader['Weapons Inventory'])
                    elif category == 'Armor':
                        print(trader['Armor Inventory'])
                    elif category == 'Healing Items':
                        print(trader['Healing Items Inventory'])

                    print('Make your selection.')
                    purchase = input()
                    inventory = category + ' Inventory'

                    if purchase == 'no':
                        break

                    if purchase not in trader[inventory].keys() and purchase != 'no':
                        while purchase not in trader[inventory].keys() and purchase != 'no':
                            print('Invalid purchase.')
                            purchase = input()

                    if purchase == 'no':
                        break

                    cost = trader[category][purchase][0]

                    if player_list['Player 1']['Character Profile']['Charisma'] < 20:
                        cost = int(cost * 1.1)
                    elif player_list['Player 1']['Character Profile']['Charisma'] > 80:
                        cost = int(cost * 0.9)

                    if player_list['Player 1']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                        player_1_inventory.append(purchase)
                        player_list['Player 1']['Secondary Stats']['Gold'] -= cost
                        trader[inventory][purchase] -= 1

                    elif player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        while player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                            print('You don\'t have enough money for that! ')
                            print('Buy something you can afford. ')
                            purchase = input()
        
                    if purchase == 'no':
                        break

                    elif trader[inventory][purchase] <= 0 and purchase != 'no':
                        while trader[inventory][purchase] <= 0 and purchase != 'no':
                            print('Desired item is out of stock.')
                            print('Buy something else. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_1_inventory)
                    break

                elif purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 0:
                    break

#display player inventory after purchase
            print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
            print(player_1_inventory)

#player 2 specific purchases
        elif purchase_counter % 2 == 0:
            print(player_2_inventory)

            if player_list['Player 2']['Character Profile']['Charisma'] < 20:
                cost = int(cost * 1.1)
            elif player_list['Player 2']['Character Profile']['Charisma'] > 80:
                cost = int(cost * 0.9)

            if player_list['Player 2']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                player_2_inventory.append(purchase)
                player_list['Player 2']['Secondary Stats']['Gold'] -= cost
                trader[inventory][purchase] -= 1

            elif player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                while player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                    print('You don\'t have enough money for that! ')
                    print('Buy something you can afford. ')
                    purchase = input()
                
                if purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 1:
                    print(player_list['Player 2']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                    print("\n")
                    print(player_list['Player 2']['Character Profile']['Name'] + ' please purchase your last item. ')
                    print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_2_inventory)

                    print('What type of item would you like to buy?')
                    category = input()

                    if category == 'no':
                        break

                    if category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                            print('Invalid input. Please try again. ')
                            category = input()
                            print("\n")
        
                    if category == 'no':
                        break

                    elif category == 'Weapons':
                        print(trader['Weapons Inventory'])
                    elif category == 'Armor':
                        print(trader['Armor Inventory'])
                    elif category == 'Healing Items':
                        print(trader['Healing Items Inventory'])

                    print('Make your selection.')
                    purchase = input()
                    inventory = category + ' Inventory'

                    if purchase == 'no':
                        break

                    if purchase not in trader[inventory].keys() and purchase != 'no':
                        while purchase not in trader[inventory].keys() and purchase != 'no':
                            print('Invalid purchase.')
                            purchase = input()

                    if purchase == 'no':
                        break

                    cost = trader[category][purchase][0]

                    if player_list['Player 2']['Character Profile']['Charisma'] < 20:
                        cost = int(cost * 1.1)
                    elif player_list['Player 2']['Character Profile']['Charisma'] > 80:
                        cost = int(cost * 0.9)

                    if player_list['Player 2']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                        player_2_inventory.append(purchase)
                        player_list['Player 2']['Secondary Stats']['Gold'] -= cost
                        trader[inventory][purchase] -= 1

                    elif player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        while player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                            print('You don\'t have enough money for that! ')
                            print('Buy something you can afford. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    elif trader[inventory][purchase] <= 0 and purchase != 'no':
                        while trader[inventory][purchase] <= 0 and purchase != 'no':
                            print('Desired item is out of stock.')
                            print('Buy something else. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_2_inventory)
                    break

                elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 1:
                    break

                elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 0:
                    print(player_list['Player 1']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                    print("\n")
                    print(player_list['Player 1']['Character Profile']['Name'] + ' please purchase your last item. ')
                    print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_1_inventory)

                    print('What type of item would you like to buy?')
                    category = input()

                    if category == 'no':
                        break

                    elif category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                            print('Invalid input. Please try again. ')
                            category = input()
                            print("\n")

                    if category == 'no':
                        break
        
                    elif category == 'Weapons':
                        print(trader['Weapons Inventory'])
                    elif category == 'Armor':
                        print(trader['Armor Inventory'])
                    elif category == 'Healing Items':
                        print(trader['Healing Items Inventory'])

                    print('Make your selection.')
                    purchase = input()
                    inventory = category + ' Inventory'

                    if purchase == 'no':
                        break

                    if purchase not in trader[inventory].keys() and purchase != 'no':
                        while purchase not in trader[inventory].keys() and purchase != 'no':
                            print('Invalid purchase.')
                            purchase = input()

                    if purchase == 'no':
                        break

                    cost = trader[category][purchase][0]

                    if player_list['Player 1']['Character Profile']['Charisma'] < 20:
                        cost = int(cost * 1.1)
                    elif player_list['Player 1']['Character Profile']['Charisma'] > 80:
                        cost = int(cost * 0.9)

                    if player_list['Player 1']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                        player_1_inventory.append(purchase)
                        player_list['Player 1']['Secondary Stats']['Gold'] -= cost
                        trader[inventory][purchase] -= 1

                    elif player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        while player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                            print('You don\'t have enough money for that! ')
                            print('Buy something you can afford. ')
                            purchase = input()
        
                    if purchase == 'no':
                        break

                    elif trader[inventory][purchase] <= 0 and purchase != 'no':
                        while trader[inventory][purchase] <= 0 and purchase != 'no':
                            print('Desired item is out of stock.')
                            print('Buy something else. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_1_inventory)
                    break

                elif purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 0:
                    break

            elif trader[inventory][purchase] <= 0 and purchase != 'no':
                while trader[inventory][purchase] <= 0 and purchase != 'no':
                    print('Desired item is out of stock.')
                    print('Buy something else. ')
                    purchase = input()
            
                if purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 1:
                    print(player_list['Player 2']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                    print("\n")
                    print(player_list['Player 2']['Character Profile']['Name'] + ' please purchase your last item. ')
                    print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_2_inventory)

                    print('What type of item would you like to buy?')
                    category = input()

                    if category == 'no':
                        break

                    if category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                            print('Invalid input. Please try again. ')
                            category = input()
                            print("\n")
        
                    if category == 'no':
                        break

                    elif category == 'Weapons':
                        print(trader['Weapons Inventory'])
                    elif category == 'Armor':
                        print(trader['Armor Inventory'])
                    elif category == 'Healing Items':
                        print(trader['Healing Items Inventory'])

                    print('Make your selection.')
                    purchase = input()
                    inventory = category + ' Inventory'

                    if purchase == 'no':
                        break

                    if purchase not in trader[inventory].keys() and purchase != 'no':
                        while purchase not in trader[inventory].keys() and purchase != 'no':
                            print('Invalid purchase.')
                            purchase = input()

                    if purchase == 'no':
                        break

                    cost = trader[category][purchase][0]

                    if player_list['Player 2']['Character Profile']['Charisma'] < 20:
                        cost = int(cost * 1.1)
                    elif player_list['Player 2']['Character Profile']['Charisma'] > 80:
                        cost = int(cost * 0.9)

                    if player_list['Player 2']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                        player_2_inventory.append(purchase)
                        player_list['Player 2']['Secondary Stats']['Gold'] -= cost
                        trader[inventory][purchase] -= 1

                    elif player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        while player_list['Player 2']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                            print('You don\'t have enough money for that! ')
                            print('Buy something you can afford. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    elif trader[inventory][purchase] <= 0 and purchase != 'no':
                        while trader[inventory][purchase] <= 0 and purchase != 'no':
                            print('Desired item is out of stock.')
                            print('Buy something else. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_2_inventory)
                    break

                elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 1:
                    break

                elif purchase == 'no' and purchase_counter % 2 == 0 and first % 2 == 0:
                    print(player_list['Player 1']['Character Profile']['Name'] + ' has 1 more turn to purchase.')
                    print("\n")
                    print(player_list['Player 1']['Character Profile']['Name'] + ' please purchase your last item. ')
                    print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_1_inventory)

                    print('What type of item would you like to buy?')
                    category = input()

                    if category == 'no':
                        break

                    elif category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                        while category not in ['Weapons', 'Armor', 'Healing Items'] and category != 'no':
                            print('Invalid input. Please try again. ')
                            category = input()
                            print("\n")

                    if category == 'no':
                        break
        
                    elif category == 'Weapons':
                        print(trader['Weapons Inventory'])
                    elif category == 'Armor':
                        print(trader['Armor Inventory'])
                    elif category == 'Healing Items':
                        print(trader['Healing Items Inventory'])

                    print('Make your selection.')
                    purchase = input()
                    inventory = category + ' Inventory'

                    if purchase == 'no':
                        break

                    if purchase not in trader[inventory].keys() and purchase != 'no':
                        while purchase not in trader[inventory].keys() and purchase != 'no':
                            print('Invalid purchase.')
                            purchase = input()

                    if purchase == 'no':
                        break

                    cost = trader[category][purchase][0]

                    if player_list['Player 1']['Character Profile']['Charisma'] < 20:
                        cost = int(cost * 1.1)
                    elif player_list['Player 1']['Character Profile']['Charisma'] > 80:
                        cost = int(cost * 0.9)

                    if player_list['Player 1']['Secondary Stats']['Gold'] >  cost and trader[inventory][purchase] > 0:
                        player_1_inventory.append(purchase)
                        player_list['Player 1']['Secondary Stats']['Gold'] -= cost
                        trader[inventory][purchase] -= 1

                    elif player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                        while player_list['Player 1']['Secondary Stats']['Gold'] < cost and purchase != 'no':
                            print('You don\'t have enough money for that! ')
                            print('Buy something you can afford. ')
                            purchase = input()
        
                    if purchase == 'no':
                        break

                    elif trader[inventory][purchase] <= 0 and purchase != 'no':
                        while trader[inventory][purchase] <= 0 and purchase != 'no':
                            print('Desired item is out of stock.')
                            print('Buy something else. ')
                            purchase = input()

                    if purchase == 'no':
                        break

                    print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
                    print(player_1_inventory)
                    break

                elif purchase == 'no' and purchase_counter % 2 == 1 and first % 2 == 0:
                    break

            print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
            print(player_2_inventory)
            
#regardless of player
#start of next purchasing cycle
#display available items
    print("\n")
    for item_type in ['Weapons', 'Armor', 'Healing Items']:
        print('Available ' + item_type + ': ')
        inventory = item_type + ' Inventory'
        print(trader[inventory])
        print("\n")
        print(item_type + ' stats: ')
        if item_type == 'Weapons':
            print('Weapon stats displayed as (price, attack damage, speed)')
        elif item_type == 'Armor':
            print('Armor stats displayed as (price, armor)')
        elif item_type == 'Healing Items':
            print('Healing Item stats displayed as (price, amount of health/mana restored)')
        print(trader[item_type])
        print("\n")

#check if there is available inventory
    test_value = 0
    no_weapons = True
    for key in trader['Weapons Inventory']:
        if trader['Weapons Inventory'][key] != test_value:
            no_weapons = False
            break
    no_armor = True
    for key in trader['Armor Inventory']:
        if trader['Armor Inventory'][key] != test_value:
            no_armor = False
            break
    no_healing = True
    for key in trader['Healing Items Inventory']:
        if trader['Healing Items Inventory'][key] != test_value:
            no_healing = False
            break
    if no_weapons == True and no_armor == True and no_healing == True:
        print('All items out of stock!')
        break

#switch players and prompt corresponding player to make purchase
    purchase_counter += 1
    if purchase_counter % 2 == 0:
        print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
        print(player_2_inventory)
        purchase_prompt = player_list['Player 2']['Character Profile']['Name'] + ' please select a type of item to purchase. '
        gold = 'Available gold: ' + str(player_list['Player 2']['Secondary Stats']['Gold'])
    elif purchase_counter % 2 == 1:
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
        print(player_1_inventory)
        purchase_prompt = player_list['Player 1']['Character Profile']['Name'] + ' please select a type of item to purchase. '
        gold = 'Available gold: ' + str(player_list['Player 1']['Secondary Stats']['Gold'])
    print("\n")
    print(gold)
    print(purchase_prompt)
    category = input()
    print("\n")  

#convert player inventories from lists to dictionaries and assign to inventory section of player list
temp_inventory_1 = dict.fromkeys(player_1_inventory)
temp_inventory_2 = dict.fromkeys(player_2_inventory)

for key in temp_inventory_1:
    if key in trader['Weapons Inventory'].keys():
        temp_inventory_1[key] = trader['Weapons Inventory'][key]
    elif key in trader['Armor Inventory'].keys():
        temp_inventory_1[key] = trader['Armor Inventory'][key]
    elif key in trader['Healing Items Inventory'].keys():
        temp_inventory_1[key] = trader['Healing Items Inventory'][key]
player_list['Player 1']['Inventory'] = temp_inventory_1

for key in temp_inventory_2:
    if key in trader['Weapons Inventory'].keys():
        temp_inventory_2[key] = trader['Weapons Inventory'][key]
    elif key in trader['Armor Inventory'].keys():
        temp_inventory_2[key] = trader['Armor Inventory'][key]
    elif key in trader['Healing Items Inventory'].keys():
        temp_inventory_2[key] = trader['Healing Items Inventory'][key]
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
print('Character intellect affects mana costs and effectiveness of healing items.')
print("\n")
for i in [1,2]:
    player_number = 'Player ' + str(i)
    Combat_Stats = {'hits':0,'misses':0,'damage taken':0,'health update':""}
    player_list[player_number]['Combat Stats'] = Combat_Stats

#Starting Combat
turn_counter = random.randint(1,2)
while True:

#convert player inventories into a combat inventory without item prices
    player_1_combat_inventory = dict.fromkeys(player_list['Player 1']['Inventory'].keys())
    player_2_combat_inventory = dict.fromkeys(player_list['Player 2']['Inventory'].keys())
    

    for key in player_list['Player 1']['Inventory']:
        if key in trader['Weapons Inventory'].keys(): 
            player_1_combat_inventory[key] = (trader['Weapons'][key][1], trader['Weapons'][key][2])
        elif key in trader['Armor Inventory'].keys():
            player_1_combat_inventory[key] = trader['Armor'][key][1]
        elif key in trader['Healing Items Inventory'].keys():
            player_1_combat_inventory[key] = trader['Healing Items'][key][1]

    for key in player_list['Player 2']['Inventory']:
        if key in trader['Weapons Inventory'].keys(): 
            player_2_combat_inventory[key] = (trader['Weapons'][key][1], trader['Weapons'][key][2])
        elif key in trader['Armor Inventory'].keys():
            player_2_combat_inventory[key] = trader['Armor'][key][1]
        elif key in trader['Healing Items Inventory'].keys():
            player_2_combat_inventory[key] = trader['Healing Items'][key][1]  

#Player 1 turn
    if turn_counter % 2 == 1:

#replenishing mana on turns after the first turn
        if turn_counter != 1 and turn_counter != 3:
            player_list['Player 1']['Secondary Stats']['Mana'] += 3

#display player 1 stats at beginning of turn
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s stats')
        for i in ['Health','Mana','Armor']:
            print(i + ': ' + str(player_list['Player 1']['Secondary Stats'][i]))
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s combat stats')
        for key in player_list['Player 1']['Combat Stats']:
            print(key + ': ' + str(player_list['Player 1']['Combat Stats'][key]))
        print("\n")

#prompt player 1 to equip an item for the turn
        print(player_list['Player 1']['Character Profile']['Name'] + ' please equip an item from your inventory. (type none for default weapon)')
        print('Weapon stats displayed as "name" : (damage, speed).')
        print('Armor stats displayed as "name" : armor')
        print('Healing item stats displayed as "name" : amount of health/mana restored')
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s inventory:')
        print(player_1_combat_inventory)
        equip = input()
        if equip not in player_1_combat_inventory or equip == 'none':
            equipped_name = 'Fist'
            equipped = (2, 'regular')
        else:
            equipped_name = equip
            equipped = player_1_combat_inventory[equip]
        print('Equipped item: ')
        print(equipped_name)
        print(equipped)
        print("\n")

#if a weapon is selected
        if equipped_name in trader['Weapons Inventory'].keys() or equipped_name == 'Fist':

#automatic miss if no mana
            if player_list['Player 1']['Secondary Stats']['Mana'] <= 0:
                print(player_list['Player 1']['Characater Profile']['Name'] + ' missed!')
                player_list['Player 1']['Combat Stats']['misses'] += 1   
                
            else:
#adjustments for player stats
#dexterity affects hit chance
                if player_list['Player 1']['Character Profile']['Dexterity'] < 30:
                    hit_chance = random.randint(-5,1)
                elif player_list['Player 1']['Character Profile']['Dexterity'] > 70:
                    hit_chance = random.randint(-1,5)
                else:
                    hit_chance = random.randint(-3,3)

#intellect affects mana costs
                if player_list['Player 1']['Character Profile']['Intellect'] < 30:
                    mana_cost = 15
                elif player_list['Player 1']['Character Profile']['Intellect'] > 70:
                    mana_cost = 5
                else:
                    mana_cost = 10

#strength affects attack damage
                damage_dealt = equipped[0]
                if player_list['Player 1']['Character Profile']['Strength'] < 15:
                    damage_dealt = int(damage_dealt * 0.8)
                elif player_list['Player 1']['Character Profile']['Strength'] > 85:
                    damage_dealt = int(damage_dealt * 1.2)

#weapon speed affects attack damage, player health, and mana costs
                if equipped[1] == 'Slow':
                    damage_dealt += 5
                    player_list['Player 1']['Secondary Stats']['Health'] -= 2
                    mana_cost = int(mana_cost * 1.05)
                elif equipped[1] == 'Fast':
                    damage_dealt -= 2
                    mana_cost = int(mana_cost * 0.95)

#successful hit
                if hit_chance >= 0:
                    print(player_list['Player 1']['Character Profile']['Name'] + '\'s attack hit!')

#adjustments for opponent armor
#if armor is equipped, damage is split 40% to opponent health and 60% to opponent armor
                    if player_list['Player 2']['Secondary Stats']['Armor'] > 0:
                        player_list['Player 2']['Secondary Stats']['Health'] -= int(damage_dealt * 0.4)
                        player_list['Player 2']['Secondary Stats']['Armor'] -= int(damage_dealt * 0.6)
                        player_list['Player 2']['Combat Stats']['damage taken'] = int(damage_dealt * 0.4)
                    else:
                        player_list['Player 2']['Secondary Stats']['Health'] -= damage_dealt
                        player_list['Player 2']['Combat Stats']['damage taken'] = damage_dealt
                    player_list['Player 1']['Secondary Stats']['Mana'] -= mana_cost
                    player_list['Player 1']['Combat Stats']['hits'] += 1

#unsuccessful attack
                else:
                    print(player_list['Player 1']['Character Profile']['Name'] + ' missed!')
                    player_list['Player 1']['Secondary Stats']['Mana'] -= int(mana_cost*0.4)
                    player_list['Player 1']['Combat Stats']['misses'] += 1

#if armor is selected
        elif equipped_name in trader['Armor Inventory'].keys():
            player_list['Player 1']['Secondary Stats']['Armor'] += equipped
            
#if healing items are selected
#player intellect modifies effectiveness of healing items
#steak and bandaids restore health
        elif equipped_name in ['Steak','Band Aid']:
            health_restored = equipped
            if player_list['Player 1']['Character Profile']['Intellect'] > 90:
                health_restored = int(health_restored * 1.1)
            elif player_list['Player 1']['Character Profile']['Intellect'] < 10:
                health_restored = int(health_restored * 0.9)
            player_list['Player 1']['Secondary Stats']['Health'] += health_restored

#vinegar restores mana
        elif equipped_name == 'Vinegar':
            mana_restored = equipped
            if player_list['Player 1']['Character Profile']['Intellect'] > 90:
                mana_restored = int(health_restored * 1.1)
            elif player_list['Player 1']['Character Profile']['Intellect'] < 10:
                mana_restored = int(health_restored * 0.9)
            player_list['Player 1']['Secondary Stats']['Mana'] += mana_restored
            
#end of player 1's turn
        print('End of ' + player_list['Player 1']['Character Profile']['Name'] + '\'s turn.')

#display player stats at end of turn
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s stats')
        for i in ['Health','Mana','Armor']:
            print(i + ': ' + str(player_list['Player 1']['Secondary Stats'][i]))
        print(player_list['Player 1']['Character Profile']['Name'] + '\'s combat stats')
        player_list['Player 1']['Combat Stats']['health update'] = player_list['Player 1']['Secondary Stats']['Health']
        for key in player_list['Player 1']['Combat Stats']:
            print(key + ': ' + str(player_list['Player 1']['Combat Stats'][key]))
        print("\n")

#player 1 wins if player 2's health is less than or equal to 0
        if player_list['Player 2']['Secondary Stats']['Health'] <= 0:
            print(player_list['Player 1']['Character Profile']['Name'] + ' the ' + player_list['Player 1']['Character Profile']['Description'] + ' ' + player_list['Player 1']['Character Profile']['Sex'] + ' ' + player_list['Player 1']['Character Profile']['Race'] + ' won the battle!')
            break

#switch to other player's turn
        turn_counter += 1

#Player 2 turn
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
        print('Armor stats displayed as "name" : armor')
        print('Healing item stats displayed as "name" : amount of health/mana restored')
        print(player_list['Player 2']['Character Profile']['Name'] + '\'s inventory:')
        print(player_2_combat_inventory)
        equip = input()
        if equip not in player_2_combat_inventory or equip == 'none':
            equipped_name = 'Fist'
            equipped = (2, 'regular')
        else:
            equipped_name = equip
            equipped = player_2_combat_inventory[equip]

        if equipped_name in trader['Weapons Inventory'].keys() or equipped_name == 'Fist':
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

                if equipped[1] == 'Slow':
                    damage_dealt += 5
                    player_list['Player 2']['Secondary Stats']['Health'] -= 2
                    mana_cost = int(mana_cost * 1.05)
                elif equipped[1] == 'Fast':
                    damage_dealt -= 2
                    mana_cost = int(mana_cost * 0.95)

                if hit_chance >= 0:
                    print(player_list['Player 2']['Character Profile']['Name'] + '\'s attack hit!')
                    if player_list['Player 1']['Secondary Stats']['Armor'] > 0:
                        player_list['Player 1']['Secondary Stats']['Health'] -= int(damage_dealt * 0.4)
                        player_list['Player 1']['Secondary Stats']['Armor'] -= int(damage_dealt * 0.6)
                        player_list['Player 1']['Combat Stats']['damage taken'] = int(damage_dealt * 0.4)
                    else:
                        player_list['Player 1']['Secondary Stats']['Health'] -= damage_dealt
                        player_list['Player 1']['Combat Stats']['damage taken'] = damage_dealt
                    player_list['Player 2']['Secondary Stats']['Mana'] -= mana_cost
                    player_list['Player 2']['Combat Stats']['hits'] += 1

                else:
                    print(player_list['Player 2']['Character Profile']['Name'] + ' missed!')
                    player_list['Player 2']['Secondary Stats']['Mana'] -= int(mana_cost*0.4)
                    player_list['Player 2']['Combat Stats']['misses'] += 1

        elif equipped_name in trader['Armor Inventory'].keys():
            player_list['Player 2']['Secondary Stats']['Armor'] += equipped
            player_2_combat_inventory[equipped_name] -= 1

        elif equipped_name in ['Steak','Band Aid']:
            health_restored = equipped
            if player_list['Player 2']['Character Profile']['Intellect'] > 90:
                health_restored = int(health_restored * 1.1)
            elif player_list['Player 2']['Character Profile']['Intellect'] < 10:
                health_restored = int(health_restored * 0.9)
            player_list['Player 2']['Secondary Stats']['Health'] += health_restored
            player_2_combat_inventory[equipped_name] -= 1

        elif equipped_name == 'Vinegar':
            mana_restored = equipped
            if player_list['Player 2']['Character Profile']['Intellect'] > 90:
                mana_restored = int(health_restored * 1.1)
            elif player_list['Player 2']['Character Profile']['Intellect'] < 10:
                mana_restored = int(health_restored * 0.9)
            player_list['Player 2']['Secondary Stats']['Mana'] += mana_restored
            
        print('End of ' + player_list['Player 2']['Character Profile']['Name'] + '\'s turn.')

        print(player_list['Player 2']['Character Profile']['Name'] + '\'s stats')
        for i in ['Health','Mana','Armor']:
            print(i + ': ' + str(player_list['Player 2']['Secondary Stats'][i]))
        print(player_list['Player 2']['Character Profile']['Name'] + '\'s combat stats')
        player_list['Player 2']['Combat Stats']['health update'] = player_list['Player 2']['Secondary Stats']['Health']
        for key in player_list['Player 2']['Combat Stats']:
            print(key + ': ' + str(player_list['Player 2']['Combat Stats'][key]))
        print("\n")

        if player_list['Player 1']['Secondary Stats']['Health'] <= 0:
            print(player_list['Player 2']['Character Profile']['Name'] + ' the ' + player_list['Player 2']['Character Profile']['Description'] + ' ' + player_list['Player 2']['Character Profile']['Sex'] + ' ' + player_list['Player 2']['Character Profile']['Race'] + ' won the battle!')
            break

        turn_counter += 1

#end of game
print("\n")
print('Thank you for playing!')