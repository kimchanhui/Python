def store():
    snacks = [
        {'name' : '과자1', 'price' : 1000, 'event' : False, 'sale' : False, 'point' : 10},
        {'name' : '과자2', 'price' : 1500, 'event' : True, 'sale' : False, 'point' : 15},
        {'name' : '과자3', 'price' : 3000, 'event' : False, 'sale' : False, 'point' : 30}
    ]


    card = 99999999
    point = 0


    while True :
        choice = input('과자를 선택 : ')
        for i in snacks :
            i.get('name')
            if choice == i.get('name') :
                print('과자의 가격 :',i.get('price'))
                YN = input('과자를 구매하시겠습니까?(네 : 아니요) : ')

                if YN == '네':
                    MC = input('결재 방법(현금 : 카드 : run) : ')
                    if MC == '현금':
                        money = int(input('가지고 있는 현금 : '))
                        if money >= i.get('price') :
                            print('구매가 완료 되었습니다.')
                            money -= i.get('price')

                            print(f'\n남은 금액 : {money} 원')
                            print('1+1 : ', i.get('event'))
                            print('할인 : ', i.get('sale'))
                            print('적립된 포인트 : ', point)
                            print('\n')
                        else:
                            print('현금이 부족합니다.')
                            break
                    elif MC == '카드' :
                        if card >= i.get('price') :
                            print('구매가 완료 되었습니다.(카드로 구매시 포인트 적립)')
                            point += i.get('point')

                            print('\n1+1 : ', i.get('event'))
                            print('할인 : ', i.get('sale'))
                            print('적립된 포인트 : ', point)
                            print('\n')
                        else:
                            print('잔액이 부족합니다.')
                            break
                    else:
                        print('run!')
                        break
                else:
                    break

if __name__ == '__main__':
    store()