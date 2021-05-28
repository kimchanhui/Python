from datetime import datetime
from user import *
from globalVariable import *

r_list = []

receipt_txt1 = open('C:/Users/DOONA/PycharmProjects/Python/examination/receipt.txt', 'r')
r_line1 = receipt_txt1.readline()
r_list1 = r_line1
receipt_txt1.close()

receipt_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/receipt2.txt', 'r',encoding='utf-8')

while True :
    r_line2 = receipt_txt2.readline()
    if not r_line2 :
        break
    r_list2 = r_line2
    r_dic = {x: y for x, y in zip(r_list1.split(), r_list2.split())}
    r_list.append(r_dic)
receipt_txt2.close()

def receipt(user_name,total, quantity, price, p_name) :
    receipt_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/receipt2.txt', 'a',encoding='utf-8')

    date = datetime.today().strftime('%Y/%m/%d-%H시%M분%S초')

    if user_name == 'None' :
        add_mile = 0
        add_mileage = 0

    add_mile = total * 0.03


    for i in list :
        i.get('id'), i.get('pw'), i.get('user_name')
        if user_name == i.get('user_name') :
            add_mileage = int(i.get('mileage'))
            mileage = i.get('mileage')
            id = i.get('id')
            pw = i.get('pw')
            break


    add_mileage += int(add_mile)
    if total != 0 :
        data = (f'{user_name} {date} {p_name} {total} {quantity} {int(add_mile)} {int(add_mileage)}\n')
        receipt_txt2.write(data)

    receipt_txt2.close()
    if user_name != 'None' :
        print('---영수증---')
        print('구매자 :', user_name)
        print('구매 날짜 :', date)
        print('상품명 :', p_name)
        print('가격 :', total, '원')
        print('수량 :', quantity, '개')
        if user_name != 'None' :
            print('적립될 마일리지 :', int(add_mile))
            print('마일리지 :', int(add_mileage))





        user_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/user2.txt', 'r+')

        while True:
            line2 = user_txt2.readline()
            if user_name in line2:
                break

        user_txt2.close()

        data1 = line2.replace(str(mileage), str(add_mileage))
        data2 = '\n'

        user_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/user2.txt', 'w')


        user_txt2.write(data1)




        user_txt2.close()















