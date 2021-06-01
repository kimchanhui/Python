
    # 영화 리스트(이름, 시간, 지역)
    # 좌석 리스트(등급, 금액)
    # 커플석 조건 2명이상
    # 고객 정보, 장애인 할인
    # 영수증 출력


def Movie_Theater(areaChoice):

    if areaChoice == '1' :
        area = '서울'
        print(f'{area}을/를 선택하셨습니다.\n')
        return area

    elif areaChoice == '2' :
        area = '인천'
        print(f'{area}을/를 선택하셨습니다.\n')
        return area

    elif areaChoice == '3' :
        area = '경기'
        print(f'{area}을/를 선택하셨습니다.\n')
        return area

    else:
        print('선택한 지역이 목록에 없습니다.\n')
        print()

#=====================================
#=====================================

def MovieList(movieChoice):
    movie_list = [
        {'no' : 1 ,'name' : '아이언맨'},
        {'no' : 2 ,'name' : '토르'}
    ]

    for i in movie_list:
        i
        if i.get('no') == movieChoice:
            break

    if movieChoice == i.get('no') :
        movie = i.get('name')
        return movie

    else:
        print('선택한 영화가 목록에 없습니다.')
        print('처음으로 돌아갑니다.\n')
        print()

#=====================================
#=====================================

def Movie_Time_Search(timeSearch):
    movie_time = [
        {'no' : 1 ,'name' : '아이언맨', 'time_h' : 9, 'time_m' : 30},
        {'no' : 2 ,'name' : '아이언맨', 'time_h' : 12, 'time_m' : 0},
        {'no' : 1 ,'name' : '토르', 'time_h': 13, 'time_m': 0},
        {'no' : 2 ,'name' : '토르', 'time_h': 16, 'time_m': 20}
    ]

    timelist = timeSearch

    for i in movie_time :
        i.get('name')
        if i.get('name') == timelist:
            print(i.get('time_h'),'시',i.get('time_m'),'분 :',i.get('no'))

    return timelist

def Movie_Time_Choice(timeSearch,timeChoice) :
    movie_time = [
        {'no': 1, 'name': '아이언맨', 'time_h': 9, 'time_m': 30},
        {'no': 2, 'name': '아이언맨', 'time_h': 12, 'time_m': 0},
        {'no': 1, 'name': '토르', 'time_h': 13, 'time_m': 0},
        {'no': 2, 'name': '토르', 'time_h': 16, 'time_m': 20}
    ]

    timelist = timeSearch

    timechoice = timeChoice

    for i in movie_time:
        i.get('name')
        if i.get('name') == timelist:
            if i.get('no') == timechoice:
                print('선택된 시간 : ',i.get('time_h'),'시',i.get('time_m'),'분')

    return timechoice

#=====================================
#=====================================

def Seat_Search(movieNo, movieName) :
    seat_list = [
        {'no' : 1, 'name' : '아이언맨', 'S' : 5, 'A' : 10, 'B' : 15, 'couple' : 5},
        {'no' : 2, 'name' : '아이언맨', 'S' : 5, 'A' : 10, 'B' : 15, 'couple' : 5},
        {'no' : 1, 'name' : '토르', 'S' : 5, 'A' : 10, 'B' : 15, 'couple' : 5},
        {'no' : 2, 'name' : '토르', 'S' : 5, 'A' : 10, 'B' : 15, 'couple' : 5}
    ]

    movieno = movieNo
    moviename = movieName

    for i in seat_list :
        i.get('no'), i.get('name')
        if i.get('no') == movieno and i.get('name') == moviename:
            print('S :', i.get('S'), '석,', 'A :', i.get('A'), '석,', 'B :', i.get('B'), '석,', 'Couple :', i.get('couple'), '석')


    print()


def Seat_Price() :
    seat_pricc = [
        {'no' : 1, 'class' : 'S', 'price' : 10000},
        {'no' : 2, 'class' : 'A', 'price' : 8000},
        {'no' : 3, 'class' : 'B', 'price' : 6000},
        {'no' : 4, 'class' : 'Couple', 'price' : 16000}
    ]

    for i in seat_pricc :
        i.get('no'), i.get('price')
        print(i.get('class'), ':', i.get('price'), '원')

    print()

def Seat_Choice(seatNo, personnel) :
    seat_list = [
        {'no': 1, 'name': '아이언맨', 'S': 5, 'A': 10, 'B': 15, 'couple': 5},
        {'no': 2, 'name': '아이언맨', 'S': 5, 'A': 10, 'B': 15, 'couple': 5},
        {'no': 1, 'name': '토르', 'S': 5, 'A': 10, 'B': 15, 'couple': 5},
        {'no': 2, 'name': '토르', 'S': 5, 'A': 10, 'B': 15, 'couple': 5}
    ]

    seat_pricc = [
        {'no': 1, 'class': 'S', 'price': 10000},
        {'no': 2, 'class': 'A', 'price': 8000},
        {'no': 3, 'class': 'B', 'price': 6000},
        {'no': 4, 'class': 'Couple', 'price': 16000}
    ]

    seatno = seatNo
    person = personnel

    for i in seat_pricc :
        i.get('no')
        if i.get('no') == seatno :
            print(i.get(''))


    print()
# =====================================
# =====================================

def Movie():
    while True:

        #----지역 선택----

        print('지역 선택')
        print('서울 : 1, 인천 : 2, 경기 : 3')

        movie_theater = Movie_Theater(areaChoice=input('선택 : '))

        if movie_theater == '서울' or movie_theater == '인천' or movie_theater == '경기' :
            print(f'{movie_theater} 영화관\n')

        else:
            continue

        #----인원 입력----

        print('인원 입력')

        persons = int(input('인원 수 : '))
        print()

        #----영화 선택----

        print('영화 선택')
        print('아이언맨 : 1, 토르 : 2')

        movie_choice = MovieList(movieChoice=int(input('선택 : ')))

        if movie_choice == '아이언맨' :
            #----선택 영화 상영 시간----
            print(f'선택 영화 : {movie_choice}\n')

            print('상영 시간표')
            Movie_Time_Search(timeSearch=movie_choice)
            time_choice = Movie_Time_Choice(timeSearch=movie_choice, timeChoice=int(input('선택 : ')))

            print()

            print('남은 좌석 및 가격')
            Seat_Search(movieNo=time_choice, movieName=movie_choice)
            Seat_Price()

            print('S : 1, A : 2, B : 3, Couple : 4')
            seat_choice = input('좌석 선택 : ')

            Seat_Choice(seatNo=seat_choice)



        elif movie_choice == '토르':
            # ----선택 영화 상영 시간----
            print(f'선택 영화 : {movie_choice}\n')

            print('상영 시간표')
            Movie_Time_Search(timeSearch=movie_choice)
            time_choice = Movie_Time_Choice(timeSearch=movie_choice, timeChoice=int(input('선택 : ')))

            print()

            print('남은 좌석 및 가격(커플석은 2인만 가능)')
            Seat_Search(movieNo=time_choice, movieName=movie_choice)
            Seat_Price()

            if persons == 2 :
                print('S : 1, A : 2, B : 3, Couple : 4')
                seat_choice = input('좌석 선택 : ')
                Seat_Choice(seatNo=seat_choice)

            else :
                print('S : 1, A : 2, B : 3')
                seat_choice = input('좌석 선택 : ')

        else:
            continue









if __name__ == '__main__':
    Movie()