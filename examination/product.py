from receipt import *
from globalVariable import *

def product_info() :
    for i in p_list:
        print()
        print('------------------------')
        print()
        print('상품 번호 :', i.get('no'))
        print('상품 이름 :', i.get('name'))
        print('상품 가격 :', i.get('price'), '원')
    print()
    print('------------------------')
    print()

def product_purchase() :
    command2 = ''
    while command2 != 'exit' :
        check = 0
        print('Command ( product_no ), ( exit )')
        command2 = input()

        null = 0
        null2 = ''

        for i in p_list :
            i
            if command2 == i.get('no') :
                price = int(i.get('price'))
                print('구매 하시겠습니끼? ( Y/N )')
                check = 1
                break


        if command2 == 'exit' :
            print('처음으로 돌아갑니다.')
            print()
            return null, null, null, null2
            break

        elif check != 1:
            print('없는 상품입니다.')
            print('상품 선택으로 돌아갑니다.')
            print()



        elif check == 1:
            YN = input()
            if YN == 'Y' :
                print('Command ( quantity )')
                quantity = int(input())
                if quantity <= 0 :
                    print('1 이상의 숫자를 입력해주세요.')
                    print('상품 선택으로 돌아갑니다.')
                    print()
                elif quantity >= 1 :
                    total = quantity * price
                    print(f'총 가격은 : {total}원 입니다.')
                    print()
                    return total, quantity, price, i.get('name')

            elif YN == 'N' :
                print('상품 선택으로 돌아갑니다.')
                print()

            else:
                print('없는 커맨드입니다.')
                print('상품 선택으로 돌아갑니다.')
                print()




                # =============================

def member_product_purchase() :
    command3 = ''
    while command3 != 'exit':
        check = 0
        print('Command ( product_no ), ( exit )')
        command3 = input()

        for i in p_list:
            i
            if command3 == i.get('no'):
                price = int(i.get('price'))
                print('구매 하시겠습니끼? ( Y/N )')
                check = 1
                break

        if check != 1:
            print('없는 상품입니다.')
            print('상품 선택으로 돌아갑니다.')
            print()

        elif check == 1:
            YN = input()
            if YN == 'Y':
                print('Command ( quantity )')
                quantity = int(input())
                if quantity <= 0:
                    print('1 이상의 숫자를 입력해주세요.')
                    print('상품 선택으로 돌아갑니다.')
                    print()
                elif quantity >= 1:
                    print(f'총 가격은 : {quantity * price}원 입니다.')
                    print()

            elif YN == 'N':
                print('상품 선택으로 돌아갑니다.')
                print()

            else:
                print('없는 커맨드입니다.')
                print('상품 선택으로 돌아갑니다.')
                print()