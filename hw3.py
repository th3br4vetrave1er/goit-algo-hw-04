import os
import sys
from colorama import Fore, Style


def visualize_directory_structure(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError("OOPS! No such directory! Check your path!")

        def _visualize_directory(directory, indent=""):
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):
                    print(Fore.BLUE + indent + "📁 " + item)
                    _visualize_directory(item_path, indent + "    ")
                else:
                    print(Fore.GREEN + indent + "📄 " + item)

        print(Fore.YELLOW + "Directory structure:")
        _visualize_directory(directory_path)

    except FileNotFoundError as error_msg:
        print(Fore.RED + f"Error: {error_msg}")
    except Exception as error_msg:
        print(Fore.RED + f"Warning! Error: {error_msg}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Вводим в терминале - python, имя файла со скриптом через пробел - hw3.py и адрес папки - C:/Users/br4vetrave1er/Desktop/projects/goit-algo-hw-04")
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)
