from playsound import playsound
import os
import random
import time
files = []
for f in os.listdir('./Notes/'):
    if f.endswith(".aif"):
        files.append('./Notes/'+f)
print("\t  Notes Practice\n")
print("\tPress Ctrl+C to End")
def play(audio):
    try:
        print("-----------------------------------")
        print("Playing Base Note (C#4)...")
        playsound('./Notes/C#4.aif')
        print("\nNow Guess...")
        playsound(audio)
    except KeyboardInterrupt:
        exit()
    time.sleep(2)
    print("It was",audio[8:],"\n")


while True:    
    au = random.choice(files)
    play(au)
    time.sleep(2)