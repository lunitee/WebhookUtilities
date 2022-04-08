from email import message
import time
from time import sleep
import sys
import os
import requests
import colorama
from colorama import Fore, init
from discord_webhooks import DiscordWebhooks
os.system('cls' if os.name == 'nt' else 'clear')
init(convert=True)
colorama.init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}    __               _    _       __     __    __                __      _   __      __            ")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}   / /  __  ______  (_)  | |     / ___  / /_  / /_  ____  ____  / /__   / | / __  __/ /_____  _____")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}  / /  / / / / __ \/ /   | | /| / / _ \/ __ \/ __ \/ __ \/ __ \/ //_/  /  |/ / / / / //_/ _ \/ ___/")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX} / /__/ /_/ / / / / /    | |/ |/ /  __/ /_/ / / / / /_/ / /_/ / ,<    / /|  / /_/ / ,< /  __/ /    ")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}/_____\__,_/_/ /_/_/     |__/|__/\___/_.___/_/ /_/\____/\____/_/|_|  /_/ |_/\__,_/_/|_|\___/_/     ")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}                                                                                                   ")
sleep(0.2)
print(f"{Fore.MAGENTA}\n\nMade By Lunity")
print(f'{Fore.WHITE}\n{Fore.RESET}[{Fore.LIGHTRED_EX}1{Fore.RESET}] {Fore.WHITE}Webhook Spammer{Fore.RESET}\n\n[{Fore.LIGHTRED_EX}2{Fore.RESET}] {Fore.WHITE}Webhook Deleter{Fore.YELLOW}\n')
print(f'{Fore.LIGHTRED_EX}[>] {Fore.RESET}', end='')
choice = int(input(''))

if choice not in [1, 2]:
    print(f'{Fore.LIGHTRED_EX}--------------------------------------------------------\n{Fore.LIGHTRED_EX}Option{Fore.RESET} = {Fore.RED}Error{Fore.LIGHTRED_EX} : Invalid Choice!')
    time.sleep(1)
    print(f"{Fore.RED}Exiting...")
    time.sleep(3)

if choice == 1:
    print(f"{Fore.RED}Press CTRL+C to Exit when finished with the Spammer!")
    sleep(1.3)
    print(f"{Fore.LIGHTRED_EX}--------------------------------------------------------\n{Fore.RESET} [{Fore.LIGHTRED_EX}1{Fore.RESET}]{Fore.WHITE} Webhook URL:{Fore.RESET}")
    webhook = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    print(f"{Fore.LIGHTRED_EX}--------------------------------------------------------\n{Fore.RESET} [{Fore.LIGHTRED_EX}1{Fore.RESET}]{Fore.WHITE} Message:{Fore.RESET}")
    message = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    print(f"{Fore.LIGHTRED_EX}----------SPAMMING WEBHOOK----------\n{Fore.RESET}")
    while True:
        _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
        if _data.status_code == 204:
            print(f'[{Fore.LIGHTRED_EX}WEBHOOK SPAMMER LOG{Fore.RESET}] Sent a new message!')

if choice == 2:
  print(f"{Fore.LIGHTRED_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.LIGHTRED_EX}1{Fore.RESET}]{Fore.WHITE} ENTER WEBHOOK URL:{Fore.RESET}")
  webhook_url = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
  requests.delete(webhook)
  print(f"{Fore.LIGHTGREEN_EX}Done! {Fore.RED}\nExiting now...")
  sleep(1)