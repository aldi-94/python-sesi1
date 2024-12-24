from libs import welcome_message, exit_program
from games import gaga
from tools import warung


def menu ():
    user_option = int(input(f'menu program:\n1. Games Gaga\n2. Warung Mini Market \n3. Keluar Program\n\nsilahkan pilih: '))

    if user_option == 1:
        gaga.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_program()
    else:
        print('hanya boleh pilih yang tersedia di menu!') 

def main():
    welcome_message()
    menu()


if __name__ == '__main__':
    main()

