#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  
Ask the user for input, and if the item they choose to 'get item', 
add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  
If they choose 'show inventory' give them a list of the items that they have. 
You will need to use the string.split() method to separate the command from the item.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool



example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""
    
INVENTORY = {}

FOOD_COUNT = 0 
WATER_COUNT = 0
ROPE_COUNT = 0
TORCH_COUNT = 0
SACK_COUNT = 0
WOOD_COUNT = 0
IRON_COUNT = 0
STEEL_COUNT = 0
GINGER_COUNT = 0
GARLIC_COUNT = 0
FISH_COUNT = 0
STONE_COUNT = 0
WOOL_COUNT = 0


#Start Menu
def start():

    POSSIBLES = ['food', 'water', 'rope', 'torch', 'sack', 'wood' ,'iron' , 'steel', 'ginger', 'garlic', 'fish', 'stone', 'wool']

    PICK_UP = ''
    AMOUNT = ""


    global FOOD_COUNT
    global WATER_COUNT
    global ROPE_COUNT
    global TORCH_COUNT
    global SACK_COUNT
    global WOOD_COUNT
    global IRON_COUNT
    global STEEL_COUNT
    global GINGER_COUNT
    global GARLIC_COUNT
    global FISH_COUNT
    global STONE_COUNT
    global WOOL_COUNT


#Picking Action 1 and 2
    ACTION = ""
    print("--------------------------------------------------------------------------------------------I")
    print("What would you like to do? : ")
    print("1 to Check Inventory")
    print("2 to Find Something")
    print("3 to Drop Something")

    ACTION = input(" : ")




#Checking
    if ACTION == '1':
        print("--------------------------------------------------------------------------------------------I")
        print(INVENTORY)
        start()


#Picking
    if ACTION == '2': 
        print("--------------------------------------------------------------------------------------------I")
        print("what would you like to pick up?")
        #retry if not an item

#--------------------------------------------------------------------------------------------I
        while PICK_UP not in POSSIBLES:
            PICK_UP = input(" : ")
            if PICK_UP == 'food':
                pass
            elif PICK_UP == 'water':
                pass
            elif PICK_UP == 'rope':
                pass
            elif PICK_UP == 'torch':
                pass
            elif PICK_UP == 'sack':
                pass
            elif PICK_UP == 'wood':
                pass
            elif PICK_UP == 'iron':
                pass
            elif PICK_UP == 'steel':
                pass
            elif PICK_UP == 'ginger':
                pass
            elif PICK_UP == 'garlic':
                pass
            elif PICK_UP == 'fish':
                pass
            elif PICK_UP == 'stone':
                pass
            elif PICK_UP == 'wool':
                pass
                if PICK_UP not in POSSIBLES:
                    print("Invalid Input")
                    print("--------------------------------------------------------------------------------------------I")
        #Invaild Input
            else:
                 print("--------------------------------------------------------------------------------------------I")
                 print("Invaild")
                 print("--------------------------------------------------------------------------------------------I")
#--------------------------------------------------------------------------------------------I
#FOOD      
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'food':
            print("--------------------------------------------------------------------------------------------I")
            print("what much food would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    FOOD_COUNT = AMOUNT + FOOD_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print(" Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: FOOD_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = FOOD_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print(" You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#WATER
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'water':
            print("--------------------------------------------------------------------------------------------I")
            print("what much water would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    WATER_COUNT = AMOUNT + WATER_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: WATER_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = WATER_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#ROPE
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'rope':
            print("--------------------------------------------------------------------------------------------I")
            print("what much rope would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    ROPE_COUNT = AMOUNT + ROPE_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: ROPE_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = ROPE_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#TORCH
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'torch':
            print("--------------------------------------------------------------------------------------------I")
            print("what much torches would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    TORCH_COUNT = AMOUNT + TORCH_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: TORCH_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = TORCH_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#SACK
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'sack':
            print("--------------------------------------------------------------------------------------------I")
            print("what much sack would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    SACK_COUNT = AMOUNT + SACK_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: SACK_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = SACK_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#WOOD     
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'wood':
            print("--------------------------------------------------------------------------------------------I")
            print("what much wood would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    WOOD_COUNT = AMOUNT + WOOD_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: WOOD_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = WOOD_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()   
#--------------------------------------------------------------------------------------------I
#IRON     
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'iron':
            print("--------------------------------------------------------------------------------------------I")
            print("what much iron would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    IRON_COUNT = AMOUNT + IRON_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: IRON_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = IRON_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#STEEL    
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'steel':
            print("--------------------------------------------------------------------------------------------I")
            print("what much steel would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    STEEL_COUNT = AMOUNT + STEEL_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: STEEL_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = STEEL_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#GINGER   
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'ginger':
            print("--------------------------------------------------------------------------------------------I")
            print("what much ginger would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    GINGER_COUNT = AMOUNT + GINGER_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: GINGER_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = GINGER_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#GARLIC     
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'garlic':
            print("--------------------------------------------------------------------------------------------I")
            print("what much garlic would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    GARLIC_COUNT = AMOUNT + GARLIC_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: GARLIC_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = GARLIC_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()      
#--------------------------------------------------------------------------------------------I
#FISH     
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'fish':
            print("--------------------------------------------------------------------------------------------I")
            print("what much fish would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    FISH_COUNT = AMOUNT + FISH_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: FISH_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = FISH_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#STONE      
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'stone':
            print("--------------------------------------------------------------------------------------------I")
            print("what much stone would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    STONE_COUNT = AMOUNT + STONE_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: STONE_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = STONE_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()
#--------------------------------------------------------------------------------------------I
#WOOL     
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'wool':
            print("--------------------------------------------------------------------------------------------I")
            print("what much wool would you like to pick up?")  
            while AMOUNT == '':
                try:
                    AMOUNT = int(input(" : "))
                    WOOL_COUNT = AMOUNT + WOOL_COUNT
                    continue
                except:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invaild")
                    print("--------------------------------------------------------------------------------------------I")


                #Update if in Inventory
                if PICK_UP in INVENTORY:
                        INVENTORY.update({PICK_UP: WOOL_COUNT})
                        
            #Add if not in Inventory
            else:
                INVENTORY[PICK_UP] = WOOL_COUNT

                print("--------------------------------------------------------------------------------------------I")
                print("You found",AMOUNT, PICK_UP + "!")
            start()     
#--------------------------------------------------------------------------------------------I
#DROP
#--------------------------------------------------------------------------------------------I
    if ACTION == '3':
        print("--------------------------------------------------------------------------------------------I")
        print(INVENTORY)
        print("--------------------------------------------------------------------------------------------I")
        print("What would you like to drop?")

        while PICK_UP not in POSSIBLES:
            PICK_UP = input(" : ")
            if PICK_UP == 'food':
                pass
            elif PICK_UP == 'water':
                pass
            elif PICK_UP == 'rope':
                pass
            elif PICK_UP == 'torch':
                pass
            elif PICK_UP == 'sack':
                pass
            elif PICK_UP == 'wood':
                pass
            elif PICK_UP == 'iron':
                pass
            elif PICK_UP == 'steel':
                pass
            elif PICK_UP == 'ginger':
                pass
            elif PICK_UP == 'garlic':
                pass
            elif PICK_UP == 'fish':
                pass
            elif PICK_UP == 'stone':
                pass
            elif PICK_UP == 'wool':
                pass
                if PICK_UP not in POSSIBLES:
                    print("--------------------------------------------------------------------------------------------I")
                    print("Invalid Input")
                    print("--------------------------------------------------------------------------------------------I")
        #Invaild Input
            else:
                 print("--------------------------------------------------------------------------------------------I")
                 print("Invaild")
                 print("--------------------------------------------------------------------------------------------I")
#--------------------------------------------------------------------------------------------I
#FOOD DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'food':
            #check if there if the item
            if FOOD_COUNT == 0 or FOOD_COUNT < 0:
                FOOD_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any food at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much food would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        FOOD_COUNT = FOOD_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: FOOD_COUNT})

                    #If dropping more than have, drop the right amount
                            if FOOD_COUNT < 0:
                                AMOUNT = FOOD_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                FOOD_COUNT = 0
                                INVENTORY.update({PICK_UP: FOOD_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#WATER DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'water':
            #check if there if the item
            if WATER_COUNT == 0 or WATER_COUNT < 0:
                WATER_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any water at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much water would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        WATER_COUNT = WATER_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: WATER_COUNT})

                    #If dropping more than have, drop the right amount
                            if WATER_COUNT < 0:
                                AMOUNT = WATER_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                WATER_COUNT = 0
                                INVENTORY.update({PICK_UP: WATER_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")  
                        
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#ROPE DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'rope':
            #check if there if the item
            if ROPE_COUNT == 0 or ROPE_COUNT < 0:
                ROPE_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any rope at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much rope would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        ROPE_COUNT = ROPE_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: ROPE_COUNT})

                    #If dropping more than have, drop the right amount
                            if ROPE_COUNT < 0:
                                AMOUNT = ROPE_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                ROPE_COUNT = 0
                                INVENTORY.update({PICK_UP: ROPE_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")  
                        
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#TORCH DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'torch':
            #check if there if the item
            if TORCH_COUNT == 0 or TORCH_COUNT < 0:
                TORCH_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any torch at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much torches would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        TORCH_COUNT = TORCH_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: TORCH_COUNT})

                    #If dropping more than have, drop the right amount
                            if TORCH_COUNT < 0:
                                AMOUNT = TORCH_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                TORCH_COUNT = 0
                                INVENTORY.update({PICK_UP: TORCH_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#SACK DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'sack':
            #check if there if the item
            if SACK_COUNT == 0 or SACK_COUNT < 0:
                SACK_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any sack at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much sacks would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        SACK_COUNT = SACK_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: SACK_COUNT})

                    #If dropping more than have, drop the right amount
                            if SACK_COUNT < 0:
                                AMOUNT = SACK_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                SACK_COUNT = 0
                                INVENTORY.update({PICK_UP: SACK_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#WOOD DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'wood':
            #check if there if the item
            if WOOD_COUNT == 0 or WOOD_COUNT < 0:
                WOOD_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any wood at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much wood would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        WOOD_COUNT = WOOD_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: WOOD_COUNT})

                    #If dropping more than have, drop the right amount
                            if WOOD_COUNT < 0:
                                AMOUNT = WOOD_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                WOOD_COUNT = 0
                                INVENTORY.update({PICK_UP: WOOD_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#IRON DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'iron':
            #check if there if the item
            if IRON_COUNT == 0 or IRON_COUNT < 0:
                IRON_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any iron at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much iron would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        IRON_COUNT = IRON_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: IRON_COUNT})

                    #If dropping more than have, drop the right amount
                            if IRON_COUNT < 0:
                                AMOUNT = IRON_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                IRON_COUNT = 0
                                INVENTORY.update({PICK_UP: IRON_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#STEEL DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'steel':
            #check if there if the item
            if STEEL_COUNT == 0 or STEEL_COUNT < 0:
                STEEL_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any steel at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much steel would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        STEEL_COUNT = STEEL_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: STEEL_COUNT})

                    #If dropping more than have, drop the right amount
                            if STEEL_COUNT < 0:
                                AMOUNT = STEEL_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                STEEL_COUNT = 0
                                INVENTORY.update({PICK_UP: STEEL_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#GINGER DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'ginger':
            #check if there if the item
            if GINGER_COUNT == 0 or GINGER_COUNT < 0:
                GINGER_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any ginger at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much ginger would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        GINGER_COUNT = GINGER_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: GINGER_COUNT})

                    #If dropping more than have, drop the right amount
                            if GINGER_COUNT < 0:
                                AMOUNT = GINGER_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                GINGER_COUNT = 0
                                INVENTORY.update({PICK_UP: GINGER_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#GARLIC DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'garlic':
            #check if there if the item
            if GARLIC_COUNT == 0 or GARLIC_COUNT < 0:
                GARLIC_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any garlic at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much garlic would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        GARLIC_COUNT = GARLIC_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: GARLIC_COUNT})

                    #If dropping more than have, drop the right amount
                            if GARLIC_COUNT < 0:
                                AMOUNT = GARLIC_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                GARLIC_COUNT = 0
                                INVENTORY.update({PICK_UP: GARLIC_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#FISH DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'fish':
            #check if there if the item
            if FISH_COUNT == 0 or FISH_COUNT < 0:
                FISH_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any fish at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much fish would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        FISH_COUNT = FISH_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: FISH_COUNT})

                    #If dropping more than have, drop the right amount
                            if FISH_COUNT < 0:
                                AMOUNT = FISH_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                FISH_COUNT = 0
                                INVENTORY.update({PICK_UP: FISH_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#STONE DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'stone':
            #check if there if the item
            if STONE_COUNT == 0 or STONE_COUNT < 0:
                STONE_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any stone at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much stone would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        STONE_COUNT = STONE_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: STONE_COUNT})

                    #If dropping more than have, drop the right amount
                            if STONE_COUNT < 0:
                                AMOUNT = STONE_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                STONE_COUNT = 0
                                INVENTORY.update({PICK_UP: STONE_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#WOOL DROP
#--------------------------------------------------------------------------------------------I
        if PICK_UP in POSSIBLES and PICK_UP == 'wool':
            #check if there if the item
            if WOOL_COUNT == 0 or WOOL_COUNT < 0:
                WOOL_COUNT = 0
                print("--------------------------------------------------------------------------------------------I")
                print(" You don't have any wool at the moment")

            else:
                print("--------------------------------------------------------------------------------------------I")
                print(" how much wool would you like to drop?")  
                while AMOUNT == '':

                    try:
                        AMOUNT = int(input(" : "))
                        WOOL_COUNT = WOOL_COUNT - AMOUNT
            
                    #Update if in Inventory
                        if PICK_UP in INVENTORY:
                            INVENTORY.update({PICK_UP: WOOL_COUNT})

                    #If dropping more than have, drop the right amount
                            if WOOL_COUNT < 0:
                                AMOUNT = WOOL_COUNT + AMOUNT
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")
                                WOOL_COUNT = 0
                                INVENTORY.update({PICK_UP: WOOL_COUNT})
                                
                            else:
                                print("--------------------------------------------------------------------------------------------I")
                                print(" You dropped",AMOUNT, PICK_UP + "!")                              
                    
                    except:
                        print("--------------------------------------------------------------------------------------------I")
                        print(" Invaild")
            start()
#--------------------------------------------------------------------------------------------I
#AGAIN!  
#--------------------------------------------------------------------------------------------I
    else:
         print("--------------------------------------------------------------------------------------------I")
         print(" Invaild")
         start()
                    
#DONE



    






           
        


            

        

        




start()






    
