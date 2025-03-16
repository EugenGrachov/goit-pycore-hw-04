import colorama, sys
from colorama import Fore
from sys import Path

colorama.init(autoreset=True)

def parse_folder(dir_path,indent=""):
	for el in dir_path.interdir():
		if el.is_dir():
			print(indent + Fore.Yellow + )