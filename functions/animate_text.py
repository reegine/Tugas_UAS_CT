import time
import random

def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()