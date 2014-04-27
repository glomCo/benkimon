import pickle
import time
from random import randint
stuffs = { "name": "", "health": 0, "food": 0, "race": 0, "xp": 1, "coin": 0, "potion": 0}
def op1(lvl):
    mahpeeps = ['pred the man', 'Ben the God', 'moose the dog', 'purple the color', 'bumpy the texture']
    print mahpeeps
    return mahpeeps[lvl]
def get(w):
    if w == 1:
        return "glommy"
    if w == 2:
        return "Ben"
    if w == 3:
        return "Io"
def game():
    stuffs = pickle.load( open( "save.p", "rb" ) )
    while 1:
       # pickle.dump( stuffs, open( "save.p", "wb" ) )
        stuffs = pickle.load( open( "save.p", "rb" ) )
        print stuffs
        print """
            Where would you like to go?
            (1) training center
            (2) fight center
            (3) hospital
            (4) shop
            """
        q = int(raw_input(">"))
        if q == 4:
            print"""
SHOP
(1) 20 coin: potion
(2) 50 coin: fez
(3) 100 coin: A compliment
"""
            r = raw_input(">")
            if r == "1":
                if stuffs['coin'] < 20:
                    print "you are too poor"
                if stuffs['coin'] > 20:
                    stuffs['coin'] = stuffs['coin'] - 20
                    stuffs['potion'] = stuffs['potion'] + 1
                    pickle.dump( stuffs, open( "save.p", "wb" ) )
                    game()
            if r == "2":
                if stuffs['coin'] < 50:
                    print "you are too poor"
                if stuffs['coin'] > 50:
                    stuffs['coin'] = stuffs['coin'] - 50
                    print "You have a fez: your xp goes up by 1.337"
                    stuffs['xp'] = stuffs['xp'] + 1.337
                    pickle.dump( stuffs, open( "save.p", "wb" ) )
                    print ""
                    game()
            if r == "3":
                if stuffs['coin'] < 100:
                    print "you are too poor"
                if stuffs['coin'] > 100:
                    stuffs['coin'] = stuffs['coin'] - 100
                    print "ur purrty"
                    pickle.dump( stuffs, open( "save.p", "wb" ) )
                    game()
                            
                    
        if q == 3:
            print """
            .--.
           /.:'/
          /.:'/
         /---/
        /   /
       /---/
      /.:'/
     /.:'/ Hospital
     '--'


                """
            stuffs['health'] = 100
            print "Your health has been restored to normal"
            pickle.dump( stuffs, open( "save.p", "wb" ) )
        if q == 1:
            print """
            Welcome to the training center
            here you can fight a benkimon thats a level that you choose
            """
            lvl = int(raw_input("level: "))
            op = ""
            op = op1(lvl)
            print stuffs['name'] + " owner of " +  get(int(stuffs['race']))
            print """
             __ __  __ 
             || || (( \
             \\ //  \\ 
              \V/  \_))
            """
            print op
            time.sleep(2)
            hop = 100
            while 1:
                if hop < 0:
                    print "You won!"
                    print "1 xp and 15 coins have been awarded!"
                    stuffs['xp'] = stuffs['xp'] + 0.1
                    stuffs['coin'] = stuffs['coin']  + 15
                    print "you are level " + str(int(stuffs['xp'])) # I enjoy effiency
                    pickle.dump( stuffs, open( "save.p", "wb" ) )
                    game()
                if stuffs['health'] < 0:
                    stuffs['health'] = 100
                    print "You died. 2 xp and 20 coins have been taken away"
                    stuffs['xp'] = stuffs['xp'] - 0.2
                    stuffs['coin'] = stuffs['coin']  - 20
                    print "you are level " + str(stuffs['xp'])
                    pickle.dump( stuffs, open( "save.p", "wb" ) )
                    game()
                print op + ": "  + str(hop)#
                print "you " + ": " + str(stuffs['health'])
                print """
                (1) attack
                (2) block
                (3) heal with potions
                """
                cho = int(raw_input(">"))
                block = 0
                if cho == 1:
                    qw = 1 * stuffs['xp']/2 + randint(2,5)
                    print "you attack for " + str(qw)
                    print qw
                    hop = hop - qw
                if cho == 2:
                    print "you block"
                    block = 1
                if cho == 3:
                    if stuffs['potion'] != 0:
                        stuffs['potion'] = stuffs['potion'] - 1
                        print "you heal yourself"
                        stuffs['health'] = stuffs['health'] + randint(2,20)
                att = 1 * lvl/2 + randint(2,5)
                print op + " attacks for " + str(att)
                if block == 1:
                    stuffs['health'] = stuffs['health'] - att / 2
                    block == 0
                if block == 0:
                    stuffs['health'] = stuffs['health'] - att
                pickle.dump( stuffs, open( "save.p", "wb" ) )
                
                 
                
                    
                
print"""
Welcome to
BENKIMON
                                       
      ##                    ###  Benkimon is the best                                          
     #  ##                 #### /                                          
    #   #    #             ####                                           
   #####    # ##            #                                             
  # ###    #       #        #                                             
 #   #    #       #        ###                                            
  ###    # ##    ##    #  # # ##                                          
        #       # #   #   #####                                           
       ##      #  # ##      #                                             
         ##   #  # #        #                                             
             #   ##        # #                                            

(1) start a new game
(2) load game
"""
r = int(raw_input(">"))
if r == 1:
    print"Welcome to Benkimon!"
    
    time.sleep(1)

    print"""
    pick your benkimon:
    (1) glommy
    (2) ben
    (3) Io
    """
    e = int(raw_input(">"))
    print "I like " + get(e) + " aswell."
    stuffs['race'] = e
    e = raw_input("What should your benkimon's name be? ")
    stuffs['name'] = e
    print "alright, " + stuffs['name'] + " the " + get(stuffs['race'])
    stuffs['health'] = 100
    stuffs['food'] = 100
    stuffs['coin'] = 100
    stuffs['potion'] = 0
    pickle.dump( stuffs, open( "save.p", "wb" ) )
    game()
if r == 2:
    stuffs = pickle.load( open( "save.p", "rb" ) )
    
    print "welcome back, " + stuffs['name'] + " the " + get(stuffs ['race'])
    game()
