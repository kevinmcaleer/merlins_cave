rooms = {
    1: {
        'title':'The Cave Entrance',
        'description': 'You are stood on the rocky beach in front of a large cave entrance. This is Merlins ' 
            'Cave, underneath Camelot Castle in Tintagle, Cornwall. The wind whistles in and out of the cave '  
            'Entrance beconning you in',
        'exits': {
            'n': 2
        },
        'items': {
            'fruit'
        }
    },
    2: {
        'title' : 'The Ante-chamber',
        'description': 'You are in a large chamber, with the Cave Entrance to the South',
        'exits': {
            'n':3,
            's':1
        }
    },
    3: {
        'title': 'Narrow Passage way',
        'description': 'You are in a dark and narrow passage way you can see light ahead and the passage entrance to the rear.',
        'exits': {
            'n':4,
            's':2
        }
    },
    4: {
        'title': 'Large Cave',
        'description': 'You are in a large cave and can hear a dripping sound to the East. There is a strange symbol'
            'above the Western exit. Its nice an warm in here, and it looks like this area has seen lots of people passing through.',
        'exits': {
            'n':6,
            's':3,
            'w':5,
            'e':7
        }
    },
    5: {
        'title':'Maze Entrance',
        'description': 'To the West is the Entrance to the Maze of Eternity. Few who enter ever leave - make sure'
           'you know the secret before entering this maze or you may never leave',
        'exits': {
            'w':10,
            'e':4
        }
    },
    6: {
        'title': 'Chest Room',
        'description': 'This room has a low ceiling, and leaning on the far wall is a large chest',
        'exits': {
            's':4
        }
    },
    7: {
        'title': 'The Waterfall',
        'description': 'The room has a large waterfall gushing down the Easterly wall, the water disappears down a crack in the floor.',
        'exits': {
            'w':4,
            's':8
        }
    },
    8: {
        'title':'Foul Smelling room',
        'description':'This room has a fowl stench, like rotting fish. The room is covered in ancient spiderwebs.',
        'exits': {
            'n':7,
            's':9
        }
    },
    9: {
        'title':'The Spiders Den',
        'description': 'You have wandered into a spiders den. The room is covered in spiderwebs some with things wrapped up inside them.',
        'exits': {
            'n':8,
        },
        'items': {
            'gold',
        }
    },
    10: {
        'title':'You are in the Maze of Eternity',
        'description':'This room looks like the one you just came from, about 3 meters by 3 meters with no distinguishing marks.',
        'exits': {
            'n': 10,
            's': 10,
            'w': 10,
            'e': 10,
        },
        'items': {
            'key',
        }
    } 
}