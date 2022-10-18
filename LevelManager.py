import pygame

class LevelManager:
    def __init__(self):
        pass
        
    def GetPropmtText(step):
        match step:
            case 1:
                return "After deciding that endlessly flicking through the local media was getting you nowhere, you decide that you need to get a job, and enlist in the local guards. After spending about half an hour standing in the entry hall of the barracks pouring over the woodwork at the corner of the painting, the captain finally rushes in, leaning to one side and panting. \n\"I'm glad you're here. There's rumours of a demon, summoned in a nearby crypt. I know you're new, but I'm going to need you to investigate it. I'm not going to through you in completely blind though; what equipment would you like?\" \nShrugging, you look over the possible equipment. \n(Type your answer and press enter. There are clues to the correct answer contained in the text and the pictures)\""
            case 2:
                return "After leaving the town, you find yourself at a river, with no obvious way to cross it. Puzzled, you consult your scroll, to see if it can offer any help. It reads: \n\'In your bid to find the crypt, be not tricked. For victory to be on your cards, you must take the choice that suits the guards\'."
            case 3:
                return "On the far side of the river, you quickly enter a forest, and begin to hear hoots and crys surrounding you, as the canopy blocks out most of the light. Becoming worried, lean against a tree and consult your scroll: \n\'That which waits the wood contains, you must prepare for what remains\'"
            case 4:
                return "Continuing on, you come across a stone structure in the middle of the woods. There are a few chickens clucking around it. This must be the crypt, but you don't know how to get in. The scroll only has a short hint for you: \n\'Have courage\'"
            case 5: 
                return "Venturing into the crypt, adorned with corpses of all kinds, you suddenly notice your scroll is gone. In front of you, a small imp-like creature is holding it, and with a click of his fingers it bursts into flame. Lowering his head to you theatrically (and showing of his large horns in the process), he cries: \"Welcome! They call me Pointy-End, and if you want to reach my master I'm afraid you'll have to go through me!\""
            case 6:
                return "You continue on, and finally find yourself face to face with the fearsome demon. You instantly know you have no chace of fighting it. The demon guffaws, bellowing \"You have done well to get this far! That being the case, I will offer you one chance. If you can tell me my name, I will leave this place and never return. I'm sure your journey will have contained many hints at it, if you were paying attention.\""

    def GetResult(step, text):
        resultText = ""
        match step:
            case 1:
                if "scroll" in text or "Scroll" in text:
                    return True, "You decide to pick the scroll, and somehow know you've made the right choice. It contains a list of instructions, which you hope will assist you on your journey. Slightly reluctant to fight a demon, but seeing no other option, you set off. \n(Press enter to continue)"
                elif "list" in text or "List" in text:
                    return True, "You spot the list of instruction on the scroll, and somehow know you've made the right choice. Slightly reluctant to fight a demon, but seeing not other option, you set off. \n(Press enter to continue)"
                elif "Map" in text or "map" in text:
                    return False, "You choose the map, and immediately start following it. After a crawl through a hedge, a trip through three seperate shops and a precarious leap between rooftops, you arrive back at the barracks. Looks like this wasn't the right option."
                elif "Sword" in text or "sword" in text:
                    return False, "You take the sword, and are immediatly enamoured by its heft and cut. You leave the barracks still playing with it, startling an old lady who screams and wacks you in the gut with her bag. You wake up in the hospital. Looks like this wasn't the right option."
                else:
                    return False, "\"Huh, what was that?\" says the captain. \"We don't have that, choose one of the options here.\""
            case 2:
                if "swim" in text or "Swim" in text:
                    return False, "Of course a guard would just swim the river. You boldly dive in, only to realise a few seconds later that you can't swim. As the river carries you downstream you wonder if there was a better option."
                elif "bridge" in text or "Bridge" in text:
                    return True, "You decide to look for a bridge, and spot one just a few meters away from where you were standing. You proudly march over it, feeling positivly regimental. \n(Press enter to continue)"
                elif "fly" in text or "Fly" in text or "wing" in text or "Wing" in text:
                    return False, "You focus all your will power on trying to grow wings. The force of your sheer willpower and concentration causes... you to pass out. Maybe not."
                else:
                    return False, "You try to " + text + ". You really do. But you simply don't know how to. Maybe you should, but that's what you get for staying inside till now I guess."
            case 3:
                if "sit" in text or "Sit" in text:
                    return False, "You sit down, and then immediatly stand back up, picking the thistle you just sat on out of your rear. You get the feeling you're close, but not quite right"
                elif "rest" in text or "Rest" in text:
                    return True, "You decide to rest for a bit; all this exercise all of a sudden has left you quite out of breath. As you recover, you notice the sounds of the forest around you start to quieten, and soon you feel confident to move on. \n(Press enter to continue)"
                elif "Torch" in text or "torch" in text or "fire" in text or "Fire" in text:
                    return False, "You decide some fire will scare away the beasts. With a spark, it lights, illuminating the many and hungry-looking eyes around you. Oops."
                elif "run" in text or "Run" in text or "flee" in text or "Flee" in text:
                    return False, "You leg it. Perhaps you can outpace the beasts around you. Unfortunatly the beasts turn out not to be your biggest problem, as you trip on a root and land headfirst on a rock."
                elif "wait" in text or "Wait" in text:
                    return False, "You decide to chill until the beasts go away, but notice your legs getting very tired. You have a feeling you're close to the answer, but not quite there yet."
                else:
                    return False, "No, why would you do that? That's silly, try again."
            case 4:
                if "sacrifice" in text or "Sacrifice" in text or "kill" in text or "Kill" in text or "murder" in text or "Murder" in text:
                    return False, "You look at one of the chickens, muttering a brief apology as you pick it up. The chicken stares at you with beady eyes, then proceeds to peck at your own eyes, forcing you to drop it in pain."
                elif "force" in text or "Force" in text or "break" in text or "Break" in text or "bust" in text or "Bust" in text or "charge" in text or "Charge" in text:
                    return False, "You take a run up, and charge shoulder first into the stone door. You immidiatly regret this, for obvious reasons."
                elif "feather" in text or "Feather" in text:
                    return False, "The chickens have feathers, but there aren't any on the ground. You'll need to find a way to seperate a feather from its chicken if you want one"
                elif "pluck" in text or "Pluck" in text:
                    return True, "You reach down, and pluck one of the feathers from one of the birds. It gives a startled cluck, as with a grating sound the stone crypt swings open. \n(Press enter to continue)"
                else:
                    return False, text + ", huh. You're clearly thinking outside of the box. Perhaps a bit too far outside the box."
            case 5:
                if "sword" in text or "Sword" in text or "knife" in text or "Knife" in text or "stab" in text or "Stab" in text:
                    return False, "You reach to your belt, preparing to run the imp through. After attempting to stab the imp, however, you remember that you didn't get a sword from the captain, only the scroll."
                elif "jump" in text or "Jump" in text:
                    return False, "You jump. This doesn't seem to achieve much."
                elif "bow" in text or "Bow" in text:
                    return True, "You spot a bow and a single arrow on one of the corpses decorating the crypt. With one smooth movement, you shoot Pointy-End, and he turns into smoke as the arrow passes through him. \n(Press enter to continue)"
                else:
                    return False, "You'd like to " + text + ". Unfortunatly, you can't."
            case 6:
                if "scroll" in text or "Scroll" in text or "list" in text or "List" in text:
                    return False, "Your scroll has been burnt up by the imp, it will not help you now."
                elif "bow" in text or "Bow" in text:
                    return False, "You raise your bow to shoot. However you don't have any arrows. So good luck with that."
                elif "note" in text or "Note" in text:
                    return False, "You notice a small note in your pocket. It must have fallen off the scroll. It reads: 'This is a clue'."
                elif "rumplestiltskin" in text or "Rumplestiltskin" in text:
                    return False, "\"Seriously?!\" rages the demon. \"That's it, I'm eating you.\""
                elif "violin" in text or "Violin" in text or "viola" in text or "Viola" in text or "Cello" in text or "cello" in text:
                    return True, "\"" + text + "!\" \nYou cry, and the demon's eyes widen, first in suprise, then in pain, as it begins to be sucked down to a single point. With a poof, it vanishes, leaving only silence in the crypt. You stand victorious, and return both to the city and to your life of idleness, now financed by the reward money. \nYOU WIN!"
                elif "guitar" in text or "Guitar" in text:
                    return False, "The demon looks slightly nervous, but then covers it up with a laugh. \"No, that's wrong, and not close in the slightest! Time for me to feed!\""
                else:
                    return False, "The demon laughs. \"You really think I would have a name like " + text + "?\" Then he eats you."

    def GetLeftImage(step):
        match step:
            case 1:
                return pygame.image.load("Assets/scroll.png")
            case 2:
                return pygame.image.load("Assets/swim.png")
            case 3:
                return pygame.image.load("Assets/rest.png")
            case 4:
                return pygame.image.load("Assets/kill.png")
            case 5:
                return pygame.image.load("Assets/sword.png")
            case 6:
                return pygame.image.load("Assets/scroll.png")

    def GetMiddleImage(step):
        match step:
            case 1:
                return pygame.image.load("Assets/sword.png")
            case 2:
                return pygame.image.load("Assets/bridge.png")
            case 3:
                return pygame.image.load("Assets/torch.png")
            case 4:
                return pygame.image.load("Assets/ram.png")
            case 5:
                return pygame.image.load("Assets/jump.png")
            case 6:
                return pygame.image.load("Assets/bow.png")

    def GetRightImage(step):
        match step:
            case 1:
                return pygame.image.load("Assets/map.png")
            case 2:
                return pygame.image.load("Assets/fly.png")
            case 3:
                return pygame.image.load("Assets/run.png")
            case 4:
                return pygame.image.load("Assets/feather.png")
            case 5:
                return pygame.image.load("Assets/bow.png")
            case 6:
                return pygame.image.load("Assets/note.png")