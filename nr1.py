import time
import random
global grandtotal1
global grandtotal2
grandtotal1 = 0
grandtotal2 = 0
def player1(t1):
    us1 = raw_input("player 1 enter 'T' to throw a dice:")
    if us1.lower()=='t':
        print "wait........dice is rolling"
        time.sleep(2)
        r1 = random.randint(1,6)
        print "You scored:",r1
        t1 = t1 + r1
        grand1(t1)
        player2(t2)
    else:
        quit()

def player2(t2):
    us2 = raw_input("Player 2 enter 'T' to throw a dice:")
    if us2.lower()=='t':
        print "wait........dice is rolling"
        time.sleep(2)
        r2 = random.randint(1,6)
        print "You scored:",r2
        t2 = t2 + r2
        grand2(t2)
        player1(t1)
    else:
        quit()

def grand1(t1):
    global grandtotal1
    grandtotal1 = grandtotal1 + t1
    if grandtotal1 >= target:
        print "player 1 wins the race"
        quit()
    else:
        print "PLAYER 1 TOTAL:",grandtotal1
        print "*"
        print "*"
        print "*"
        print "*"
    
def grand2(t2):
    global grandtotal2
    grandtotal2 = grandtotal2 + t2
    if grandtotal2 >= target:
            print "player 2 wins the race"
            quit()
    else:
            print "PLAYER 2 TOTAL:",grandtotal2
            print "*"
            print "*"
            print "*"
            print "*"
    

target = int(input("ENTER TARGET NUMBER:"))    
t1 = 0
t2 = 0

player1(t1)   
