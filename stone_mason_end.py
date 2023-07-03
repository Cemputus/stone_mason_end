 from stanfordkarel import *
  
      
          
def main():
    pick_all()
    steps()
    turn_side()
    pick_all() 
    
          
     
def half(): 
    turn_left()
    for i in range(4):
        pick_move()
    pick_beeper()
    turn_left()
    
def pick_move():
    pick_beeper()
    move()


    
    
    
    
    
def steps():
    for i in range(4):
        move()

def turn_side():
    for i in range(2):
        turn_left()


def pick_all():
    half()
    steps()
    half()
    turn_side()


if __name__ == "__main__":
    run_karel_program()
