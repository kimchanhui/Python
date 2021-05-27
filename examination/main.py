from user import *
from product import *


if __name__ == '__main__' :
    command = ''
    while command != 'exit' :
        print('Command ( shopping ), ( login ), (  signup  ), ( exit )')
        command = input()
        if command == 'shopping' :
            product_info()

            user = 'None'

            total, quantity, price, p_name = product_purchase()

            receipt(user_name=user, total=total, quantity=quantity, price=price, p_name=p_name)

        elif command == 'login' :
            user = login()
            if user == 'no' :
                print('')
            else:
                command1 = ''
                while command1 != 'exit' or command1 == 'logout':
                    print(f'Command ( shopping ), ( info ), ( exit = logout ) {user}님')
                    command1 = input()
                    if command1 == 'shopping' :
                        product_info()

                        total, quantity, price, p_name = product_purchase()


                        receipt(user_name=user, total=total, quantity=quantity, price=price, p_name=p_name)



                    elif command1 == 'info' :
                        user_info(user)

                    elif command1 == 'exit' or command1 == 'logout' :
                        print('처음으로 돌아갑니다.')
                        print()

                    else :
                        print('없는 커맨드 입니다.')
                        print()

        elif command == 'signup' :
            signup()


        elif command == 'exit':
            print('종료합니다.')
            print()

        else:
            print('없는 커맨드 입니다.')
            print()












