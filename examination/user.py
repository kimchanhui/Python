from receipt import *
from globalVariable import *

#===================================
#===================================

def signup() :
    user_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/user2.txt', 'a')

    name = input('이름 : ')
    id = input('아이디 : ')
    pw = input(('패스워드 : '))

    data = (f'{name} {id} {pw} 0\n')
    user_txt2.write(data)

    user_txt2.close()

    print('생성 완료')
    print()

#===================================
#===================================

def login() :
    user_id = input('아이디 : ')
    user_pw = input('패스워드 : ')

    for i in list :
        i.get('id'), i.get('pw'), i.get('user_name')

        if i.get('id') == user_id and i.get('pw') == user_pw :
            print('로그인 성공')
            print()
            user_name = i.get('user_name')
            return user_name
            print()
            break
    print('로그인 실패')
    print('처음으로 돌아갑니다.')
    check = 'no'
    return check
    print()

#===================================
#===================================

def user_info(username) :
    for i in list :
        i.get('user_name')
        if i.get('user_name') == username :
            id = i.get('id')
            name = i.get('user_name')
            mileage = i.get('mileage')
            print('아이디 :' ,id)
            print('이름 :' ,name)
            print('마일리지 :' ,mileage)
            print()
    print()




