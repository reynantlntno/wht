'''wht - A Python program that emulates a 'terminal' within a terminal.
    reynantlntno, 2023. 
    https://github.com/reynantlntno/wht
    
    btw, this is generally nonsense for now, there is too much work needed here.'''

import os
import platform
# import math -- maybe I should make a built-in calculator here...
# import tkinter as tk -- gui? no, cli only.

# wht version
wht_vers = "1.0.1" # version number
wht_sapi_vers = "20231015" # sub_api, for future development
wht_rel_type = "ALPHA"

# define wht funcs:
def wht_plat_check():
    wht_plat = platform.system()
    if wht_plat == "Darwin":
        wht_hello()
    elif wht_plat == "Linux":
        wht_hello()
    elif wht_plat == "Windows":
        print(f'\nFuture versions of wht will have limited support to {platform.system()}')
        wht_hello()

    else:
        print("Platform not supported.")
        exit

def wht_clear():
    if platform.system() == "Darwin" or platform.system() == "Linux" or platform.system() == "Windows":
        os.system("clear" if platform.system() == "Darwin" or platform.system() == "Linux" else "cls")
    

# wht main:
def wht_hello():
    wht_clear()
    print("\n------------------------------------\n"
          "wht Command Prompt"
          "\n------------------------------------\n")
    wht_term()
    
def wht_term():
    wht_commands = ["hlp", "vers", "clr", "exit", "scrp"]
    wht_l = "} "
    wht_input = (input(wht_l +""))

    if wht_input in wht_commands:
        if wht_input == "hlp":
            wht_hlp()

        elif wht_input == "vers":
            print(wht_vers)
            wht_term()

        elif wht_input == "clr":
            wht_clear()
            wht_term()

        elif wht_input == "scrp":
            wht_run_script()

        elif wht_input == "exit":
            wht_input = input("    Exit y/n: ")
            wht_exit_menu = ["y", "n"]
            if wht_input in wht_exit_menu:
                if wht_input == "y":
                    exit()
                elif wht_input == "n":
                    wht_term()

    else:
        print(" Invalid command, type hlp for help.")
        wht_term()

# wht commands ext:
def wht_hlp():
    print(" \n 'wht' is in early stages of development."
          " \n wht available commands: \n "
          " \n "
          "hlp - displays this help \n"
          " vers - displays wht version \n"
          " clr - clear screen \n"
          " scrp - run scripts (alpha) \n" )
    wht_term()


# under testing
def wht_run_script():
    print("\n   wht scripts only. python scripts may not work. (alpha)")
    wht_script_path = input("\n   Enter the path of the script ---> ")
    try:
        with open(wht_script_path, 'r') as wht_script_file:
            wht_script_lines = wht_script_file.readlines()
            
            for line in wht_script_lines:
                line = line.strip()

                if line == "#-wht_script":
                    print("   done. ")
                elif line == "#-wht_run":
                    exec(input("   Enter Python code to run: "))
                    wht_term()
                else:
                    print(f"   Unsupported: {line}")
                    wht_term()

    except FileNotFoundError:
        print("   File not found.")
        wht_term()

    except Exception as e:
        print(f"   An error occurred: {str(e)}")
        wht_term()


wht_plat_check()




