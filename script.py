import sys

from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(directory: Path, indent: str = ""):

		init(autoreset=True)

		try:
			entries = sorted([e for e in directory.iterdir() if not e.name.startswith(".")], key=lambda e: (not e.is_dir(), e.name.lower()))
			for index, entry in enumerate(entries):
				connector = "|_" if index == len(entries) - 1 else "|-"
				if entry.is_dir():
					print(f"{indent}{connector} {Fore.BLUE}{entry.name}/{Style.RESET_ALL}")
					print_directory_structure(entry, indent + ("  " if index == len(entries) - 1 else "|  "))
				else:
					print(f"{indent}{connector} {Fore.GREEN}{entry.name}{Style.RESET_ALL}")
		except PermissionError:
			print(f"{Fore.RED}Доступ до {directory} заборонено!{Style.RESET_ALL}")


def main():

		if len(sys.argv) != 2:
			print("Для використання необхідно ввести: python script.py шлях/до/вашої/директорії")
			sys.exit(1)

		path = Path(r"C:\my_repo\goit-pycore-hw-04\picture")
		if not path.exists():
			print(f"{Fore.RED}Помилка: цей шлях '{path}' не існує.{Style.RESET_ALL}")
			sys.exit(1)
		if not path.is_dir():
			print(f"{Fore.RED}Помилка: '{path}' не є діректорією.{Style.RESET_ALL}")
			sys.exit(1)

		print(f"{Fore.BLUE}{path.name}/{Style.RESET_ALL}")
		print_directory_structure(path)

if __name__ == "__main__":
		main()
