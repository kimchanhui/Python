from datetime import datetime
from user import *
from globalVariable import *

r_list = []

receipt_txt1 = open('C:/Users/DOONA/PycharmProjects/Python/examination/receipt.txt', 'r')
r_line1 = receipt_txt1.readline()
r_list1 = r_line1
receipt_txt1.close()

receipt_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/receipt2.txt', 'r')

while True :
    r_line2 = receipt_txt2.readline()
    if not r_line2 :
        break
    r_list2 = r_line2
    r_dic = {x: y for x, y in zip(r_list1.split(), r_list2.split())}
    r_list.append(r_dic)
receipt_txt2.close()

def receipt(user_name,total, quantity, price, p_name) :
    receipt_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/receipt2.txt', 'a')

    date = datetime.today().strftime('%Y/%m/%d')

    add_mile = total * 0.03

    for i in list :
        i.get('id'), i.get('pw'), i.get('user_name')
        if user_name == i.get('user_name') :
            mileage = int(i.get('mileage'))
            break

    mileage += add_mile

    data = (f'{user_name} {date} {p_name} {total} {quantity} {int(add_mile)} {int(mileage)}')
    receipt_txt2.write(data)

    receipt_txt2.close()










