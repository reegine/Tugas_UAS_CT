import os
os.system('cls')
import time
import random
from PIL import Image
from colorit import init_colorit, background
import urllib.request 

def animate_text(text, color=None, italic=False):
    if color == 'green':
        color_code = '\033[92m'  # Green color ANSI escape code
    elif color == 'blue':
        color_code = '\033[1;36m'  # Blue color ANSI escape code
    elif color == 'red':
        color_code = '\033[0;31m'  # Red color ANSI escape code
    elif color == 'purple':
        color_code = '\033[1;35m'  # Purple color ANSI escape code
    elif color == 'yellow':
        color_code = '\033[0;33m'  # Yellow color ANSI escape code
    else:
        color_code = ''  # Empty string for default color or other color codes
    
    italic_code = '\033[3m' if italic else ''  # ANSI escape code for italic

    text = text.replace('user_major', globals().get('user_major', ''))
    text = text.replace('user_name', globals().get('user_name', ''))

    for char in text:
        print(f"{color_code}{italic_code}{char}\033[0m", end='', flush=True)  # Reset color and italic with '\033[0m'
        # time.sleep(0.001)
    print()


class Monster:
    def __init__(self):
        self.health = 50

    def take_damage(self, damage):
        self.health -= damage

user_list_of_item = []
user_monster_defeated = []
i = "Cursed Bracelet"
monster = Monster()

while True :
    os.system('cls' if os.name == 'nt' else 'clear')
    animate_text("Welcome To '......' \n")
    # urllib.request.urlretrieve('https://res.cloudinary.com/reginee/image/upload/v1611221307/samples/food/pot-mussels.jpg', "pot-mussels.jpg") 
    # img = Image.open("pot-mussels.jpg") 
    # img.show()
    animate_text("In the heart of the Egyptian desert, a recently uncovered tomb beckons with the allure of ancient mysteries. \nThe newly discovered tomb looms before you, and your curiosity intensifies as you join a group of archeologists on this extraordinary expedition.\nThe group consists of college students, older archeologists, and a man who you notice seems out of place. You feel like that man keeps staring at you. \nFeeling quite uncomfortable, you ignore his stares. \nAs you and your group gathered near the entrance, a young man from the group, probably still a student, turned to you with curiosity.")
    animate_text("\n   [Young Man] : “Are you an archeology student too?” \x1B ", color='purple', italic= True)
    user_major = "SOFTWARE ENJINIR" #input("\033[92m \nInput Your Major: \n")
    animate_text("\nYou responded with a shake of your head\n")
    animate_text("   [You] : No, I'm a user_major student.", color='green', italic=True)
    animate_text("\n   [Young Man] : “really?” \x1B ", color='purple', italic= True)
    animate_text("\nThe young man? responded in surprise.")
    animate_text("\n   [Young Man] : “Our team mainly consists of archeology majors. Why is a user_major major interested in this field?” \x1B ", color='purple', italic= True)

    animate_text("\n   Option A : I've always been interested in ancient tombs since I was a child. \n   Option B : I’m just here to observe and spend my holidays.", color='red', italic=True)
    user_answer1 = 'a' #input("\033[92m \n   Input Your Answer (A/B): ")

    if user_answer1 == 'A' or user_answer1 == 'a' :
        animate_text("\n   [You] : I've always been interested in ancient tombs since I was a child.", color='green', italic=True)
    else :
        animate_text("\n   [You] :  I’m just here to observe and spend my holidays.", color='green', italic=True)

    animate_text("\n   [Young Man] : I see” \x1B ", color='purple', italic= True)

    animate_text("\nThe young man nodded. The conversation lingered for a moment before the group shifted its focus to the tomb itself.")

    animate_text("The tomb, unearthed just a month ago, is shrouded in mystery. \nThere’s still no detailed information about this tomb. Archaeologists speculate that this tomb was the final resting place of an Egyptian god, judging by how old the tomb is. \nBut even though it has been buried for thousands or perhaps tens of thousands of years in the sands of Egypt, you can see how magnificent this god's tomb is.\n")

    animate_text("The tomb itself was a grand structure, its entrance adorned with faded hieroglyphics, offering no immediate clues about its purpose or the identity of the ancient occupant.\nIntricate carvings lined the walls of tombs, depicting scenes of ancient rituals and divine beings.\nThe air within the tomb was heavy with the weight of history, and the passageways led deeper into the heart of the ancient structure.")

    animate_text("\n\n......\n\n")

    animate_text("Darkness begins to descend upon the desert, As night falls, the ruins take on an ethereal quality, and in the maze-like corridors, you realize that you are alone,\nwhich means you have been separated from your group.")
    animate_text("\nAs you cautiously traverse the unsettling terrain in search of your group, an eerie silence hangs in the air, broken only by the distant echo of your own footsteps. ")
    animate_text("\nFinally, the sound of people chattering could be heard. Feeling relief, you approach the group of archeologists- or so what you thought.\nIt turns out, you’ve met a group of tomb riders, digging through the fragile walls.")

    animate_text("\n   What would you do?\n     Option A : RUN\n     Option B : HIDE\n", color='red', italic=True)
    user_answer2 = 'a' #input("\033[92m \n   Input Your Answer (A/B): ")

    if user_answer2 == "A" or user_answer2 == "a":
        animate_text("\n   [You] : You immediately turned and ran away from that place. Hearing your running steps, the tomb raider notices your presence.", color='green', italic=True)
    else :
        animate_text("\n   [You] :  You stopped your feet, but before you could hide, one of the men noticed your presence.\n           He looked at you in shock, and fortunately, you were quick to turn and ran away.", color='green', italic=True)

    animate_text("\n   [Tomb Riders] : HEY, CATCH THAT SCOUNDREL!", color='yellow', italic= True)

    animate_text("\n\nPanic begins to arouse in you.")
    animate_text("\nThe tomb raiders, relentless in their pursuit, closed in on you and the chase began.\nDesperation fueled your sprint as you evaded them, but the labyrinth led you to a dead-end chamber.\nA massive stone wall stands in front of you, while the relentless tomb raider becomes closer and closer.")
    animate_text("\nCornered and with nowhere to escape and your knees losing strength from too much running, you slumped in front of the stone wall.\nThe tomb raiders closed in, their weapon ready to slash directly to your head.")

    animate_text("\nWith fear and resignation, you shut your eyes.\nBut the pain never came to you.\nInstead, you can feel some liquid dripping onto your face.")
    animate_text("\nWhen you open your eyes, you see the strange man from the group stab a dagger into the tomb raider's neck, killing him before he can even scream.\nA torrent of crimson surged forth from his neck, and a chilling revelation dawned upon you: the liquid staining your face was not mere moisture, but the blood of the death tomb's raider")
    animate_text("\nThat guy now swiftly dispatched the tomb raiders with a lethal grace.\nThe clash was over almost as quickly as it began, and in the aftermath, the man turned his attention to you.")

    animate_text("\n   [???] : Can you get up? ", color='blue', italic= True)

    animate_text("\nHe extended his hand with a gentle smile on his face, ignoring the blood trickling down his cheek. The dissonance of his presence sends shivers throughout your entire body. ")
    animate_text("\n   What would you do?\n     Option A : Take His Hand\n     Option B : Ignore Him\n", color='red', italic=True)
    user_answer3 = 'a' #input("\033[92m \n   Input Your Answer (A/B): ")

    if user_answer3 == "A" or user_answer3 == "a":
        animate_text("You subconsciously took his hand to get up, and murmured a quiet ‘thank you’.", color='green', italic=True)
        animate_text("The recent event hadn't entirely settled in your mind. However, looking at the dangerous man, you believe it’s best to go along with the situation for the time being.", color='green', italic=True)
    else :
        animate_text("You stared blankly at the person in front of you as shock still lingered inside you. When you regain your senses bit by bit, you push yourself up, avoiding the dangerous man's hand.", color='green', italic=True)

    animate_text("\n\n......\n\n")

    animate_text("Suddenly,")
    animate_text("GRREEEK")
    animate_text("There was a loud sound of stones grinding against the ground. \nYou immediately turned around, recognizing that the stone wall- now transformed into a stone door, had shifted and revealed a mysterious path leading deeper into the tomb.")
    animate_text("The man beside you humm in amusement before he spoke, ")
    animate_text("\n   [???] : It looks like the blood that splattered on the rock activated a hidden mechanism- ", color='blue', italic= True)

    animate_text("he cocked his head towards you")

    animate_text("\n   [???] : Shall we head inside? ", color='blue', italic= True)

    animate_text("\n   What would you do?\n     Option A : Sure...\n     Option B : I think we should go and report to the police first…\n     Option C : I'd rather go home.", color='red', italic=True)
    user_answer4 = 'c' #input("\033[92m \n   Input Your Answer (A/B/C): ")

    if user_answer4 == "A" or user_answer4 == "a":
        ()
    elif user_answer4 == "B" or user_answer4 == "b" :
        animate_text("\nThe man looked at you with a smile that didn't quite reach his eyes.")
        animate_text("\n   [???] : The police won't understand what we're dealing with here. ", color='blue', italic= True)
        animate_text("\nAs you hear his response, a late realization comes into you.")
        animate_text("\nOf course, the psychotic man that has murdered people won't willingly turn himself to the police. What was I even thinking?", color='green', italic=True)
        animate_text("\nHis unnerving smile gradually intensifies, almost as if it's conveying to you that his proposition to enter the tomb isn't merely an invitation but rather a subtle threat.")
        animate_text("\nWary of the man, you hesitantly agreed")
        animate_text("\n   [You] :  Then… let's go inside the tomb..", color='green', italic=True)
    else :
        animate_text("\nThe man chuckled,")
        animate_text("\n   [???] : Do you really want to go home? Think about it, when will we ever come across a tomb like this again? ", color='blue', italic= True)
        animate_text("\n\nHis smile stayed the same yet his tone changed to slightly pressuring.")
        animate_text("\n   [???] : Entering is the sensible choice, wouldn't you agree? ", color='blue', italic= True)
        animate_text("\n\nYou realize that his proposition to enter the tomb isn't merely an invitation but rather a subtle threat.\nWary of the man, you hesitantly agreed, ")
        animate_text("\n   [You] :  Then… let's go inside the tomb..", color='green', italic=True)

    animate_text("\n\n......\n\n")

    animate_text("The man nodded approvingly, his smile widening.")
    animate_text("\n   [???] : Good choice ", color='blue', italic= True)
    animate_text("\nhe remarked, leading the way into the dark recesses of the tomb.")
    animate_text("\nYou obediently follow the man into the concealed passageway. The secret passage inclines downward, indicating that it will lead you to a deeper underground. \nAs soon as the two of you step past the threshold into the secret tunnel, the stone door rolls back into place. ")
    animate_text("\nLooking at the sealed exit without apparent opening, the guy in front of you let out an extragrated sigh, ")
    animate_text("\n   [???] : What a pity, it seems like we can no longer go back ", color='blue', italic= True)
    animate_text("\n   [You] : ...", color='green', italic=True)
    animate_text("\nIn the midst of finding yourself filled with regret and silently uttering curses in your heart, you find that man drawing near. \nWith the same somewhat insincere smile that never fell off his face, he extended a clean white handkerchief.")
    animate_text("\n   [???] : Here ", color='blue', italic= True)
    animate_text("\nhe gestured towards your cheeks,")
    animate_text("\n   [???] : use this to wipe your face. ", color='blue', italic= True)
    animate_text("\nIt was then you realized that your face was still splattered with freshly dried blood.\nGlancing at the man, you observed that his condition wasn't much different, if not worse.")


    animate_text("\n   What would you do?\n     Option A : Accept the handkerchief\n     Option B : Decline\n     Option C : I think you need it more.", color='red', italic=True)
    user_answer5 = 'c' #input("\033[92m \n   Input Your Answer (A/B/C): ")

    if user_answer5 == "A" or user_answer5 == "a":
        animate_text("You took the handkerchief and carefully wiped your face clean of blood. After folding it, you returned the handkerchief to its owner.")
        animate_text("Right after you returned it, the man used the same handkerchief to wipe his face.\nHis actions left you dumbfounded.")
        user_list_of_item.append("Leo's handkerchief")

    elif user_answer5 == "B" or user_answer5 == "b" :
        animate_text("\n   [???] : You don't want it? Then let me help you. ", color='blue', italic= True)
        animate_text("\nWith a sly smile, the man wiped your face with his handkerchief.")
        animate_text("\nBefore you could even react, he proceeded to clean his face with the same handkerchief.\nHis actions left you dumbfounded.")

    else :
        animate_text("\nThe man laughed,")
        animate_text("\n   [???] : No worries, I'll use it after you use it. ", color='blue', italic= True)
        animate_text("\nHis response left you dumbfounded.\nYou reluctantly accepted the handkerchief and wiped your face. \nAfter returning it, the man used the same handkerchief to clean his face, just as he said before.")
    
    animate_text("\n\n......\n\n")

    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    animate_text("You tried to hide your uncomfortable expression as he shoved the dirty cloth into his coat pocket. The two of you then walk side by side.")
    animate_text("During your walk together, he remarked, ")
    animate_text("\n   [???] : Considering we're in this together for the duration of this hidden path exploration, it wouldn't hurt to know each other's names, don’t you think? ", color='blue', italic= True)
    animate_text("\n  Would you tell your name? \n     OPTION A: My Name is... \n     OPTION B: You first", color='red', italic=True)
    user_answer6 = 'b' #input("\033[92m \n   Input Your Answer (A/B): ")

    if user_answer6 == "A" or user_answer6 == "a":
        user_name = 'Yoon Chan' #input("\033[92m \nInput Your Name: \n")
        animate_text("\n   [You] : My name is user_name,you answered him.", color='green', italic=True)
        animate_text("\nThat man smiled and called out to you,")
        animate_text("\n   [???] : user_name", color='blue', italic= True)
        animate_text("\nAfter that, he hummed and silently mouthed your name, as if getting used to calling you.")
        animate_text("‘He's a total nutcase.’ crossed your mind. The feeling of escaping from this place and this man grew even stronger.")
        animate_text("After he seemed satisfied, he turned to you and said,")
        animate_text("\n   [???] : Then, nice to meet you user_name, you can call me…", color='green', italic=True)
        animate_text("\nHe paused for a while, thinking, before opening his mouth.")
        animate_text("\n   [Leo] :Leo, you can call me Leo.", color='green', italic=True)
        animate_text("\nLooking at how he hesitated, he probably used a fake name. You can't help but silently regret telling him your real name.")

    else:
        animate_text("\n The man laughed and then stopped abruptly. He seemed to ponder for a moment before speaking,")
        animate_text("\n   [Leo] : Call me Leo. ",color='green', italic=True )
        animate_text("\nThe man grinned,")
        animate_text("\n   [Leo] : Now that I've told you my name, you should tell me yours in exchange",color='green', italic=True)
        animate_text("\n What a laugh")
        animate_text("\n Looking at how he hesitated, he probably used a fake name. Nevertheless, you still told him your name.")
        user_name = 'Yoon Chan' #input("\033[92m \nInput Your Name: \n")
        animate_text("\n   [You] : My name is user_name, you answered him.", color='green', italic=True)
        animate_text("\nThat man smiled and called out to you,")
        animate_text("\n   [???] : user_name", color='blue', italic= True)
        animate_text("\nAfter that, he hummed and silently mouthed your name, as if getting used to calling you.")
        animate_text("\n‘He's a total nutcase.’ you thought as you continued walking through the hidden road.")
        
    animate_text("\n\n......\n\n")

    animate_text("\nThe hidden passageway's walls were adorned with an array of meticulously crafted carvings, each displaying a level of clarity and detail that surpassed those found in any other section of the tomb.\n   These intricate depictions seemed to unfold a narrative, offering not only artistic beauty but also potential clues about the occupant of the tomb. ")
    animate_text("Leo seems to notice your focused gaze on the incrate walls.")
    animate_text("\nHe followed your gaze on the incrate wall")
    animate_text("\n    [Leo]: Do you know what these cravings tell ",color='blue', italic= True)
    animate_text("\nYou ponder the carvings for a moment before answering the man's question")
    animate_text("\n   [You] : These carvings seem to mostly depict the Ennead, the nine deities of ancient mythology, \n           it looks like it tells the about the great war between one of Ennead deities, Seth and his nephew, Horus, \n          judgjing by how frequently those heads and set heads symbols show up in the carvings", color='green', italic=True)

    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    animate_text("You walk further into the tomb, now alone. The longer you walk, the more you realize that this hallway is very quiet. \nIt doesn't feel as scary when you walk with Leo. The fear and uncertainty you felt with the lunatic are now replaced by a new kind of unease. \nYou wonder if it's better or worse not to have him by your side on this silent journey.")
    animate_text("\nYour steps stop when the tunnel branches to the west and east. \nSeeing a branching road, you pay attention to the walls to look for clues that might lead you out of this tomb. \nYour eyes catch an inscription on the side of the wall, but it is written in ancient Egyptian.")
    animate_text("You tried to read it but gave up. If only it was a mural or symbolic carving instead of writing, maybe you could read it.")
    animate_text("\n   Now you have to depend completely on your luck, west or east?\n     Option A : Go West\n     Option B : Go East", color='red', italic=True)
    user_answer15 = input("\033[92m \n   Input Your Answer (A/B): ")

    if user_answer15 == 'a' or user_answer15 == 'A' :
        animate_text("\nMoving westward, you maintain a brisk pace through the labyrinthine corridors of the ancient tomb. \nThe flickering light through the hall casts eerie shadows on the intricate carvings that adorn the walls. \nThe air is heavy with the scent of ancient dust, and a subtle chill sends shivers down your spine as you delve deeper into the heart of the burial chamber.")
        animate_text("\nSuddenly, as you turn a corner, the oppressive silence is broken by a soft, haunting melody that seems to resonate through the stone passages. \nThe sound is faint, yet it reverberates with an otherworldly quality that adds to the mysterious ambiance of the tomb.")
        animate_text("\nAs you cautiously proceed, the melody becomes more distinct, and you find yourself face-to-face with a surreal sight. \nThere, in the pale glow of light, stands a humanoid figure wrapped in golden-hued bandages, resembling a mummy. \nThe bandages seem to move on their own, hiding something beneath.")
        animate_text("\nWithout warning, the mummy springs to life, It reveals a golden bow and a quiver of arrows from beneath its bandages. \nThe haunting melody reaches a sudden crescendo as the creature turns its gaze towards you, raising the golden bow.")
        animate_text("\nThere’s no way to retreat from this monster without turning your back and inviting a parting shot. The only way to stay alive is to defeat the mummy. ")
        

        while monster.health > 0:
            animate_text(f"Mummy's HP: {monster.health}", color='red', italic=True) 
            animate_text("\nPress 'D' to attack the Monster!")

            user_attack1 = input("\033[92m \n   To Attack, press D: ")

            if user_attack1 == 'D' or user_attack1 == 'd':
                damage = 10  # Assuming a fixed damage value for the player's attack
                monster.take_damage(damage)
                animate_text(f"You attack the Mummy and deal {damage} damage!", color='red', italic=True)

            else:
                animate_text("Invalid input. Press 'D' to attack.")

        user_monster_defeated.append('Mummy')
        animate_text("\nWith a final clash, your dagger finds its mark, and the supernatural mummy crumbles into a cloud of dust, dissipating into the ancient air of the tomb. \nThe haunting melody fades away, leaving behind once again eerie silence. \nAs the dust settles, you notice a gleam amidst the remnants of the defeated guardian—a golden bow, the very weapon wielded by the ethereal mummy.")
        animate_text("You reach down and carefully pick up the golden bow and a limited supply of arrows. \nThe scarcity of arrows implies you may only use them sparingly in future confrontations. ")
        animate_text("\nAs you stand amidst the remnants of the defeated guardian, you notice a fancy-looking ornate door. \nPreviously, the monster's body had concealed the door, making you miss it.")
        animate_text("You approach the ornate door. The door looks like it is made of high-quality material, a testament to its endurance over thousands of years. \nThe surface is full of ornate, and there’s some kind of sunken hole in the middle of the door.")
        animate_text("You couldn’t open the door; it was locked. You likely need to find something as the key to unlock it. ")
        animate_text("\nYou wander around looking for the key to the ornate door. But instead of a key, you find a different door.")
        animate_text("This time, the door looks less luxurious than the ornate door. It's made from wood and is pretty fragile. \nThe temptation to break through it grows, and as you try, a faint noise from the other side hints at the presence of a living creature—likely a monster.")
    

        animate_text("\n   Do you want to break the wooden door? Or maybe you want to go back to the branching road and go to the east?\n     Option A : Break the wooden door\n     Option B : Return and go to the east.", color='red', italic=True)
        user_answer16 = input("\033[92m \n   Input Your Answer (A/B): ")

        if user_answer16 == 'a' or user_answer16 == 'A' :
            animate_text("Right after the wooden door breaks, a monster launches at you, confirming your earlier anticipation.")
            animate_text("The creature takes the form of a seropard—an ancient beast from the depths of time, its body a sinister blend of a leopard's agility and the sinuous neck of a serpent.  \nA sparkling jewel is embedded between its eyes, casting a glow that adds to the surreal atmosphere.")
            animate_text("\nThe seropard fixes its predatory gaze on you, emitting a low, guttural growl as it moves closer.")
            animate_text("Having become accustomed to the sudden appearance of monsters, you draw your weapon in response.")
            animate_text("\n   choose your weapon\n     Option A : Dagger\n     Option B : Golden Bow", color='red', italic=True)
            user_answer17 = input("\033[92m \n   Input Your Answer (A/B): ")

            if user_answer17 == 'a' or user_answer17 == 'A' :
                user_list_of_item.append("Dagger")
            else :
                user_list_of_item.append("Golden Bow")

            while monster.health > 0:
                animate_text(f"Seropard's HP: {monster.health}", color='red', italic=True) 
                animate_text("\nPress 'D' to attack the Monster!")

                user_attack2 = input("\033[92m \n   To Attack, press D: ")

                if user_attack2 == 'D' or user_attack2 == 'd':
                    damage = 10  # Assuming a fixed damage value for the player's attack
                    monster.take_damage(damage)
                    animate_text(f"You attack the Seropard and deal {damage} damage!", color='red', italic=True)

                else:
                    animate_text("Invalid input. Press 'D' to attack.")
            
            user_monster_defeated.append('Seropard')
            animate_text("\nJust like how it was before, this monster also crumbled to dust when defeated. \nAmong its remains, you notice a sparkling jewel that was originally embedded in its forehead. \nExamining the jewel, you ponder if it could serve as the key for the ornate door.")

            animate_text("\n   Make A Decision\n     Option A : Check the ornate door\n     Option B : Explore the chamber behind the wooden door", color='red', italic=True)
            user_answer18 = input("\033[92m \n   Input Your Answer (A/B): ")

            if user_answer18 == 'a' or user_answer18 == 'A' :
                animate_text("\nReturning to the previous ornate door, you try to put the jewel into the sunken hole in the middle of the door. When you put it in, the ornate on the door lights up and a subtle 'click' resonates through the hall.")
                animate_text("To your amazement, the ornate door begins to shift, and upon entering, you realize that you are not alone.")
            else : 
                animate_text("\nIn the chamber behind the wooden door, you found yourself surrounded by the walls adorned with a very big mural depicting scenes of Seth and Horus, engaged in an intense clash. \nSeth, with his chaotic energy, clashed ferociously against the elegant and poised Horus. \nThe colours were vibrant, each stroke of paint preserving the age-old struggle between light and darkness.")
                animate_text("When you look at it closely, you notice there's a faint glint, twinkling within the depths of Horus's left eye. ")
                animate_text("You feel compelled to examine the gleaming object in Horus' eyes. However, you realize you may need a bow or something similar to target the high-located eyes.")
                animate_text("But since you already used up all of the arrows, you have no choice but go back to check the ornate door. ")

        else :
            animate_text("\nYou return to the branching road, this time heading to the east.")
            animate_text("The passage to the east extends into the distance, leading to a well-lit room at its conclusion.")
            animate_text("The room is adorned with faintly glowing torches, casting a warm illumination that contrasts with the dark corridors you've traversed so far. \nAs you step into the room, you notice two ornate chest boxes placed at its center, each emanating an air of mystique.")
            animate_text("\nThe first chest, with a carefully crafted potion-like symbol in the middle, emits an air of alchemical elegance. \nThe craftsmanship suggests a certain mystique, hinting at the possibility of containing potent elixirs or mysterious potions. ")
            animate_text("Turning your attention to the second chest, you notice that this chest is quite plain compared to the first one.\nIt is adorned with simple carvings and doesn't give any clues about what kind of thing is stored inside.")
            animate_text("\n   Which chestbox do you want to open first?\n     Option A : Potion box\n     Option B : Plain box", color='red', italic=True)
            user_answer19 = input("\033[92m \n   Input Your Answer (A/B): ")

            if user_answer19 == 'a' or user_answer19 == "A" :
                animate_text("Upon opening the first chest, you uncovered a bottle of potion. \nDelicately removing the cork, you brought the potion to your lips, allowing the elixir to course through you. \nIn an instant, a refreshing wave revitalized your entire body. While savoring the effects, a resounding 'CRAAK' caught your attention, leading you to quickly turn toward the source of the noise. \nIt turned out that both chest boxes had instantaneously shattered into ash, which made the item inside the second chest box remain unknown forever.")
                animate_text("   [Health +10] ", color= 'green', italic=True)
                user_list_of_item.append("Potion")

            else : 
                animate_text("Upon opening the second chest, you discover a meticulously crafted obsidian-colored bracelet adorned with intricate details. \nCarefully, you slid the bracelet onto your right arm. When you wear it, \nthe obsidian bracelet seems to meld with your skin, forming peculiar runes that extend along your right forearm. \n\nA burning sensation engulfed your right arm, intensifying as if it were ablaze. \nFrantically attempting to remove it, you found that no matter your efforts, the bracelet refused to budge from your wrist.")
                animate_text("The searing discomfort persisted for a while before gradually subsiding, and the unease in your hand began to fade, returning the bracelet to its original form. \nIt appeared that this bracelet carried a curse.")
                animate_text("\nSuddenly, a resounding 'CRAACK' caught your attention, leading you to quickly turn toward the source of the noise. \nIt turned out that both chest boxes had instantaneously shattered into ash, which made the item inside the first chest box remain unknown forever.")
                user_own_bracelet = True
                user_list_of_item.append("Cursed Bracelet")

            
    else : 
        animate_text("The passage to the east extends into the distance, leading to a well-lit room at its conclusion.")
        animate_text("The room is adorned with faintly glowing torches, casting a warm illumination that contrasts with the dark corridors you've traversed so far. \nAs you step into the room, you notice two ornate chest boxes placed at its center, each emanating an air of mystique.")
        animate_text("The first chest, with a carefully crafted potion-like symbol in the middle, emits an air of alchemical elegance. \nThe craftsmanship suggests a certain mystique, hinting at the possibility of containing potent elixirs or mysterious potions. ")
        animate_text("Turning your attention to the second chest, you notice that this chest is quite plain compared to the first one.\nIt is adorned with simple carvings and doesn't give any clues about what kind of thing is stored inside.")
        animate_text("\n   Which chestbox do you want to open first?\n     Option A : Potion box\n     Option B : Plain box", color='red', italic=True)
        user_answer19 = input("\033[92m \n   Input Your Answer (A/B): ")

        if user_answer19 == 'a' or user_answer19 == "A" :
            animate_text("\nUpon opening the first chest, you uncovered a bottle of potion. \nDelicately removing the cork, you brought the potion to your lips, allowing the elixir to course through you. \nIn an instant, a refreshing wave revitalized your entire body. While savoring the effects, a resounding 'CRAAK' caught your attention, leading you to quickly turn toward the source of the noise. \nIt turned out that both chest boxes had instantaneously shattered into ash, which made the item inside the second chest box remain unknown forever.")
            animate_text("   [Health +10] ", color= 'green', italic=True)
            user_list_of_item.append("Potion")


        else : 
            animate_text("\nUpon opening the second chest, you discover a meticulously crafted obsidian-colored bracelet adorned with intricate details. Carefully, you slid the bracelet onto your right arm. \nWhen you wear it, the obsidian bracelet seems to meld with your skin, forming peculiar runes that extend along your right forearm. \nA burning sensation engulfed your right arm, intensifying as if it were ablaze. \nFrantically attempting to remove it, you found that no matter your efforts, the bracelet refused to budge from your wrist.")
            animate_text(" The searing discomfort persisted for a while before gradually subsiding, and the unease in your hand began to fade, returning the bracelet to its original form. \nIt appeared that this bracelet carried a curse.")
            animate_text("Suddenly, a resounding 'CRAACK' caught your attention, leading you to quickly turn toward the source of the noise. \nIt turned out that both chest boxes had instantaneously shattered into ash, which made the item inside the first chest box remain unknown forever.")
            user_own_bracelet = True
            user_list_of_item.append("Cursed Bracelet")

    animate_text("   ...   ")
    animate_text("\nAfter that, you exit the chamber and proceed forward. You continue to walk until you find a door, weathered by time and adorned with mystical symbols. \nWith a hesitant breath, you pushed it open and stepped into the room.")
    animate_text("Upon entering the chamber beyond the door, you encounter a creature resembling a seropard—a primal beast from ancient times, \nfeaturing the agile body of a leopard and the sinuous neck of a serpent. \nA sparkling jewel is nestled between its eyes, emitting a glow that adds to the surreal atmosphere.")
    animate_text("The seropard fixes its predatory gaze on you, emitting a low, guttural growl as it moves closer.")
    animate_text("You quickly draw your weapon in response.\n")

    while monster.health > 0:
        animate_text(f"Seropard's HP: {monster.health}", color='red', italic=True) 
        animate_text("\nPress 'D' to attack the Monster!")
        user_attack3 = input("\033[92m \n   To Attack, press D: ")

        if user_attack3 == 'D' or user_attack3 == 'd':
            damage = 10  # Assuming a fixed damage value for the player's attack
            monster.take_damage(damage)
            animate_text(f"You attack the Seropard and deal {damage} damage!", color='red', italic=True)

        else:
            animate_text("Invalid input. Press 'D' to attack.")

    user_monster_defeated.append('Seropard')
    animate_text("\nJust like how it was before, this monster also crumbled to dust when defeated. \nAmong its remains, you notice a sparkling jewel that was originally embedded in its forehead. \nExamining the jewel, you ponder if it could serve as the key for the ornate door.")

    animate_text("\nWith a final clash, your dagger finds its mark, and the supernatural seropard crumbles into a cloud of dust, dissipating into the ancient air of the tomb. \nAs the dust settles, you notice a gleam amidst the remnants of the defeated seropard—a sparking jewel that was originally embedded in its forehead. ")
    animate_text("Examining the jewel, you ponder if it could serve as something important in the journey ahead. You then shove the jewel into your pocket.")
    animate_text("\nTaking a few steps inside, you find yourself surrounded by the walls adorned with a very big mural depicting scenes of Seth and Horus, engaged in an intense clash. \nThe colors were vibrant, each stroke of paint preserving the age-old struggle between light and darkness.")
    animate_text("The atmosphere buzzed with ancient energy, urging you to explore further.")
    animate_text("Your gaze wandered, searching every corner until you spotted an anomaly—a seemingly wooden wall amidst the stone carvings. \nntuition sparked within you, hinting at a concealed passage. \nWithout hesitation, you approached and delivered a swift kick to the wooden wall. \nTo your surprise, it yielded, revealing a hidden path beyond.")
    animate_text("\nCuriosity urged you forward. At the pathway's conclusion stood an ornate door. \nThe door looks like it is made of high-quality material, a testament to its endurance over thousands of years. \nThe surface is full of ornate, and there’s some kind of sunken hole in the middle of the door.")
    animate_text("Instinctively, you reached for the jewel you had kept before and tried to place it into the sunken hole in the middle of the door. \nWhen you put it in, the ornate on the door lights up and a subtle 'click' resonates through the hall. ")
    animate_text("To your amazement, the ornate door begins to shift, and upon entering, you realize that you are not alone.")


    #-----------------------Orang satu------------------------------------------------------------------------------------------------------------------------------------------------


    animate_text("\nLeo, who had vanished earlier, is standing in front of a statue in the room.")
    animate_text("\n   What Will You Do ?\n     Option A : Greet him\n     Option B : Remain silent", color='red', italic=True)
    user_answer20 = input("\033[92m \n   Input Your Answer (A/B): ")

    if user_answer20 == "A" or user_answer20 == "a":
        animate_text("\n    [You]: Leo",color='green', italic= True)
        animate_text("\nThe one who got called turns to you with an unusual enthusiasm. ")
        animate_text("\n    [Leo]: user_name!, I was just about to search for you.",color="blue", italic=True)
    else:
        animate_text("\n You remained silent")
        animate_text("\nSilently, you approach Leo. ")
        animate_text("\nIt seems Leo recognizes your presence and turns to you with an unusual enthusiasm. ")
        animate_text("\n    [Leo]: user_name!, I was just about to search for you.",color="blue", italic=True)
        animate_text("\nHearing Leo’s response, numerous questions spark in your mind, \nlike 'Where has he been all this time?' or 'How did he manage to disappear so suddenly? ")

    animate_text("\n   What Will You Do ?\n     Option A : Where were you this whole time?\n     Option B : Remain silent", color='red', italic=True)
    user_answer21 = input("\033[92m \n   Input Your Answer (A/B): ")    

    if user_answer21 == "A" or user_answer21 == "a": 
        animate_text("\nLeo shrugged his shoulders and chuckled, ")
        animate_text("\n   [Leo]: Actually, I've been searching for something, user_name.",color="blue", italic=True)
    else:
        animate_text("\n You remained silent")
        animate_text("\nYou decided to keep your question in your head, but it became evident that Leo noticed your intense gaze directed at him.")
        animate_text("\nHe raised his eyebrow looking amused,")
        animate_text("\n   [Leo]: What's on your mind? ",color="blue", italic=True )
        animate_text("\nCaught red-handed, you became slightly flustered.")
        animate_text("\n   [user_name]: It's just... I’m just wondering where you've been all this time. ")
        animate_text("\nLeo looked and you and laughed, ")
        animate_text("\n   [Leo]: Actually, I've been searching for something, user_name.", color="blue", italic=True)
        
    animate_text("\nIt's surprising to receive a straightforward response from Leo, who typically dismisses your questions with laughter…")
    animate_text("\n   [user_name]: What kind of thing are you looking for? ", color="green", italic=True) 
    animate_text("\nLeo strides forward, moving closer to the statue in the room, and you quietly trail behind him.")
    animate_text("\nThe statue, a commanding representation of the ancient deity Seth, stands tall and imposing. \nIn its hand, the statue holds a khopesh, a curved blade with a distinctive sickle-like shape. \nThe khopesh seems to glow faintly in the dim light of the chamber, giving it an otherworldly appearance.")
    animate_text("\nLeo gently takes hold of the khopesh in the statue's hand before speaking,")
    animate_text("\n   [Leo]: I've been in pursuit of an artifact, user_name",color="blue", italic=True)

    animate_text("\nHe turned his gaze from the statue to you,")
    animate_text("\n   [Leo]: And I need a key to unlock the treasure.",color="blue", italic=True) 
    animate_text("\nWow, he properly answered your answer again… This is starting to get weird.")
    animate_text("\nIn any case, you ponder whether the statue before them holds any relevance to the key or the artifact Leo is referring to, especially given how focused he gazes at it.") 


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if i in user_list_of_item:
        #ending 1
        animate_text("\nThe blade in Leo's hand gleams with an ominous aura as he approaches, and a sense of dread washes over you.")
        animate_text("The room seems to close in, and once bare walls now reveal glowing murals expanding with eerie energy. \nThe air itself becomes charged with the impending ritual.")
        animate_text("\nLeo raises the blade, and it descends with a sickening certainty.")
        animate_text("An intense pain shoots through your body as Leo successfully stabs you, the ritual blade finding its mark. \nAgony consumes your senses, and the vibrant glow of the blade intensifies as it pierces your flesh.")
        animate_text("\nThe room quivers with an eerie energy, and the murals on the walls seem to come alive, capturing the moment of sacrifice in vivid detail.")
        animate_text("The air resonates with a melancholic hum as if the tomb itself mourns the life force now being extinguished.")
        animate_text("\nLeo, a triumphant grin on his face, withdraws the blade, leaving you gasping for breath. \nBlood stains the altar, and the vibrant glow of the blade flickers with a sinister satisfaction.")
        animate_text("\nAs the last vestiges of life slip away, your consciousness begins to fade. \nVisions of your past, fragments of moments long gone, flash before your eyes. \nThe room becomes a blur of spectral lights, and the last thing you hear is his soft whisper.")
        animate_text("\n   [Leo] : R ■ ■t  w■l■ ■y de■r■ ■t ke■. ", color='blue', italic= True)
    else:
        #ending 2
        animate_text("\nAs Leo advances with the menacing blade, an intense burning sensation erupts from your right arm, causing you to writhe in pain. \nThe burning sensation is similar to when you wore the cursed bracelet, but now, the burn is much worse. \nThe sudden agony is almost unbearable, and you choke back a scream.")
        animate_text("\nInstinctively, you glance at your right arm. \nThe cursed bracelet once again melted into your skin and has taken on the form of intricate runes, pulsing and shimmering with an otherworldly glow.")
        animate_text("\nLeo, momentarily startled, steps back as he witnesses the unexpected turn of events.")
        animate_text("\n   [Leo] : [user_name]…? ", color='blue', italic= True)
        animate_text("\nThe restraints on your body inexplicably loosen. \nIt's as if the power coursing through the runes is affecting the constraints that held you captive.")
        animate_text("\nAmidst the torment, a surge of determination courses through you. \nIf the bracelet has fused with your very being, perhaps it grants you an unexpected advantage.")
        animate_text("\n   [user_name] :...I-It hurts…, my arm is hurting...", color='green', italic=True)
        animate_text("\nLeo, who had stood back cautiously, advances toward you. \nWhen Cheungryo is close enough, you swiftly break free from your restraints and grab the blade in Leo's hands.")
        animate_text("\nAs your right hand comes into contact with the mystical blade, a surge of electricity replaces the burning sensation. \nThe clash between these two ancient artifacts results in the blade in Leo's hands being thrown.")
        animate_text("\nGathering every ounce of strength, you roll off the altar table in a swift and calculated move, catching Leo off guard. \nHis eyes widen in disbelief as he notices his weapon on the floor.")
        animate_text("\nSeeing the opportunity, you seize the restraining rope in your hands, summoning all your strength. \nYou approach Leo, who is reaching for his fallen weapon, and swiftly loop the rope around his neck.")
        animate_text("\n   [Leo] : ...You! ", color='blue', italic= True)
        animate_text("\nThe rope presses down on his neck, but of course, his resistance is strong.")
        animate_text("\nLeo struggles against the tightening grip of the rope, his eyes narrowing with a mix of anger and desperation. \nDespite his resistance, you maintain your hold, determined to keep control of the situation.")
        animate_text("\nGradually, Leo's eyes lose color from the lack of oxygen. \nIn a final moment, his eyes roll back, and his body goes limp. \nYou release the grip on the restraining rope, letting it fall to the ground as Leo collapses unconscious.")
        animate_text("\nAs you stand over Leo's unconscious form, a mix of emotions floods through you\n—relief, triumph, and a lingering sense of creep when you realize that you narrowly escaped death.")
        animate_text("\nThe runes on your arm, still glowing softly, seem to guide you as you make your way through the tomb. \nThe chamber, once filled with tension and imminent danger, now feels strangely serene.")
        animate_text("\nWith the dangerous and lunatic man now subdued, \nyou slowly navigate your way out through the secret passage of the tomb, \nleaving behind the shadows of peril and stepping into the uncertain light beyond.")
        user_monster_defeated.append('Leo')

    animate_text("\n\n======================================================================================================================================", color='green')
    animate_text("\nCongradulation user_name!!\nYou Have Finished '.....'\n\nThese are your Accomplishments!!\nHere are the monsters that you have defeated!")
    animate_text(" ",user_monster_defeated)
    animate_text("\n\nAnd these are the items that you had collected")
    animate_text(" ",user_list_of_item)

    animate_text("\n\nThank You For Playing This Role Play Game That Was Created By \n   Branden Axton Aurelius\n   Celine Davina Masko\n   Gerald Julian Kemmanandro\n   Ivan Bunardi Junganda\n   Nirwasita Padmarini Putri R.\n   Regine Angelina Halim")
    animate_text("\n======================================================================================================================================", color='green')


    play_again = input("\n\nDo you want to play again? (yes/no): ")
    if play_again.lower() == 'no':
                animate_text("Thank you for playing! Hope To See You Again!")
                break
    

























