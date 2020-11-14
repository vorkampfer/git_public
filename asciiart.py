'''
#ASCII ART EXERCISE
#python3 asciiart.py
#what message do you want to print? Hello World!
#what color? magenta

#python3 -m pip install pyfiglet

#Help on package pyfiglet: 
#first import pyfiglet then
#run the help(pyfiglet) command in terminal

 # for general use for pyfiglet try the following,
 #code:
#help(pyfiglet.figlet_format)
#Help on function figlet_format in module pyfiglet:

#figlet_format(text, font='standard', **kwargs)
#EXAMPLE:
>>> import pyfiglet
>>> result= pyfiglet.figlet_format("Ariel")
>>> result
    _         _     # _ \n   / \\   _ __(_) ___| |\n  / _ \\ | '__| |/ _ \\ |\n / ___ \\| |  | |  __/ |\n/_/   \\_\\_|  |_|\\___|_|\n                       \n"
>>> print(result)
    _         _      _ 
   / \   _ __(_) ___| |
  / _ \ | '__| |/ _ \ |
 / ___ \| |  | |  __/ |
/_/   \_\_|  |_|\___|_|
                       

>>> result= pyfiglet.figlet_format("Sapphire <3")
>>> print(result)
 ____                    _     _             _______ 
/ ___|  __ _ _ __  _ __ | |__ (_)_ __ ___   / /___ / 
\___ \ / _` | '_ \| '_ \| '_ \| | '__/ _ \ / /  |_ \ 
 ___) | (_| | |_) | |_) | | | | | | |  __/ \ \ ___) |
|____/ \__,_| .__/| .__/|_| |_|_|_|  \___|  \_\____/ 
            |_|   |_|                                


'''
################################################################################################
# bad code? on_color = input ("Want a background color? Just hit enter to skip this. ")
#Available text colors:
#red, green, yellow, blue, magenta, cyan, white.

#code:
from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
	valid_colors = ("red", "green", "yellow, blue", "magenta", "cyan", "white")
	if color not in valid_colors:
		color = "white"
	ascii_art = figlet_format(msg)
	colored_ascii = colored(ascii_art, color=color)
	print(colored_ascii)

msg = input("What would you like to print? ")
color = input("Colors available: red, green, yellow, blue, magenta, cyan, white ")
print_art(msg, color)