"""
Gratis ini silakan kalian edit free to recode!!!
by adjidev 2024
"""

import google.generativeai as genai # modul google gemini
from time import sleep as turu # delay
from colorama import Fore, init, Style
from config import key
import os
import sys

init() # init colorama

# judul nya
banner = f"""                                                                                 
{Fore.RED} _____ _____ _____ _____ _____ _____    _____ __ __ _____ _____ _____ __    _____ 
{Fore.RED}|   __|   __|     |     |   | |     |  |   __|  |  |  _  |     |  _  |  |  |   __| {Fore.YELLOW}# Adjidev 2024
{Fore.WHITE}|  |  |   __| | | |-   -| | | |-   -|  |   __|-   -|     | | | |   __|  |__|   __| {Fore.YELLOW}# Ctrl + C to exit
{Fore.WHITE}|_____|_____|_|_|_|_____|_|___|_____|  |_____|__|__|__|__|_|_|_|__|  |_____|_____|

{Fore.YELLOW}# input text

"""

genai.configure(api_key=key) # import key dari gemininya
model = genai.GenerativeModel(model_name='gemini-1.5-pro')  # model nya bisa make gemini-1.5-pro atau gemini-1.5-flash

def ngetik(teks): # animasi ngetik
    for i in teks:
        sys.stdout.write(i)
        sys.stdout.flush()
        turu(0.001)

def mulaichat():
    ngetik(banner)
    while True:
        try:
            teks = input(f'{Fore.RED}System{Fore.YELLOW}@{Fore.WHITE}Adjidev> ')
            jawabai = model.generate_content(teks)
            ngetik(f'\n{Fore.CYAN}{Style.BRIGHT}{jawabai.text}\n')
            if teks == 'clear':
                os.system('cls')
        except KeyboardInterrupt:
            ngetik(f'{Fore.RED}Exiting . . .')
            break

mulaichat()
