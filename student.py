def student():
    student = [
        {'name' : 'AAA', 'type' : 'N', 'time' : 10},
        {'name' : 'BBB', 'type' : 'Y', 'time' : 8},
        {'name' : 'CCC', 'type' : 'N', 'time' : 8}
    ]

    timeout = 0
    dis = 0
    notdis = 0

    for i in student:
        if i.get('time') > 9:
            timeout += 1
        if i.get('type') == 'Y':
            dis += 1
        else :
            notdis += 1

    print(f'장애인 : {dis}')
    print(f'일반인 : {notdis}')
    print(f'총 출석 수 : {len(i)}')
    print(f'출석한 사람 중 지각 : {timeout}')
    print(f'결석 수 : {5-len(i)}')


if __name__ == '__main__':
    student()