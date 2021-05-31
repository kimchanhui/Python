
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

#================================================
#================================================
#================================================

p_list = []

prod_txt1 = open('C:/Users/DOONA/PycharmProjects/Python/examination/product.txt', 'r')
p_line1 = prod_txt1.readline()
p_list1 = p_line1
prod_txt1.close()

prod_txt2 = open('C:/Users/DOONA/PycharmProjects/Python/examination/product2.txt', 'r')

while True :
    p_line2 = prod_txt2.readline()
    if not p_line2 :
        break
    p_list2 = p_line2
    p_dic = {x: y for x, y in zip(p_list1.split(), p_list2.split())}
    p_list.append(p_dic)
prod_txt2.close()



#================================================
#================================================
#================================================












