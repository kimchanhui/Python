from user import *
from product import *

def receipt():
    print()


if __name__ == '__main__' :
    command = ''
    while command != 'exit' :
        print('Command ( shopping ), ( login ), ( exit )')
        command = input()
        if command == 'shopping' :
            product_info()

            product_purchase()

        elif command == 'login' :
            user = login()
            if user == 1 :
                print('')
            else:
                command1 = ''
                while command1 != 'exit' or command1 != 'logout':
                    print(f'Command ( shopping ), ( info ), ( exit = logout ) {user}님')
                    command1 = input()
                    if command1 == 'shopping' :
                        product_info()


                    elif command1 == 'info' :
                        user_info(user)

                    else :
                        print('없는 커맨드 입니다.')
                        print()

        else:
            print('없는 커맨드 입니다.')
            print()












