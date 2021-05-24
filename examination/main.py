list = []

user_txt1 = open('C:/Users/DOONA/PycharmProjects/Python/김찬희_중간고사/user.txt', 'r')
line1 = user_txt1.readline()
list1 = line1
user_txt1.close()

user_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/김찬희_중간고사/user2.txt', 'r')

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

def login(user_id, user_pw) :
    for i in list :
        i.get('id'), i.get('pw')

        while i.get('id') == user_id :
            if i.get('pw') == user_pw :
                print('로그인 성공')
                print()
                user_name = i.get('user_name')

                return user_name
                break
            else:
                print('패스워드가 다릅니다.')
                a = 1
                break
        if a == 1 :
            break
        else:
            print('없는 아이디 입니다.')

#===================================
#===================================

def user_info(userid, userpw) :
    for i in list :
        i.get('id')
        if i.get('id') == userid and i.get('pw') == userpw :
            print('아이디 :' ,i.get('id'))
            print('이름 :' ,i.get('user_name'))
            print('마일리지 :' ,i.get('mileage'))
    print()

#===================================
#===================================

p_list = []

prod_txt1 = open('C:/Users/DOONA/PycharmProjects/Python/김찬희_중간고사/product.txt', 'r')
p_line1 = prod_txt1.readline()
p_list1 = p_line1
prod_txt1.close()

prod_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/김찬희_중간고사/product2.txt', 'r')

while True :
    p_line2 = prod_txt2.readline()
    if not p_line2 :
        break
    p_list2 = p_line2
    p_dic = {x: y for x, y in zip(p_list1.split(), p_list2.split())}
    p_list.append(p_dic)
prod_txt2.close()

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


if __name__ == '__main__' :
    command = ''
    while command != 'exit' :
        print('Command ( shopping ), ( login ), ( exit )')
        command = input()
        if command == 'shopping' :
            product_info()


        elif command == 'login' :
            user_id = input('아이디 : ')
            user_pw = input('패스워드 : ')
            user_name = login(user_id, user_pw)

            for i in list :
                if i.get('user_name') == user_name :
                    print(f'{user_name}님 환영합니다.')
                    break

            command1 = ''
            while command1 != 'exit' :
                print('Command ( shopping ), ( exit = logout ), ( info )')
                command1 = input()

                if command1 == 'shopping' :
                    print()

                elif command1 == 'info':
                    user_info(userid=user_id, userpw=user_pw)

                elif command1 == 'exit':
                    print('처음으로 돌아갑니다.')
                    print()
                    break

                else :
                    print('없는 커맨드 입니다.')
                    print()

        else:
            print('없는 커맨드 입니다.')
            print()












