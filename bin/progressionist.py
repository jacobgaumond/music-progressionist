#! /opt/homebrew/bin/python3

import os
from lib.pitch import Pitch
from lib.key import Key
from lib.chord import Chord

APP_NAME = "Progressionist"

EXIT_BUTTON = 'Q'
BACK_BUTTON = 'B'

MAX_OPTIONS_PER_LINE = 4

# Technical functions
def clear_cli() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exit_app(exit_code: int=0) -> None:
    clear_cli()
    quit(exit_code)

# Printing functions
def print_app_name_header() -> None:
    print("### " + APP_NAME + " ###\n")

def print_hash_banner(num_hashes=100) -> None:
    print("\n" + "#"*num_hashes + "\n")

def print_quit_instructions() -> None:
    print("\n(Enter `" + EXIT_BUTTON + "` to EXIT)")

def print_quit_and_back_instructions() -> None:
    print("\n(Enter `" + EXIT_BUTTON + "` to EXIT or `" + BACK_BUTTON + "` to go BACK)")

# Shortcut functions
def get_str_int_list(end_int: int, start_int: int=1) -> list[str]:
    list_of_ints = list(range(start_int, end_int + 1))
    
    list_of_str_ints = []
    for int in list_of_ints:
        list_of_str_ints += str(int)
    return list_of_str_ints

# App functions
def start_screen_setup() -> None:
    SETUP_KEY_BUTTON = 'K'

    # Loop over start screen until progression
    user_input = None
    is_valid_input = False

    while(not is_valid_input):
        # Update gui
        clear_cli()
        print_app_name_header()

        print("The app that helps musicians visualize musical keys, along with the chords in the key and their notes")

        print_hash_banner()

        print("\t" + SETUP_KEY_BUTTON + ") Setup a musical key\n\n")

        print("To get started, select one of the options above by entering the corresponding symbol")

        print_quit_instructions()
        
        # Collect user input
        user_input = input().upper()
        if user_input in [EXIT_BUTTON, SETUP_KEY_BUTTON]:
            is_valid_input = True
    # Handle user input
    if user_input == EXIT_BUTTON:
        exit_app()
    elif user_input == SETUP_KEY_BUTTON:
        setup_key()

def setup_key() -> None:
    key_type = None
    key_root_pitch = None

    # Collect key_type
    ## Loop over screen until progression
    user_input = None
    is_valid_input = False

    while(not is_valid_input):
        # Update gui
        clear_cli()
        print_app_name_header()

        print_hash_banner()

        print("Setting up key (key type)...")

        print_hash_banner()

        print("\t1) MAJOR\t\t2) MINOR\n\n")

        print("Select the type of key you would like to use by entering its corresponding number...")

        print_quit_and_back_instructions()

        # Collect user input
        user_input = input().upper()
        if user_input in ([EXIT_BUTTON, BACK_BUTTON] + get_str_int_list(2)):
            is_valid_input = True
    ## Handle user input
    if user_input == EXIT_BUTTON:
        exit_app()
    elif user_input == BACK_BUTTON:
        return
    elif user_input == '1':
        key_type = "MAJOR"
    elif user_input == '2':
        key_type = "MINOR"
    else:
        raise Exception("`user_input` is not supported, even though it was read as a \"valid\" input value")
    

    # Collect key_root_pitch
    ## Loop over screen until progression
    user_input = None
    is_valid_input = False

    while(not is_valid_input):
        # Update gui
        clear_cli()
        print_app_name_header()

        print_hash_banner()

        print("Setting up key (key root pitch)...")

        print_hash_banner()

        options_printed = 0
        for pitch_num in range(len(Pitch.PITCH_LIST)):
            print("\t" + str(pitch_num + 1) + ") " + Pitch.PITCH_LIST[pitch_num], end='')

            options_printed += 1
            if options_printed < len(Pitch.PITCH_LIST): # Is this NOT the last iteration?
                if options_printed % MAX_OPTIONS_PER_LINE == 0: # Is options_printed divisible by MAX_OPTIONS_PER_LINE?
                    print() # Newline
                else:
                    print("\t", end='') # Add a tab (end result is all items are 2 tabs apart)
        print("\n\n", end='')

        print("Select the key's root pitch by entering its corresponding number...")

        print_quit_and_back_instructions()

        # Collect user input
        user_input = input().upper()
        if user_input in ([EXIT_BUTTON, BACK_BUTTON] + get_str_int_list(12)):
            is_valid_input = True
    ## Handle user input
    if user_input == EXIT_BUTTON:
        exit_app()
    elif user_input == BACK_BUTTON:
        return
    elif user_input.isdigit():
        user_input = int(user_input)
        if user_input < 1 or user_input > len(Pitch.PITCH_LIST):
            raise Exception("`user_input` was given an unsupported int, even though it was read as a \"valid\" input value")
        
        key_root_pitch = Pitch(Pitch.PITCH_LIST[user_input - 1])
    else:
        raise Exception("`user_input` is not supported, even though it was read as a \"valid\" input value")


    # Show key info screen
    key_info_screen_setup(key_type, key_root_pitch)

def key_info_screen_setup(key_type: str, key_root_pitch: Pitch) -> None:
    # Setup key
    key_scale_type = None
    if key_type == "MAJOR":
        key_scale_type = "MAJOR"
    if key_type == "MINOR":
        key_scale_type = "NATURAL_MINOR"

    musical_key = Key(key_root_pitch, key_type, key_scale_type)

    # Loop over screen until progression
    user_input = None
    is_valid_input = False

    while(not is_valid_input):
        # Update gui
        clear_cli()
        print_app_name_header()

        print_hash_banner()

        print("Displaying chord info for the key of " + str(key_root_pitch) + " " + key_type.lower())

        print_hash_banner()

        for chord_entry in musical_key.get_key_chords_and_roman_numerals():
            roman_numeral = chord_entry[0]
            chord         = chord_entry[1]

            print("\t" + roman_numeral + "\t: " + chord.get_chord_name() + "\t\t|", end='')
            for pitch in chord.get_chord_notes():
                print("\t" + str(pitch), end='')
            print()

        print_quit_and_back_instructions()

        # Collect user input
        user_input = input().upper()
        if user_input in ([EXIT_BUTTON, BACK_BUTTON]):
            is_valid_input = True
    ## Handle user input
    if user_input == EXIT_BUTTON:
        exit_app()
    elif user_input == BACK_BUTTON:
        return
    else:
        raise Exception("`user_input` is not supported, even though it was read as a \"valid\" input value")

def run_app() -> None:
    while(True): # Any finished job should ultimately return you to the start screen
        start_screen_setup()

if __name__ == "__main__":
    run_app()
