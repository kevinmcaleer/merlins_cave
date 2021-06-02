# Adventure
# A really simple text adventure game written in MicroPython
# Kevin McAleer
# May 2021
# https://www.smarsfan.com

from rooms import rooms

# setup the Cave
inventory = []
items = ['key','gold','spider_repellant','fruit', 'chest', 'frog']
actions = ['go','get','look','inventory','open','help','quit']
directions = ['north','south','east','west']
move_history = []
direction_shortcuts = []
action_shortcuts = []

# setup some shortcuts - just takes the first letter from each action & direction
for action in actions:
    action_shortcuts.append(action[0])
for direction in directions:
    direction_shortcuts.append(direction[0])

# setup the game variables
current_room_id = 0
dead = False
won = False

def show_exits(current_room):
    # displays the exits for the current room

    exit_description = "Exits are to "
    for key, val in rooms[current_room].items():
        if key == 'exits':
            for exit in val:
                if exit == 's': exit_description += 'South, '
                if exit == 'n': exit_description += 'North, '
                if exit == 'e': exit_description += 'East, '
                if exit == 'w': exit_description += 'West, '
    print(exit_description)

def show_help():
    # displays the in game help
    print("*"*80)
    print("to move North, South, East or West type 'north','south','east','west' or 'n','s','e','w'")
    print("to look around and get a more detailed description type 'look' or 'l")
    print("to open something, like a chest, type 'open' or 'o'")
    print("to take or get something type 'get' or 'g' and 'take' or 't'")
    print("to check the list of things you are carrying, type 'inventory' or 'i'")
    print("To quit the game type 'quit' or 'q")
    print("*"*80)

def look(current_room):
    # shows the room title and any times in the room
    print(rooms[current_room]['title'])
    if 'items' in rooms[current_room]:
        if 'items' in rooms[current_room] is not None:
            items_message = 'You see'
            for item in rooms[current_room]['items']:
                items_message += ' '
                items_message += item
            print(items_message)
    
def show_inventory():
    # shows the players inventory (things in their pockets)
    global inventory
    if len(inventory) == 0:
        print("You're not carrying anything")
    else:
        for item in inventory:
            inventory_message = item
        print("You are carrying:", inventory_message)

def describe_location(current_room):
    # shows a more detailed description of the room
    print("*"*80)
    print(rooms[current_room]['title'])
    print(rooms[current_room]['description'])
    print("")

def get_command()->str:
    # displays the input cursor and gets the command from the user
    ''' Gets a command from the player '''
    print("Enter Command:")
    command = input('>')
    return command

def check_mob(current_room):
    # checks to see if there are any Monster Objects (mobs) in the current room
    if 'mobs' in rooms[current_room]:
        if rooms[current_room]['mobs'] is not None:
            mob_message = "You see "
            for mob in rooms[current_room]['mobs']:
                mob_message += 'a '
                mob_message += mob
            print(mob_message)

def do_action(current_room):
    global inventory, current_room_id, dead, rooms, won
    if (current_room == 9) and 'spider' in rooms[current_room]['mobs'] and 'spider_repellant' not in inventory:
        print("the spider lunges forward and kills you.")
        dead = True

    if (current_room == 9) and 'spider_repellant' in inventory:
        rooms[current_room]['items'] = ['gold']

    if current_room == 6 and 'key' not in inventory:
        print("You try to open the chest but it is locked, maybe you need a key.")

    if (current_room == 6) and 'key' in inventory:
        rooms[current_room]['items'] = ['spider_repellant']
        print("You open the chest with the Key and inside is some Spider Repellant.")
        inventory.remove('key')
  
    if (current_room == 10) and move_history == ['n','s','e','w']:
        current_room_id = 5
        print("You have managed to exit the Maze of Eternity.")

    if (current_room == 1) and 'gold' in inventory:
        won = True

def take_item(item, current_room):
    # pickup an item from the floor
    
    # bring in our global variables
    global inventory, rooms

    if item in inventory:
        print("You already have the ", item)
    else:
        if 'items' in rooms[current_room]:
            if item in rooms[current_room]['items']:
                print("You take the",item)
                inventory.append(item)
                rooms[current_room]['items'].remove(item)
        else:
            print("That items cannot be found here, or you can't take that.")

def move(direction, current_room):
    # Move the adventurer from one to another based on a direction or north, east, south and west

    # bring in the global variables
    global current_room_id, move_history

    if direction in ['n','north','s','south','e','east','w','west']:

        for room,exits in rooms[current_room].items():
            if room == 'exits':
                if direction[0] in exits:
                    current_room_id = exits[direction[0]]
                    move_message = 'You move'
                    if direction in ['n','north']: move_message += 'North'
                    if direction in ['s','south']: move_message += 'South'
                    if direction in ['e','east']: move_message += 'East'
                    if direction in ['w','west']: move_message += 'West'
                    if len(move_history) > 3:
                        move_history.pop(0)
                        # print('popping direction')
                    move_history.append(direction[0])
                else:
                    print("You can't go that way.")
           
def process_command(command, current_room):
    # Processes the command from the Adventurer

    # Get the global variable 'items' and set noun and verb to None
    global items, quit
    noun = None
    verb = None

    # split the command into individual words    
    commands = command.split()

    # check if the command is empty
    if len(command) == 0:
        print("Nothing Happend")
        return None
    # check if the command has a verb and an noun e.g. 'go north'
    if len(commands) > 2:
        print("Only provide 2 words at a time please a Verb and a Noun, e.g. 'Go North','Get Fruit'")
    
    verb = commands[0] # Get the action
    if len(commands) > 1:
        noun = commands[1] # Get the item or direction

    verb = verb.lower()
    # check if the commands are valid:
    if verb not in actions and verb not in action_shortcuts:
        print("I don't know how to", verb ,". For a list of commands type 'help'")
        return None
    if verb in ['l','look']:
        describe_location(current_room)
    if verb in ['q','quit']:
        print('Quiting time...')
        quit = True
    if verb in ['h','help']:
        show_help()
    if verb in ['i','inventory','inv']:
        show_inventory()
    if noun is not None:
        noun = noun.lower()
        if noun not in ['north','south','east','west'] and noun not in items \
            and noun not in direction_shortcuts:
            print("I don't know what a ", noun, 'is')
            return None
        else:
            if verb in ['t','take','u','use','g','get']:
                take_item(noun, current_room)
            if verb in ['o','open']:
                # do_action(current_room)       
                pass
            if verb in ['g','go']:
                move(noun, current_room)
            
        do_action(current_room)  

# *** THE MAIN PROGRAM ***

# Set the room to 1 (the cave entrance)
current_room_id = 1
quit = False

while not dead and not quit and not won: 
    # show details of the room you are in
    print('-'*80)
    look(current_room_id)
    show_exits(current_room_id)
    check_mob(current_room_id)

    # get a command from the Adventurer
    command = get_command()
    if command is not None:
        process_command(command, current_room_id)

    if dead:
        print("Oh dear, try again...")     
    if won:
        print("*"*80)
        print("*" , ' '*78,'*')
        print("Congratulations you got the gold and returned home safely.")
        print("*" , ' '*78,'*')
        print("*"*80) 
print("You leave the game. Play again soon.")
print("*"*80)