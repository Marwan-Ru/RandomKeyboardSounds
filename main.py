import os
import random
from pynput.keyboard import Key, Listener
from playsound import playsound
import random

# List of available sounds For onpress in "sounds"
sounds_list_onpress = []
# List of available sounds For onrelease in "sounds_release"
sounds_list_onrelease = []

sound_used_on_press = []
sound_used_on_release = []

def list_files(folder_path, sound_list):
    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            full_path = os.path.join(folder_path, filename)
            sound_list.append(full_path)

def play_random_sound(sounds, list_used):
    try:
        sound_file = get_new_sound(sounds, list_used)
        playsound(sound_file)
        list_used.append(sound_file)
        if len(list_used) == len(sounds):
            list_used.clear()
    except Exception as e:
        print(f"Error playing sound: {e}")

def get_new_sound(sounds, list_used):
    already_used = True
    sound_file = random.choice(sounds)
    while already_used == True:
        already_used = False
        sound_file = random.choice(sounds)
        for s in list_used:
            if sound_file == s:
                already_used = True

    return sound_file

def on_press(key):
    if key == Key.insert:  # Add a key combination to exit the program (e.g., 'esc')
        return False  # Stop the listener
    
    
    if is_empty(sounds_list_onpress) == False:
        if random.randint(0, 1000) == 2:
            play_random_sound(sounds_list_onpress, sound_used_on_press)
    else:
        print("There is no files | sounds folder is Empty.")

def on_release(key):
    if is_empty(sounds_list_onrelease) == False and random.randint(0, 1000) == 10:
        play_random_sound(sounds_list_onrelease, sound_used_on_release)
    else:
        pass

def is_empty(alist):
    return len(alist)==0


def main():
    # Load onpress sounds from "sounds"
    list_files("sounds", sounds_list_onpress)
    print("Loded OnPress files:",sounds_list_onpress)
    # Load onrelease sounds from "sounds_release"
    list_files("sounds_release", sounds_list_onrelease)
    print("Loded OnRelease files:",sounds_list_onrelease)
    with Listener(on_press=on_press, on_release=on_release) as listener:    # start Listener 
        print("Listening for key presses. Press 'Inser' to exit.")
        listener.join()


if __name__ == "__main__":
    main()
