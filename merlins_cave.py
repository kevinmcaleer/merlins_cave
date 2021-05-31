# Adventure
# A really simple text adventure game written in MicroPython

from rooms import rooms

inventory = []
items = ['key','gold','spider repellant','fruit']

actions = ['go','get','look','inventory','open','help','quit']
directions = ['north','south','east','west']

direction_shortcuts = []
action_shortcuts = []
for action in actions:
    action_shortcuts.append(action[0])
for direction in directions:
    direction_shortcuts.append(direction[0])

current_room_id = 0

def show_exits(current_room):
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
    print("*"*80)
    print("to move North, South, East or West type 'north','south','east','west' or 'n','s','e','w'")
    print("to look around and get a more detailed description type 'look' or 'l")
    print("to open something, like a chest, type 'open' or 'o'")
    print("to take or get something type 'get' or 'g' and 'take' or 't'")
    print("to check the list of things you are carrying, type 'inventory' or 'i'")
    print("To quit the game type 'quit' or 'q")
    print("*"*80)

def look(current_room):
    print(rooms[current_room]['title'])
    if 'items' in rooms[current_room]:
        if 'items' in rooms[current_room] is not None:
            items_message = 'You see'
            for item in rooms[current_room]['items']:
                items_message += ' '
                items_message += item
            print(items_message)
    
def show_inventory():
    global inventory
    if len(inventory) == 0:
        print("You're not carrying anything")
    else:
        for item in inventory:
            inventory_message = item
        print("You are carrying:", inventory_message)

def describe_location(current_room):
    print("*"*80)
    print(rooms[current_room]['title'])
    print(rooms[current_room]['description'])
    print("*"*80)

def get_command()->str:
    ''' Gets a command from the player '''
    print("Enter Command:")
    command = input('>')
    return command

def do_action(current_room):
    global inventory
    if (current_room == 6):
        inventory = ['spider repellant']
    if (current_room == 9) and 'spider repellant' in inventory:
        rooms[current_room]['items'] = ['gold']

def take_item(item, current_room):
    global inventory, rooms
    if item in inventory:
        print("You already have the ", item)
    else:
        if item in rooms[current_room]['items']:
            print("You take the",item)
            inventory.append(item)
            rooms[current_room]['items'].remove(item)

def move(direction, current_room):
    global current_room_id
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

def process_command(command, current_room):
    ''' Processes the command from the Adventurer'''

    # Get the global variable 'items' and set noun and verb to None
    global items, quit
    noun = None
    verb = None

    # split the command into individual words
    
    commands = command.split()
    if len(command) == 0:
        print("Nothing Happend")
        return None
    if len(commands) > 2:
        print("Only provide 2 words at a time please a Verb and a Noun, e.g. 'Go North','Get Fruit'")
    
    verb = commands[0] # Get the action
    if len(commands) > 1:
        noun = commands[1] # Get the item or direction

    # check if the commands are valid:
    if verb.lower() not in actions and verb.lower() not in action_shortcuts:
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
        if noun.lower() not in ['north','south','east','west'] and noun.lower() not in items \
            and noun.lower() not in direction_shortcuts:
            print("I don't know what a ", noun, 'is')
            return None
        else:
            if verb in ['t','take','u','use','g','get']:
                take_item(noun, current_room)
            if verb in ['o','open']:
                do_action(current_room)       
            if verb in ['g','go']:
                print("Moving",noun)
                move(noun, current_room)
            


# Set the room to 1 (the cave entrance)
current_room_id = 1
quit = False

while True and not quit: 
    # show details of the room you are in
    print('-'*80)
    look(current_room_id)
    show_exits(current_room_id)

    # get a command from the Adventurer
    command = get_command()
    if command is not None:
        process_command(command, current_room_id)
                    
print("You leave the game. Play again soon.")
print("*"*80)