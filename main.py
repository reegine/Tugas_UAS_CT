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
    for char in text:
        print(f"{color_code}{italic_code}{char}\033[0m", end='', flush=True)  # Reset color and italic with '\033[0m'
        # time.sleep(0.001)
    print()

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

elif user_answer5 == "B" or user_answer5 == "b" :
    animate_text("\n   [???] : You don't want it? Then let me help you. ", color='blue', italic= True)
    animate_text("\nWith a sly smile, the man wiped your face with his handkerchief.")
    animate_text("\nBefore you could even react, he proceeded to clean his face with the same handkerchief.\nHis actions left you dumbfounded.")

else :
    animate_text("\nThe man laughed,")
    animate_text("\n   [???] : No worries, I'll use it after you use it. ", color='blue', italic= True)
    animate_text("\nHis response left you dumbfounded.\nYou reluctantly accepted the handkerchief and wiped your face. \nAfter returning it, the man used the same handkerchief to clean his face, just as he said before.")
   
animate_text("\n\n......\n\n")











