import os
import platform
import math

# wht version
wht_vers = "1.0.0"
wht_sapi_vers = "1.0.0"
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
    wht_commands = ["hlp", "vers", "clr", "eof", "scrp"]
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

    else:
        print(" Invalid command, type hlp for help.")
        wht_term()

# wht commands ext:
def wht_hlp():
    print(" wht available commands: \n "
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
                elif line == "#-wht_one_run":
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


