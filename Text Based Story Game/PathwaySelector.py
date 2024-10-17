from ctypes.wintypes import ULONG
from time import sleep

import random
from Pathway1 import *
from Pathway2 import *
import sys,time
from tkinter import N

input("Press Enter to start the game")



print(R""" 
         __________________ _______                               _       _________
|\     /|\__   __/\__   __/(  ____ \|\     /|  |\     /||\     /|( (    /|\__   __/
| )   ( |   ) (      ) (   | (    \/| )   ( |  | )   ( || )   ( ||  \  ( |   ) (   
| | _ | |   | |      | |   | |      | (___) |  | (___) || |   | ||   \ | |   | |   
| |( )| |   | |      | |   | |      |  ___  |  |  ___  || |   | || (\ \) |   | |   
| || || |   | |      | |   | |      | (   ) |  | (   ) || |   | || | \   |   | |   
| () () |___) (___   | |   | (____/\| )   ( |  | )   ( || (___) || )  \  |   | |   
(_______)\_______/   )_(   (_______/|/     \|  |/     \|(_______)|/    )_)   )_(   
Luck and choices
""")


print("\nYour luck and choices will decide your fate...")
print("If you make the wrong choice, You die")
print("If you die , you restart,.. good luck..")
print("There are many pathways in this game, which route will you take??..\n")

input("Press Enter to continue..\n\n")

skip = False


def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(5./90)   #Hello James and Marten, set it to (0./90) for instant typing, or (3./90) or whatever you like if you need to.

#beginning

sprint("You awaken...")
sleep(1)
sprint('"Where am I?" you look around you, but you stop arubtply when something catches your eyes')
sprint("\n")
sprint("A being of light draped in holy white clothes emerges before you")
sleep(1)
print(R""" 
   -=-
(\  _  /)
( \( )/ )
(       )
 `>   <'
 /     \  
 `-._.-'

 """)
sleep(2)
sprint("You watch in awe as she glides into the air, floating towards a runelike contstruct.")
sleep(2)
sprint('"Wh- Who are you?" you ask, confused with the situation')
print("\n")
sprint('"Me?" she says, "My name is Helia Young one, I have been tasked with leading you onto the right path "\n')
PlayerName = input('"What is your name Player"\n')
print(PlayerName)
print("\n")
print('"',PlayerName,'huh, how peculiar"')
print("\n")
sprint('"You share the same name as him, but can you live up to his will? "')
sprint('"We shall witness your fate.."')
print("\n")

sprint("Suddenly she stops, as she lands onto the shrine, the only construct in the vast white space above the clouds,")
sprint("you can finally see it in its true beauty")
print("\n")
sprint("It appeared to be old, however its age did not cease its modernised look.")
sprint("The bricks looked strong, impregnable even, and radiated with a holy aura that threatened to erase any tresspassers.")
print("\n")
sprint("Somehow or someway, it seemed sentient, capable of discerning who was free to use its raw power or not.")
sleep(1)
sprint("Slowly its doors opened up to allow the dainty looking angel in")
sleep(1)
print("\n")
print(R"""
              )\          _._._._  _._._._           /(
                \`--.___,'=================`.___,--'/
                 \`--._.__                 __._,--'/
                   \  ,. l`~~~~~~~~~~~~~~~'l ,.  /
       __            \||(_)!_!_!_.-._!_!_!(_)||/            __
       \\`-.__        ||_|____!!_|;|_!!____|_||        __,-'//
        \\    `==---='-----------'='-----------`=---=='    //
        | `--.                                         ,--' |
         \  ,.`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',.  /
           \||  ____,-------._,-------._,-------.____  ||/
            ||\|___!`======="!`======="!`======="!___|/||
            || |---||--------||-| | |-!!--------||---| ||
  __O_____O_ll_lO_____O_____O|| |'|'| ||O_____O_____Ol_ll_O_____O__
  o H o o H o o H o o H o o |-----------| o o H o o H o o H o o H o
 ___H_____H_____H_____H____O =========== O____H_____H_____H_____H___
                          /|=============|\
()______()______()______() '==== +-+ ====' ()______()______()______()
||{_}{_}||{_}{_}||{_}{_}/| ===== |_| ===== |\{_}{_}||{_}{_}||{_}{_}||
||      ||      ||     / |==== s(   )s ====| \     ||      ||      ||
======================()  =================  ()======================
----------------------/| ------------------- |\----------------------
                     / |---------------------| \
-'--'--'           ()  '---------------------'  ()
                   /| ------------------------- |\    --'--'--'
       --'--'     / |---------------------------| \    '--'
                ()  |___________________________|  ()           '--'-
  --'-          /| _______________________________  |\
 --'           / |__________________________________| \
""")

sleep(1)
sprint('"By using the power of this holy shrine, you can recieve abilities to push through your journey"') 
sprint('"Eventually, you can defeat your enemies and find the world ticket which will grant you ascendance and a wish."')
sleep(1)
sprint('"Which class intrests you the most young one"')
print("\n")
print("""
There are many classes, but these are the base ones:
Warrior
Archer
Mage
""")
print("\n")
sprint('"These are all the base starting classes, after your class evolution you can recieve more skills"')
sprint('"A Warrior would be able to become a berserker."')
sprint('"There are other class evolutions such as Summoner, Assassain, Jester, Enchanter, Dark Mage and Wizard"')
print("\n")
PlayerChosenClass = input('" Out of all the base classes ( Warrior, Archer, Mage ) Which path will you choose"\n')
#the input is to make the game more interactive, but you will recieve hidden tamer class
sleep(1)
print('"',PlayerChosenClass,'...? Very well then, I shall do as you wish"')
sprint('"Let us get on with the ritual"')
sleep(2)
print("\n")
sprint('"While we wait for the Shrine to finish processing its power, I must inform you of your mission"')
print("\n") 
sleep(1)
sprint('"Recently,the dark apostle, Herbia, has been deemed as an enemy of the holy kingdoms."')
sleep(1)
sprint('"Disgustingly,her name is unfortunately very similar to mine"')
print("\n")
sprint("You flinch as her attitude immediately changes at the mention of this evil witch")
print("\n")
sleep(1)
sprint('"We, the ACTUAL holy ones cannot intervene, so we have called for you in order to vanquish her"')     
sprint("'It seems this matter is of great importance to Miss Helia you think to yourself'\n")

IsHerbiaReallyThatBad = input(""" 
What would you like to responde with
1 for "Do i really have to??...I mean, I dont know what she has done and this isnt even my own world"
2 for "What has she done to recieve that treatment"
3 for "I understand"
                             \n""") 
if IsHerbiaReallyThatBad == '1': # ur dead (become stuffed doll)
    sprint('"You dare disrespect the heavens wishes like this?"')
    sleep(1)
    sprint('"Foolish mortal, I shall erase you before you decide to taint the air with your blasphemous prescence"')
    print("\n")
    print("You feel her powering up")
    sleep(1)
    sprint('"No wait, I didnt mean to disrespect you like that" you plead,')
    sleep(1)
    print("but it is already too late")
    print("\n")
    sleep(2)
    sprint("You wake up.. but you are stiff")
    sleep(1)
    sprint("You are stuck, and paralysed.... as a doll made out of a living human soul")
    sleep(1)
    sprint("You shall live for the rest of existence as so,... ")
    sleep(1)
    sprint("and not even the underworld can save you")
    print("\n")
    print("\n")
    sleep(2)
    print("You have made the wrong choice.")
    sleep(2)
    sprint("Before you embark on your long journey of silence, degradation, silence, boredom, silence and paralysation")
    sprint("you lament yourself")
    sleep(1)
    sprint('"Ah, I wish I had made the right decisions"')
    sleep(2)
    print("\n")
    print("You are a failure.")
    sleep(1)
    sprint("An entity that can literally one tap you expressed her hate on her opps,")
    sprint("however you still decide to question her")
    sleep(1)
    sprint("you are a being of ignorance, one that needed to be removed in order for this world to progress")
    sleep(3)
    print("\n")
    print("\n")
    print("\n")
    sprint("Intelligence is chasing you... however you have always been faster")
    sleep(2)
    sprint("better luck next time,.. dumbass")
    exit()
elif IsHerbiaReallyThatBad == '2':  # 2 choices, 1= u continue, 2 = u die
    sprint("The angel glares at you")
    IsHerbiaReallyThatBadContinuation = input ("""
    1 for "Sorry if i offended you, I am just curious Miss"
    2 for "So,.. are you going to answer"
    \n""")
    if IsHerbiaReallyThatBadContinuation == '1':
        sleep(1)
        sprint('"It is fine" the angel remarks')
        sleep(1)
        sprint('"She spreads chaos and terror across the realm"')
        sleep(1)
        print("\n")
        sprint('"And worst of all, she dares to rival us higher beings,"')
        sleep(1)
        sprint("'That sounds kind of petty', you think to yourself")
        sleep(1)
        sprint('"That you for informing me" you reply')
    elif IsHerbiaReallyThatBadContinuation == '2': # u die
        sleep(1)
        sprint('"How arrogant"')
        sleep(1)
        sprint('"A mere human, with not even an ounce of power in his hands"')
        sleep(1)
        sprint('"DARES TO RESPOND IN SUCH ARROGANCE TO ME?"')
        sleep(1)
        sprint('"A being of such an opulence of stupidity will not make it far regardless..."')
        sprint('"Natural selection would have taken you down anyways"')
        sleep(1)
        sprint('"Your stupidity has lead to this"')
        sleep(3)
        print("\n")
        print("\n")
        print("You have made the wrong choice.")
        sleep(2)
        print("\n")
        print("You are a failure.")
        sleep(1)
        sprint("You would respond to an angel with such arrogance and remarks?, It seems some of us have yet to evolve. ")
        sleep(1)
        sprint("Stupidity has taken ahold of you.")
        sprint("If you had been taught some manners maybe you would have survived today.")
        sleep(3)
        print("\n")
        print("\n")
        print("\n")
        sprint("Intelligence is chasing you... however you have always been faster")
        sleep(2)
        sprint("better luck next time,... rude ahh")
        exit()
elif IsHerbiaReallyThatBad == '3':
    sprint('"good"')
    sleep(1)

    


print("\n")
print("\n")
sprint("The conversation ceases, however you start to think")
sleep(1)
sprint("As you do, you feel a certain aura enveloping your surroudings")
sleep(1)
sprint("It seemed as if someone was there...however, there was no one")
sleep(1)
sprint('"Young one...Not everything is as it seems"')
sleep(1)
sprint('"Who are you"you whisper back in fear as wicked energy surrounds you')
sprint('"And where is miss Helia"')
sleep(1)
print("\n")
sprint('"We are seperated for a while. Player, she is tricking you,"')
sprint('"do not fall for her manipulative poisonous words coated in honey.."the unknown voice says"')
WouldYouLikeToFollowMeInstead = input ("""
"Would you like to follow me instead"
1 for "yes"
2 for "Who are you... and what do you want "
3 for "no"
""")
if WouldYouLikeToFollowMeInstead == '1': #kills u
    sprint('"ugh" she says')
    sprint("...\n")
    sprint("so you're one of those huh... disgusting")
    sprint('"what did i do?" you respond confused\n')
    sleep(1)
    sprint('"Your kind of people, switching sides with one sentence..."')
    sprint('"I cannot take in traitors, for you will betray me in the same way you have just betrayed that filthy angel"')
    sprint('"No variables must be left alive... good riddance"')
    sleep(3)
    print("\n")
    print("\n")
    print("You have made the wrong choice.")
    sleep(2)
    print("\n")
    print("You are simply stupid.")
    sleep(1)
    sprint("Really switched sides faster than michael jackson huh?")
    sleep(1)
    sprint("you flithy snake, someone who backstabs others every chance they get should be removed anyways.")
    sprint('"good riddance" indeed')
    sleep(3)
    print("\n")
    print("\n")
    print("\n")
    sprint("Intelligence is chasing you... however you have always been faster")
    sleep(2)
    sprint("better luck next time,... traitor..")
    exit()
elif WouldYouLikeToFollowMeInstead == '2': 
    sprint('"I am the great witch Herbia, ')
    sprint('"Their story about me is fabricated."')
    sprint('"They are just mad that a mortal such as myself has managed to ascend to a semi heavenly state"')
    sleep(1)
    print("\n")
    sprint('"Their grip on power is detestable"')
    sprint('"the so called good side strikes down anyone with the potential to reach their rank"')
    sprint('"And someday.. they shall do the same to you"')
    sleep(1)
    print("\n")
    sprint("Therefore, will you join our side,")
    sprint("the side that will will bring the treacherous two faced villains that sit atop their shiny throne to ruin")
    WillYouFollowTheWitch = input("""
    Will you follow the witch?
    1 for "Alright,..I will believe in your words and help you,..lets see what the future has in store for us..."
    2 for "No, I do not believe you"
    """)
    if WillYouFollowTheWitch == '1': #pathway 2
        sprint('" I shall lead the way, so let us leave this place quickly"')
        sleep(2)
        print("A space time rift opens up")
        sleep(1)
        print("The residue ofd ancient mana permeates through the air")
        sleep(1)
        print("Dark dreary aura fills you as you walk through")
        randomnumber = random.randint(1,3)
        randomuser = int(input("Enter a number from 1 to 3: "))
        if randomnumber == randomuser:
            print("You survived the journey")
            sleep(2)
            sprint("Welcome to the land of revolution. The Demon Kingdom...")
            from Pathway2 import *
            path_2()
           
        else:
            sprint("to be honest.... you didnt even make the wrong choice")
            sprint("You just had a skill issue")
            print("\n")
            sprint("You did not survive..your soul could not handle the burden of travelling through space and time")
            print("the correct answer was",randomnumber)
            sleep(1)
            print("\n")
            sprint("Cant even hate that much, but get better")
            sprint("improve your luck, strengthen your soul")
            sleep(1)
            print("\n")
            sprint("Intelligence has always chased you... you know what? nevermind i feel bad..")
            sprint("better luck next time..")
            exit()


         


                                     
    elif WillYouFollowTheWitch == '2': # u die
        sprint("It seems that even after questioning me, and having me tell a whole tale , ")
        sprint("you shall still be rude and reject my invitations.")
        sprint("You do not deserve this life you live, and variables must be removed anyways")
        sprint("Die, pest")
        sleep(3)
        print("\n")
        print("\n")
        print("You have made the wrong choice.")
        sleep(2)
        print("\n")
        print("You really are stupid huh?")
        sleep(1)
        sprint("You get a heaven level being to explain who they are, their stance and backstory.") 
        sprint("And you sit like a fool listening to it all, you just reject them?")
        sleep(1)
        sprint("Indecisiveness is a weakness, you would not have mad it far regardless")
        sprint('with your removal, the world becomes a better place')
        sleep(3)
        print("\n")
        print("\n")
        print("\n")
        sprint("Intelligence is chasing you... however you have always been faster")
        sleep(2)
        sprint("better luck next time,...(i lied)")
        exit()
elif WouldYouLikeToFollowMeInstead == '3': #no more pathway 2, either 1 or 3
    sprint('"You refuse???...I guess i cant force you" she says')
    sleep(1)
    sprint('"Very well then"')
    sprint(R'"I shall let you go then..... TO HELL 😈"')
    sleep(1)
    sprint('"No variables must be left.. so you shall not be allowed to exist"')
    sleep(1)
    print("\n")
    print("Herbia, the ancient witch powers up")
    print("please prepare to attempt to defeat her")
    sprint("...")
    sleep(2)
    sprint("Just as you start to regret your decisions, fate saves you")
    sprint("the angel who realised the situation calmly steps in and saves your day")
    sprint('"You are lucky, i noticed in time"she says')
    sprint('"With this you are indepted to me" she continues')



    WillYouTakeOnThisMission = input('"Will you formally take on this mission, Player? Yes or No "\n').strip().lower() #decides pathway 1 or 3
    if WillYouTakeOnThisMission.lower() == 'yes': #you will go on pathway 1
        sprint('"I must thank you hero, there will certainly be a multitiude of rewards and benefits for you"')
        sprint('"Maybe even me.... after you complete your mission though ofcourse"')
        sprint("Suddenly you feel yourself drop")
        sprint("The world twists in your vision and your sight crumbles")
        sleep(1)
        sprint("...")
        print("\n\n")
        from Pathway1 import *
        path_1()
    elif WillYouTakeOnThisMission.lower() == 'no': #test your luck in pathway 3
        sleep(1)
        sprint('"Then may death grasp your soul"')
        sleep(1)
        sprint('"Foolish Mortal....."ZWAP')
        print("fu23*&£YUR{@}{@y2")
        sleep(1)
        print(R"""
        ⣴⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢾⣷⣿⣿⣿⣿⣿⠿⠟⠛⠉⠉⠉⠉⠉⠙⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠘⢿⡏⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠒⠒⠒⠒⢢⣤⠀⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
    ⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
    ⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣿⡆⠀⠀
    ⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
    ⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣄⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠻⣿⣿⣄⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⢹⡌⢻⣿⣦⣄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠘⣧⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⢹⣿⡇⢿⣿⣿⣿⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢹⣄⣀⣀⠈⠛⢻⣿⣿⣿⣿⡏⠀⠀⠀⣿⣿⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀
    ⠀⠀⠀⠀⠀⠀⠈⣯⠉⠀⠀⠀⢸⣿⣿⣿⣿⣆⠀⠀⠀⢿⣿⡇⠸⣿⣿⣿⣿⣿⣿⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⠀⠀⠘⣿⡇⠀⢹⣿⣿⣿⣿⣿⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⢹⣧⡀⠀⣿⣿⣿⣿⡿⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⢸⣿⣿⣿⣿⣿⣿⣧⠀⠀⣿⣿⣷⣄⢹⣿⣿⣿⡇⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡄⠀⢿⣿⢿⡻⢝⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠐⠈⠁⠁⠀⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠘⣿⠃⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠟⠛⠛⠿⠿⠿⠿⠿⣿⣿⣿⣿⠿⠿⠿⢿⠿⠟⠛⠛⠃
        """)
        sleep(2)
        print("beep") # now in underworld 
        sprint("You have made the wrong choice")
        sprint("You have died..")
        sprint("You start to see, and witness a pool of darkness below you")
        sleep(1)
        sprint("Slowly, your senses return")
        sprint("And with it excruitiating pain")
        sleep(2)
        sprint("In the midst of agony, you feel")
        sprint("However you do not feel")
        sleep(1)
        sprint("You are a living being no longer, In the realm of the dead all beings are equal")
        sleep(1)
        sprint("Before the king of the underworld and his messenger, the reaper, suffering is beauty")
        sleep(1)
        HowDoYouFeel = input("How do you feel\n") # useless input
        sleep(2)
        sprint("It does not matter, your feelings are not important")
        DoYouHarbourRegretOrVengeanceInYourHeart = input("Do you harbour regret or vengeance in your heart. Yes or No\n").strip().lower()
        if DoYouHarbourRegretOrVengeanceInYourHeart.lower() == 'yes': # MAIN SCANERIO 3 you said you have regrets when underworld ruler asked 
            #(will lead you to pathway 3)
            sleep(2)
            sprint("Through the darkness of the abyss, an even darker aura emerges")
            sleep(1)
            sprint("Torrents of deathly mana rush through the space")
            sprint("A tear, rips through reality and finally,... a voice speaks to you")
            sleep(1)
            print('"We have heard your pleas,..Player"',PlayerName)
            sprint('"Your heart has the place for desire, it glows with hatred for the being who caused unjust"')
            sleep(1)
            print("\n")
            sprint("Here is your chance, for the ticket")
            print("\n")
            print("Pathway Three (hidden) unlocked")
            sleep(1)
            #this is not taken from the net, nor is it copyright or anything like that
            # this is just part of the book that im making and i thought it would be cool to put it somewhere in the game 
            # enjoy :)
            print("Welcome to pathway three, you have not joined a side of the war.")
            print("Instead, you have unlocked a hidden function of the game.")
            sleep(1)
            sprint("From now on, a chaos spirit shall read the beginning of a story to you.")
            sprint("If you answer his questions at the end correctly, you shall live and recieve your prize; if not.....\nzn")
            sleep(2)

            sprint("""
            Two people sat on the edge of a large rock, in the depth of a snake infested cavern.
            There were tiny insects swarming in the moss beneath them but they didn't seem to mind it.
            The cave was dull, glowing berries hanging from the ceiling of the deceptively uninhabited cave.
            Hisses of malice responded to the two visitor’s every move.


            The boy sat, extending his long legs. He was fitted with a black cloak that covered the surface of his body
            ,his face and neck were veiled with a scarf and mask that seemed merged and...moving?
            All his clothes were dark, and he sat in a way befitting of a emperor. The space he was in seemed warped.

            When looking at him, it was difficult to discern his true height, or build; 
            Any memorable aspect about him was useless, for his features seemed always everchanging.


            Due to this frightening aspect of him, coupled with his infamous deeds and
            the reputation of his mysterious organisation,
            that seemed to have emerged out of nowhere, he did have some admirers.
            However he had many enemies, and masses with deep grudges against him. 


            Resting on another edge of the rock, there was a girl who seemed full of radiance.
            Her hair glistened in the thin moonlight while her royal white clothes that 
            outlined her curves gracefuly reflected those very rays of light,
            the silver pattern that layered them shining like rare gemstones. Her name was Sylvia. 


            She sat, her face was covered with a beautiful smile that seemed perfect for an angelic face.
            Her eyes looked deep, as if she was thinking of an important matter.


            Yes, soon their world would reset. Again.
            A time ago, humanity as a whole was thrown into a similar copy of their own world.
            Except not so similar, this world has beasts, rituals, artifacts, abilities,
            magic, and an energy that sourced all those things.

            They knew some things, they were currently in a 'repeated tutorial'. After a period of time,
            the world resets, bringing the people who died from the last tutorial back to life.
            The goal was to allow humans to gather the maximum amount of knowledge experience they could. But why?

            Today , it would reset again. But today, it was the final time, they were going back to earth.


            “No one knows the exact time but it's soon right? The reset." She broke the silence first

            "I guess so” he shrugged

             "We spent so long leading up to where we are now" she said

            "Everything must come to an end"

            He had responded in a way she didn’t like “And it's just gonna go poof" Sylvia continued

            "Mhm" he responded dryly once more

            "Hey can you fucking respond properly, It's like I'm speaking to a rock"

            << The boy shrugs his shoulders >>

            Sylvia: "Come to think of it I've never seen your face, I don't even know your name!"
            "Those who know of you call you Anubis, and because of that tasteless mask I don't even know what you look like"

            ".."

            Sylvia: "You must have a name right?"
            "Well if you don't wanna tell me then I'll just go take care of preparations for my Clan"

            << She looks at him hoping for a reaction >>

            "You know, after the countless tutorials humanity braved, a lot of clans were made overtime. 
            But yours was somehow created instantly, even then it seemed like you decided to remain hidden.
            The strongest humans all payed attention to this because it was a little weird“

            Anubis: “And? What about it” 

            “What's weirder is that this is the first time you yourself became a thing,
            you weren’t even part of that organisation before. Its like this is the first tutorial you've done" 
            she laughs at her own joke but he remains silent.

            "Well, at least take care of your group, the future seems bleak" she utters before leaving

            "We're fine"
    
            "Hmph, with that ego you'll have it coming for you one day, and don't expect me to help you" said Sylvia jokingly
            << She starts to leave >>

            "..."
            "You said you wanted to see my face right?"

            "Haha so very funny, you've done this joke already" she said sulking

            <<He starts to take off his veils>>
            << First his cloak, then his scarf, and lastly.. his mask >>

            "What. you do this NOW!!??" 
            << But inwardly, her heart was beating rapidly, she's always dreamt of this moment >>

            Before he could remove the fabric layering his face, the air itself shook, as if being crushed by an imposing will.
            The ground quaked, the energy twisted the air, warping its surface with another reality. 
            Both humans witnessed this miracle together; The first with an energy of nature,
            very life dwelling in the air around her body.


            The second, radiated with an unfathomable aura, one that seemed to overleap itself and collapse.
            Its energy was contained, multiple threads of his energy existed in one place, 
            at the same time, one of those exact threads was in a different place, as if existing in two places at ones. 
            Frankly that was impossible, it said something about the boy...


            "Well it seems like I wont be able to show you today" he said laughingly

            "YOU IDIOT"
            "you knew this would happen didn't you"
            "Tell  me"

            She rushed towards him hoping to catch him before he disappeared. But it was already too late.
            "Tell me how you knew"
            He was gone.


            Soon, this mysterious world finished it's reset. 
            The final tutorial was over, and it was now time to go back to earth, for the real thing.
            """)

            sleep(1)
            sprint("What do you think the name of this chapter is called?")
            userchoice = input("reset, potato, clans: ")

            if userchoice.lower() == 'reset':
                print("Well done!")
                sprint("You have unlocked a ticket... Thank you for playing this game.")
            else: 
                sprint("Wrong!! :(  ")
        elif DoYouHarbourRegretOrVengeanceInYourHeart.lower() == 'No': #you said you have no regrets when underworld ruler asked (will kill you)
            sleep(2)
            print("You have made the wrong choice.")
            sleep(1)
            sprint('"Return.."')
            print("\n")
            sprint("You feel yourself losing something")
            sleep(1)
            sprint("Something deep inside of you,... Something..profound")
            sleep(1)
            sprint("A trail of essense exits your consciousness")
            sleep(1)
            sprint("In your final moments of sentience, you come to a realisation")
            sleep(1)
            sprint('"Ah, I wish I had made the right decisions"')
            sleep(2)
            print("\n")
            print("You are a failure.")
            sprint("You have been given a chance after the next, however your ignorance continues to shine")
            sleep(3)
            print("\n")
            print("\n")
            print("\n")
            sprint("Intelligence is chasing you... however you have always been faster")
            sleep(2)
            sprint("better luck next time, if there is one...")
            exit()
            #dead from pathway 3 after saying u have no regrets


