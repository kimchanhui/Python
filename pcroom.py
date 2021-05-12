def pcroom():
    userinfo = [
        {'name': '돈 많은 백수', 'time_h': 600, 'time_m': 0}
    ]

    for i in userinfo:
        i.get('name')

        # 현재 시간
        print('\n현재 시간')
        h = int(input('현재 시간 = 시 : '))
        if h < 24:
            m = int(input('현재시간 = 분 : '))
            if m > 59:
                print('60 미만의 숫자를 입력해주세요.')
        else:
            print('24 미만의 숫자를 입력해주세요.')
            break
        # 현재 시간

        # 사용자 정보 생성
        name = input('이름 : ')
        if name != i.get('name'):
            YN1 = input('없는 사용자 입니다. 추가 하시겠습니까? (네 : 아니요) : ')
            if YN1 == '네':
                userinfo.append({'name': name, 'time_h': 2, 'time_m': 0})
                for i in userinfo:
                    i.get('name')
                print('사용자 정보가 추가되었습니다.')
            # 사용자 정보 생성

            # 이용할 시간
            YN2 = input('바로 사용하시겠습니까? (네 : 아니요) : ')
            if YN2 == '네':

                usetime_h = int(input('사용하실 시간 = 시 : '))
                usetime_m = int(input('사용하실 시간 = 분 : '))
                if m > 59:
                    print('60 미만의 숫자를 입력해주세요.')
                # 이용할 시간

                # 이름, 이용 시간, 시작 시간, 종료시간
                print('')
                print('이름 :', i.get('name'))
                print(f'이용 시간 : {usetime_h} 시 {usetime_m} 분')
                print(f'시작 시간 : {h} 시 {m} 분')

                endtime_h = h + usetime_h

                while endtime_h >= 24:
                    endtime_h -= 24

                endtime_m = m + usetime_m
                if endtime_m >= 60:
                    endtime_m -= 60
                    endtime_h += 1
                    if endtime_h == 24 :
                        endtime_h = 0

                print(f'종료 시간 : {endtime_h} 시 {endtime_m} 분')
                # 이름, 이용 시간, 시작 시간, 종료시간

                # 초과 금액, 적립 시간
                savetime_h = i.get('time_h') - usetime_h

                if savetime_h > 0:
                    savetime_m = i.get('time_m') - usetime_m

                    if savetime_m < 0:
                        savetime_m = 60 - abs(savetime_m)
                        overamount_m = abs(savetime_m) * (1000 / 60)
                        savetime_h -= 1

                    elif savetime_m == 0:
                        overamount_m = abs(savetime_m) * (1000 / 60)

                    elif savetime_m > 0:
                        if savetime_m >= 60:
                            savetime_m -= 60
                            savetime_h += 1
                        overamount_m = abs(savetime_m) * (1000 / 60)

                    overamount_h = 1000 * abs(savetime_h)

                    print(f'초과 금액 : {-int(overamount_h) - int(overamount_m)} 원')
                    print(f'적립된 시간 : {savetime_h} 시 {savetime_m} 분')

                    # 리스트안에 딕셔너리  쓸때 값 변경 법 모르겠음

                elif savetime_h <= 0:
                    savetime_m = i.get('time_m') - usetime_m

                    if savetime_m < 0:
                        overamount_m = (1000 / 60) * abs(savetime_m)
                    elif savetime_m == 0:
                        overamount_m = 0

                    overamount_h = 1000 * abs(savetime_h)

                    print(f'초과 금액 : {int(overamount_h) + int(overamount_m)} 원')
                    print('적립된 시간 : 0시 0분')



            # 초과 금액, 적립 시간

            elif YN2 == '아니요':
                print('ㅂ')
                break

        # 나머지는 다같음

        elif name == i.get('name'):
            YN3 = input('사용하시겠습니까? (네 : 아니요) : ')
            if YN3 == '네':
                usetime_h = int(input('사용하실 시간 = 시 : '))
                usetime_m = int(input('사용하실 시간 = 분 : '))
                if m > 59:
                    print('60 미만의 숫자를 입력해주세요.')

                print('')
                print('이름 :', i.get('name'))
                print(f'이용 시간 : {usetime_h} 시 {usetime_m} 분')
                print(f'시작 시간 : {h} 시 {m} 분')

                endtime_h = h + usetime_h
                while endtime_h >= 24:
                    endtime_h -= 24

                endtime_m = m + usetime_m
                if endtime_m >= 60:
                    endtime_m -= 60
                    endtime_h += 1

                print(f'종료 시간 : {endtime_h} 시 {endtime_m} 분')

                savetime_h = i.get('time_h') - usetime_h

                if savetime_h > 0:
                    savetime_m = i.get('time_m') - usetime_m

                    if savetime_m < 0:
                        savetime_m = 60 - abs(savetime_m)
                        overamount_m = abs(savetime_m) * (1000 / 60)
                        savetime_h -= 1

                    elif savetime_m == 0:
                        overamount_m = abs(savetime_m) * (1000 / 60)

                    elif savetime_m > 0:
                        if savetime_m >= 60:
                            savetime_m -= 60
                            savetime_h += 1
                        overamount_m = abs(savetime_m) * (1000 / 60)

                    overamount_h = 1000 * abs(savetime_h)

                    print(f'초과 금액 : {-int(overamount_h) - int(overamount_m)} 원')
                    print(f'적립된 시간 : {savetime_h} 시 {savetime_m} 분')

                    # 리스트안에 딕셔너리  쓸때 값 변경 법 모르겠음

                elif savetime_h <= 0:
                    savetime_m = i.get('time_m') - usetime_m

                    if savetime_m < 0:
                        overamount_m = (1000 / 60) * abs(savetime_m)
                    elif savetime_m == 0:
                        overamount_m = 0

                    overamount_h = 1000 * abs(savetime_h)

                    print(f'초과 금액 : {int(overamount_h) + int(overamount_m)} 원')
                    print('적립된 시간 : 0시 0분')

            # 나머지는 다같음


if __name__ == '__main__':
    pcroom()