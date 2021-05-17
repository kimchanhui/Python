def attendance():
    print('출근')

    print('8시 알람!')

    current_time = 0

    while current_time <= 541 :
        current_time = 480

        YN1 = input('일어남? (Y/N) : ')
        if YN1 == 'Y' :
            print('')
        else :
            print('10분뒤 알람')

            current_time += 10

            YN2 = input('일어남? (Y/N) : ')
            if YN2 == 'N' :
                print('지각')
                break
            else:
                print()
        YN3 = input('씻? (Y/N) : ')
        if YN3 == 'Y' :
            current_time += 10

        else:
            print('윽.. 더러워')

        YN4 = input('교통수단? (버스/지하철 : 1, 택시 : 2) : ')
        if YN4 == '1' :
            print('버스/지하철 40분')
            current_time += 40

        elif YN4 == '2' :
            print('택시 20분')
            current_time += 20

        print('회사건물 도착')

        YN5 = input('엘레베이터? (Y/N) : ')
        if YN5 == 'Y' :
            print('엘레베이터 3분')
            current_time += 3
        else :
            print('계단 5분')
            current_time += 5

        print('사무실 도착')

        print(f'현재 시간 : {int(current_time / 60)} 시 {current_time % 60} 분')
        cum_time = current_time - 480
        print(f'누적 시간 : {int(cum_time / 60)} 시 {cum_time % 60} 분')

    print('그랜절')
    print(f'현재 시간 : {int(current_time / 60)} 시 {current_time % 60} 분')
    cum_time = current_time - 480
    print(f'누적 시간 : {int(cum_time / 60)} 시 {cum_time % 60} 분')



if __name__ == '__main__':
    attendance()