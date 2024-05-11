import os
import sys
from colorama import Fore, Style


def visualize_directory_structure(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError("Directory not found.")

        # Вспомогательная функция для рекурсивного обхода директорий и файлов
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

    except FileNotFoundError as e:
        print(Fore.RED + f"Error: {e}")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Вводим в терминале: python hw3.py C:/Users/br4vetrave1er/Desktop/projects/goit-algo-hw-04")
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)
