import os
import screenshots
import videoEditor


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("OnlineClasses -------------------")
    print("1. Take screenshots (execute as root)")
    print("2. Cut silence on videos")
    print("Q. Exit")
    print("---------------------------------")
    
    print("Choice: ", end="", flush=True)
    return input()

if __name__ == "__main__":
    while 1:
        choice = menu()

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            screenshots.menu()
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            videoEditor.menu()
        elif choice == 'Q':
            os.system('cls' if os.name == 'nt' else 'clear')    
            exit()