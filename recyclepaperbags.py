import pgzrun
import random


#variables
Font_option=(255,255,255)

WIDTH=800
HEIGHT=600
#marking the center oh the height and width
CENTRE_X=WIDTH/2
CENTRE_Y=HEIGHT/2
CENTRE=(CENTRE_X,CENTRE_Y)
#Gameplay
FINAL_LEVEL=6
START_SPEED=10
ITEMS=("bag","battery","bottle","chips")

#game states and variables
game_over=False
game_complete=False
current_level=1
items=[]
animations=[]

#draw function runs without calling
def draw():
    #global variables
    global items, current_level, game_over, game_complete
    screen.clear()
    #blit
    screen.blit("bground,(0,0)")
    #dislplay_message
    if game_over:
        display_message("Game Over,Try again")
    elif game_complete:
        display_message("You WON, Good Job")
    else:
        for items in items:
            item.draw()

def update():
    global items
    if len(items)==0:
        items=make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)

def get_options_to_create(number_of_extra_items):
    item_to_create=["paper"] 
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
def crate_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option+"img")
        new_items.appdend(item)
    return new_items    

def layout_items(items_to_layout):
    number_of_gaps= len(items_to_layout) +1
    gap_size=WIDTH/number_of_gaps
        
def animate_items():  
   
def mouse_down():

def handle_game_complete():

def stop_animation():

def display_message():

