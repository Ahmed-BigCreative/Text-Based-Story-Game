import random
import sys
import time
from ctypes.wintypes import ULONG
from time import sleep

def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 90)

def path_1():
    sprint("You wake up... as you look around you feel a person on your left\n")
    sprint('"It seems you have finally awoken, hero," he says softly.')
    time.sleep(1)
    sprint('"W-What happened?" you say, bewildered\n')
    sprint('"It seems that the aura of two incredible beings has shocked you to your core," he replies with an eerie smile on his face.')
    sprint('You sit there in silence as you think, but he stammers on...\n\n')
    time.sleep(1)
    sprint('"It seems that the deviation in your aura has caused some issues in your class awakening..." the bishop says.')
    sprint('"Not to worry, however, you were blessed with the paladin class."')
    time.sleep(1)
    sprint('"Please read this," he says as he hands you a tea-colored paper.\n')
    print("You take the paper and open it")
    sprint("""
       it reads...
       Hello dear hero,
You have been graced with the paladin class; your first attack is Light Slash.

You must defeat 3 monsters by following the map given to you: 
The Undead Zombie (drops core of healing),
The Tainted Minotaur (drops core of defense),
And finally... The Dark Serpent (drops the material needed to go on the second part of your adventure..)

In order to use these dropped rewards, you must call upon the power of the shrine.
I wish you luck.

- Helia
    """)
    print("\n\n")
    time.sleep(3)
    sprint('"Here is your map, sir hero. I shall leave you to it now," he says as he finally leaves.\n\n')
    sleep(1)
    sprint("After making your preparations you follow the map given to you to a dark forest.")
    sprint("Here, you finally see your first target... the undead zombie.")
    sprint("You rush towards him and your battle system gifted by the angel activates.")

    # Battle starts
    # For the battle 
    battle = True

    # Class of the player
    class Player:
        def __init__(self, name, health):
            self.name = name
            self.health = health
            self.max_health = health  # saves the max health

        def attack(self, target):
            damage = random.randint(16, 25)
            print(f"\n{self.name} uses 'Light Slash' and attacks {target.name} for {damage} damage!")
            target.health -= damage

    # Class for the zombie
    class Zombie:
        def __init__(self, name, health):
            self.name = name
            self.health = health
            self.max_health = health  # saves the max health

        def attack(self, target):
            damage = 10
            print(f"\n{self.name} attacks {target.name} for {damage} damage!")
            target.health -= damage

        def heal(self):
            heal_amount = random.randint(8, 10)
            if self.health + heal_amount > self.max_health:  # prevents overhealing
                heal_amount = self.max_health - self.health
            self.health += heal_amount
            print(f"{self.name} heals by {heal_amount}!")

    player = Player("Player One", 50)
    zombie = Zombie("Zombie", 100)

    # Start of actual battle with Zombie
    while battle:
        action = input("\nType 'attack': ").lower()

        if action == "attack":
            player.attack(zombie)
        else:
            print("Invalid option. Please type 'attack'.")
            continue

        if zombie.health > 0:
            if random.choice(["attack", "heal"]) == "attack":
                zombie.attack(player)
            else:
                zombie.heal()

        # Display health
        print(f"\nPlayer Health: {player.health} / {player.max_health}")
        print(f"Zombie Health: {zombie.health} / {zombie.max_health}")
        
        # Adds line to make it look better
        print("---------------------------------------")

        # Player dead... repeat story
        if player.health <= 0:
            print("You have died... The Angel Helia looks down at you with disgust.")
            battle = False
            exit()

        # Zombie dead... continue the story
        if zombie.health <= 0:
            print("The zombie has been slain... it drops a dark core of healing. Return to the shrine to evolve.")
            sleep(1)
            print("You call upon the name of the shrine")   
            sleep(1)
            sprint("The stonelike core starts to disappear. \nYou feel a power entering your body... you have evolved.")
            sprint("You have unlocked the power of healing.")
            sleep(1)
            sprint("After a little rest, you continue on your path into the maze where the tainted minotaur lives.")
            sleep(1)
            sprint("Finally, you spot the minotaur in the distance; you charge towards him to fight...")

            # Start of fight with the minatour
            battle = True

            # Class of the hero
            class Hero:
                def __init__(self, name, health):
                    self.name = name
                    self.health = health
                    self.max_health = health  # saves starting hero health

                def attack(self, target):
                    damage = random.randint(18, 30)  # buffed attack of hero
                    print(f"\n{self.name} uses 'Holy Cleave' and attacks {target.name} for {damage} damage!")
                    target.health -= damage

                def heal(self):
                    heal_amount = random.randint(10, 20)
                    if self.health + heal_amount > self.max_health:  # stops healing over starting health
                        heal_amount = self.max_health - self.health
                    self.health += heal_amount
                    print(f"The Hero calls upon the angel for healing... his pleas have been heard. Heals by {heal_amount}!")

            # Class for the Minotaur
            class Minotaur:
                def __init__(self, name, health):
                    self.name = name
                    self.health = health
                    self.max_health = health  # was going to make the minatour able to heal too but figured thats too op, however when i remove this line it breaks the code and idk why so i left it

                def attack(self, target):
                    damage = random.randint(15, 25)  # Buffed Minotaur attack
                    print(f"\n{self.name} attacks {target.name} for {damage} damage!")
                    target.health -= damage

                def defend(self):
                    print(f"{self.name} grasps the darkness, it braces itself for the next attack!")

            hero = Hero("The Hero", 60)  # made hero stronger
            minotaur = Minotaur("Tainted Minotaur", 120)  

            # Start of actual battle with Minotaur
            while battle:
                action = input("\nType 'attack' or 'heal': ").lower()

                if action == "attack":
                    hero.attack(minotaur)
                elif action == "heal":
                    hero.heal()
                else:
                    print("Invalid option. Please type 'attack' or 'heal'.")
                    continue

                if minotaur.health > 0:
                    if random.choice(["attack", "defend"]) == "attack":
                        minotaur.attack(hero)
                    else:
                        minotaur.defend()

                # shows health
                print(f"\nHero Health: {hero.health} / {hero.max_health}")
                print(f"{minotaur.name} Health: {minotaur.health} / {minotaur.max_health}")
                
                # Adds line to make it look better
                print("---------------------------------------")

                # Hero dead... 
                if hero.health <= 0:
                    print("You have died... The Angel Helia looks down at you with disdain")
                    battle = False
                    exit()

                # Minotaur has died, 1 more boss
                if minotaur.health <= 0:
                    print("The Tainted Minotaur has been slain... it drops a core of defense. Return to the shrine to evolve.")
                    time.sleep(1)
                    print("You call upon the name of the shrine.")   
                    time.sleep(1)
                    sprint("The stonelike core starts to disappear. \nYou feel a power entering your body... you have evolved.")
                    sprint("You have unlocked the power of defense.")
                    sleep(1)
                    print("\n\n")
                    sprint("After taking one more rest break you venture onwards to the final enemy..")
                    sprint("The serpent..")
                    sleep(1)
                    print("\n")
                    sprint("After many twists and turns you finally eneter a large cavern")
                    sprint("The hairs on your neck screech and you instinctively summon a holy shielf to protect you")
                    sleep(1)
                    sprint("Just in time... the serpent appears behind you")
                    # Start of fight with the Dark Serpent
                    battle = True

                    # Class of the hero
                    class Hero:
                        def __init__(self, name, health):
                            self.name = name
                            self.health = health
                            self.max_health = health  # saves starting hero health

                        def attack(self, target):
                            damage = random.randint(20, 35)  #heros damage is strronger now
                            print(f"\n{self.name} uses 'Sun Slash' and attacks {target.name} for {damage} damage!")
                            target.health -= damage

                        def heal(self):
                            heal_amount = random.randint(15, 25)  
                            if self.health + heal_amount > self.max_health:  # stops healing over the starting health
                                heal_amount = self.max_health - self.health
                            self.health += heal_amount
                            print(f"The Hero calls upon the angel for healing... his pleas have been heard. Heals by {heal_amount}!")

                        def defend(self):
                            print(f"{self.name} raises their shield, channeling holy energy to protect against the next attack!")

                    # Class for the Dark Serpent
                    class DarkSerpent:
                        def __init__(self, name, health):
                            self.name = name
                            self.health = health
                            self.max_health = health  # saves starting serpent health

                        def attack(self, target):
                            damage = random.randint(25, 40)  
                            print(f"\n{self.name} attacks {target.name} for {damage} damage!")
                            target.health -= damage

                        def heal(self):
                            heal_amount = random.randint(10, 20)  # healing percentagesof for the serpent
                            if self.health + heal_amount > self.max_health:  # prevents healing over serpents startign health
                                heal_amount = self.max_health - self.health
                            self.health += heal_amount
                            print(f"{self.name} absorbs dark energy, healing for {heal_amount}!")

                        def defend(self):
                            print(f"{self.name} coils around itself, bracing for the next attack!")

                    hero = Hero("The Hero", 80)  # hero health (buffed)
                    dark_serpent = DarkSerpent("Dark Serpent", 150)  

                    # Start of actual battle with Dark Serpent
                    while battle:
                        action = input("\nType 'attack', 'heal', or 'defend': ").lower()

                        if action == "attack":
                            hero.attack(dark_serpent)
                        elif action == "heal":
                            hero.heal()
                        elif action == "defend":
                            hero.defend()
                            continue
                        else:
                            print("Invalid option. Please type 'attack', 'heal', or 'defend'.")
                            continue

                        if dark_serpent.health > 0:
                            if random.choice(["attack", "heal", "defend"]) == "attack":
                                dark_serpent.attack(hero)
                            elif random.choice(["heal"]) == "heal":
                                dark_serpent.heal()
                            else:
                                dark_serpent.defend()
                                continue

                        # showing the healths
                        print(f"\nHero Health: {hero.health} / {hero.max_health}")
                        print(f"{dark_serpent.name} Health: {dark_serpent.health} / {dark_serpent.max_health}")

                        # Adds line to make it look better
                        print("---------------------------------------")

                        # if hero dies
                        if hero.health <= 0:
                            print("You have died... The Angel Helia looks down at you with disdain.")
                            battle = False
                            exit()

                        # Dark Serpent dead... continue the story
                        if dark_serpent.health <= 0:
                            print("The Dark Serpent has been slain... it drops a powerful artifact. Return to the shrine to evolve.")
                            sleep(1)
                            print("You call upon the name of the shrine.")
                            sleep(1)
                            sprint("The artifact shimmers as it disappears into your hands. \nYou feel a power entering your body... you have evolved.")
                            sprint("You have unlocked a ticket....")
                            sleep(1)
                            sprint("Thank you for playing this game")
                            break
                            exit()
path_1()
