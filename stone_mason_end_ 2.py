from stanfordkarel import *
def main():
    gpt()
    cen()  
    turn_left()   
    loop1() 
    gpt()   
    cen()       
    turn_right()
    loop1()
    pick_beeper() 
    turn_right()
    cen()
    turn_left() 
    loop1()
    gpt()
    cen()

    

   
def turn_right():
    for x in range(3):
        turn_left()
    
def cen():
    for i in range(4):
        chat()

def loop1():
    for i in range(4):
        move()    


        
def chat():
    move()
    pick_beeper()
    
def gpt():
    pick_beeper()
    turn_left()    
    
if __name__ == "__main__":
    run_karel_program()
