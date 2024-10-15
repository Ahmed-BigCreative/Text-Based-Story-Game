from ctypes.wintypes import ULONG
from time import sleep
import random
import sys
import time
from tkinter import N

def sprint(message):
    for c in message + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 90)

def path_2():
    sleep(2)
    print("Welcome to pathway two, you have joined the war on the side of the witches")
    sprint("3 days later...")
    sprint("You wake up and open your window")
    print("\n")
    sleep(1)
    sprint("Since you were taken by the witches, you unlock the class 'Shadow Master' instead of your chosen class")
    sprint("Today is the day that you finally head out on your journey to defeat the revolutioners' enemies.")
    sleep(1)
    print("\n")
    sprint("...")
    sprint("You find the cathedral marked on the map, however its doors are protected by a priest..")
    sprint("Defeat him to continue")

    playerhealth = 50      # Player health
    priesthealth = 100     # Priest health
    maxplayerhealth = 50   # Max health for details
    maxpriesthealth = 100  # Max health for details

    # Battle loop
    Battle = True
    while Battle:
        print(f"\nPlayer has {playerhealth}/{maxplayerhealth} health")  # Shows health of player and priest
        print(f"Priest has {priesthealth}/{maxpriesthealth} health")

        # Choice between attack or defend
        fightchoice = input("Will you 'attack' or 'defend'? ").strip().lower()

        if fightchoice == 'attack':
            playerdmg = random.randint(1, 35)  # Player damage
            priesthealth -= playerdmg
            print("\n")
            print(f"You attacked the priest with 'dark torrent' and dealt {playerdmg} damage!")

        elif fightchoice == 'defend':
            defendamount = random.randint(1, 10)  # Damage reduced
            priestdmg = random.randint(3, 8)      # Damage of priest if you defend
            effective_damage = max(0, priestdmg - defendamount)
            playerhealth -= effective_damage
            print(f"You defended! The priest dealt {effective_damage} damage.")
        else:
            print("Invalid choice, choose between either 'attack' or 'defend'.")
            continue  

        # Priest attacks if he is still alive (health over 0)
        if priesthealth > 0:
            priestdmg = random.randint(5, 10)  # Damage of priest
            playerhealth -= priestdmg
            print(f"The priest attacked you and dealt {priestdmg} damage!")
            print("----------------------------------------------------------------")

        if playerhealth <= 0:
            print("You have died..The witches regret their decision in taking you")
            exit()
        
        if priesthealth <= 0:
            print("You have defeated the priest! Victory is yours!")
            print("You move on to the next target on your list... the Cathedral Master")
            sleep(1)
            print("\n")
            sprint("As you enter a hall, you finally see the Cathedral Master sitting on a chair.")
            sprint("You approach with the intent to attack\n")
            sprint('"For the Revolution!!" you scream as you rush towards him')

            # Setup for Cathedral Master battle
            playerhealth = 100      # Player health
            maxplayerhealth = 100   # Max health for details
            cathedralmasterhealth = 150  # Cathedral Master's health
            maxcathedralmasterhealth = 150  # Max health for details

            # Battle loop for Cathedral Master
            Battle = True
            while Battle:
                print(f"\nPlayer has {playerhealth}/{maxplayerhealth} health")
                print(f"Cathedral Master has {cathedralmasterhealth}/{maxcathedralmasterhealth} health")
                enemyhealingchance = random.randint(1, 100)

                # Choice between attack or heal
                fightchoice = input("Will you 'attack' or 'heal'? ").strip().lower()

                if fightchoice == 'attack':
                    playerdmg = random.randint(15, 40)  # Player damage
                    cathedralmasterhealth -= playerdmg
                    print(f"\nYou attacked the Cathedral Master with the move 'Shadow Convulgence' and dealt {playerdmg} damage!")
                elif fightchoice == 'heal':
                    healamount = random.randint(10, 30)  # Amount of health healed
                    playerhealth = min(maxplayerhealth, playerhealth + healamount)  # Prevents healing over max health
                    print(f"You call upon the dark... the energy of the shadows revitalizes you for {healamount} health!")

                else:
                    print("Invalid choice, choose between either 'attack' or 'heal'.")
                    continue  

                # Cathedral Master attack damage
                if cathedralmasterhealth > 0:
                    cathedralmasterdmg = random.randint(10, 25)  # Damage of the enemy
                    playerhealth -= cathedralmasterdmg
                    print(f"The Cathedral Master attacked you with 'Spiritual Wash - Holy' and dealt {cathedralmasterdmg} damage!")

                    # Enemy can heal
                    if enemyhealingchance <= 20:  # 20% chance of healing
                        healamount = random.randint(10, 20)
                        cathedralmasterhealth = min(maxcathedralmasterhealth, cathedralmasterhealth + healamount)
                        print(f"The Cathedral Master calls forth holiness and heals {healamount} health!")

                    print("----------------------------------------------------------------")

                if playerhealth <= 0:
                    print("You have been purged. The witches frown upon you.")
                    exit()

                if cathedralmasterhealth <= 0:
                    print("You have defeated the Cathedral Master! There is one more enemy remaining...")
                    Battle = False
                    sleep(1)
                    sprint("You make your way over to a hidden chamber")
                    sprint("It leads to the sewers, a stinking path, unbefitting of a holy building")
                    print("\n")
                    sprint('"is this really a place under a cathederal?" you think to yourself')
                    sleep(1)
                    sprint("Finally, you reach an entrance.. you push open the door\n\n")
                    sleep(1)
                    sprint('"Hoo? Welcome...fallen hero" a gruff voice greets you from inside')
                    sprint('"As you can see, im unbefitting of a duel, due to my age of course" he speaks, his voice of a man whos seen it all')
                    sprint('"I shall give you a chance, answer my riddle and I shall let you pass"')
                    print("\n")
                    sleep(1)
                    sprint("This should be easy enough.. you think to yourself")
                    sprint('"Alright old man.. What is it.." you respond, wary\n\n')
                    sleep(1)
                    print("""
                    "Everyone who goes on the road eventually stops for a rest.

                    But my road never ends, and I never get to stop. However, I do not move.

                    I endure a perpetual journey which the years cannot stop,

                    Nations and kings cannot prevent my journey."

                    What am I?
                    """)
                    riddlechoice = input("'The sun' , 'A river' , 'A messenger'").strip().lower()
                    if riddlechoice == 'the sun':
                        sprint('"Unbelievable.. correct answer young one')
                        sprint('"You may pass"')
                        sprint("You enter another room..")
                        sprint("Inside it is dark, with the center spotlighted in a holy white light")
                        sprint("You recieve a ticket")
                        sprint("Thank you for playing!")
                    elif riddlechoice == 'a river' or 'a messenger':
                        sprint('"Wrong choice,.. Vermin"The bishop grins, as the ground under you quakes')
                        sprint('A holy artifact quakes infront of you')
                        sprint('And finally... You are sealed')
                        sleep(1)
                        print("\n")
                        sprint("Your sould perishes")
                        sprint("You have failed your mission")
                        sprint("The witches regret taking in a stupid entity")
                    else:
                        print("invalid answer")


path_2()

 