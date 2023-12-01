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
        color_code = '\033[0;31m'  # Blue color ANSI escape code
    elif color == 'purple':
        color_code = '\033[1;35m'  # Blue color ANSI escape code
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
user_answer2 = input("\033[92m \n   Input Your Answer (A/B): ")

if user_answer2 == "A" or user_answer2 == "a":
    animate_text("\n   [You] : You immediately turned and ran away from that place. Hearing your running steps, the tomb raider notices your presence.", color='green', italic=True)
else :
    animate_text("\n   [You] :  You stopped your feet, but before you could hide, one of the men noticed your presence.\n           He looked at you in shock, and fortunately, you were quick to turn and ran away.", color='green', italic=True)
