from time import sleep
import sys
import time

def sprint(text):
    for c in text + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 90)  # Adjust this time if it's too fast or too slow

def path_3():
    sleep(1)
    print("Welcome to pathway three, you have not joined a side of the war. Instead, you have unlocked a hidden function of the game.")
    sleep(1)
    sprint("From now on, a chaos spirit shall read the beginning of a story to you.")
    sprint("If you answer his questions at the end correctly, you shall live; if not.....")
    sleep(2)

    sprint(R"""
    Two people sat on the edge of a large rock, in the depth of a snake infested cavern.
    There were tiny insects swarming in the moss beneath them but they didn't seem to mind it.
    The cave was dull, glowing berries hanging from the ceiling of the deceptively uninhabited cave.
    Hisses of malice responded to the two visitor’s every move.


    The boy sat, extending his long legs. He was fitted with a black cloak that covered the surface of his body,\n his face and neck were veiled with a scarf and mask that seemed merged and...moving?
    All his clothes were dark, and he sat in a way befitting of a emperor. The space he was in seemed warped.\n When looking at him, it was difficult to discern his true height, or build; Any memorable aspect about him was useless, for his features seemed always everchanging. Due to this frightening aspect of him, coupled with his infamous deeds and the reputation of his mysterious organisation that seemed to have emerged out of nowhere, he did have some admirers. However he had many enemies, and masses with deep grudges against him. 

    Resting on another edge of the rock, there was a girl who seemed full of radiance.zn Her hair glistened in the thin moonlight while her royal white clothes that outlined her curves gracefuly reflected those very rays of light, the silver pattern that layered them shining like rare gemstones. Her name was Sylvia. She sat, her face was covered with a beautiful smile that seemed perfect for an angelic face. Her eyes looked deep, as if she was thinking of an important. matter.

    Yes, soon their world would reset. Again. A time ago, humanity as a whole was thrown into a similar copy of their own world.|n Except not so similar, this world has beasts, rituals, artifacts, abilities, magic, and an energy that sourced all those things.
    They knew some things, they were currently in a 'repeated tutorial'.|n After a period of time, the world resets, bringing the people who died from the last tutorial back to life. The goal was to allow humans to gather the maximum amount of knowledge experience they could. But why?

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

    "You know, after the countless tutorials humanity braved, a lot of clans were made overtime, but yours was somehow created instantly. Even then it seemed like you decided to remain hidden due to weakness or something. The strongest humans all payed attention to this because it was a little weird“

    Anubis: “And? What about it” 

    “What's weirder is that this is the first time you yourself became a thing, you weren’t even part of that organisation before. Its like this is the first tutorial you've done" she laughs at her own joke but he remains silent.

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
    Both humans witnessed this miracle together; The first with an energy of nature, very life dwelling in the air around her body.
    The second, radiated with an unfathomable aura, one that seemed to overleap itself and collapse. Its energy was contained, multiple threads of his energy existed in one place, at the same time, one of those exact threads was in a different place, as if existing in two places at ones. Frankly that was impossible, it said something about the boy...

    "Well it seems like I wont be able to show you today" he said laughingly

    "YOU IDIOT"
    "you knew this would happen didn't you"
    "Tell  me"

    She rushed towards him hoping to catch him before he disappeared. But it was already too late.
    "Tell me how you knew"
    He was gone.


    Soon, this mysterious world finished it's reset. The final tutorial was over, and it was now time to go back to earth, for the real thing.
    """)

    sleep(1)
    sprint("What do you think the name of this chapter is called?")
    userchoice = input("reset, potato, clans: ")

    if userchoice.lower() == 'reset':
        print("Well done!")
        sprint("You have unlocked a ticket... Thank you for playing this game.")
    else: 
        sprint("Wrong!! :(  ")

# Call the function to run the game
path_3()
