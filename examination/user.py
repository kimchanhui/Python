list = []

user_txt1 = open('C:/Users/DOONA/PycharmProjects/Python/examination/user.txt', 'r')
line1 = user_txt1.readline()
list1 = line1
user_txt1.close()

user_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/user2.txt', 'r')

while True :
    line2 = user_txt2.readline()
    if not line2 :
        break
    list2 = line2
    dic = {x: y for x, y in zip(list1.split(), list2.split())}
    list.append(dic)
user_txt2.close()

#===================================
#===================================

def signup() :
    user_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/user2.txt', 'a')

    name = input('이름 : ')
    id = input('아이디 : ')
    pw = input(('패스워드 : '))

    data = (f'\n{name} {id} {pw} 0')
    user_txt2.write(data)

    user_txt2.close()

#===================================
#===================================

def login() :
    user_id = input('아이디 : ')
    user_pw = input('패스워드 : ')

    for i in list :
        i.get('id'), i.get('pw')

        if i.get('id') == user_id and i.get('pw') == user_pw :
            print('로그인 성공')
            print()
            return i.get('user_name')
            print()
            break
    print('로그인 실패')
    print('처음으로 돌아갑니다.')
    check = 1
    return check
    print()

#===================================
#===================================

def user_info(username) :
    for i in list :
        i.get('user_name')
        if i.get('user_name') == username :
            print('아이디 :' ,i.get('id'))
            print('이름 :' ,i.get('user_name'))
            print('마일리지 :' ,i.get('mileage'))




    print()


