# 3이면 수박수
# 4이면 수박수박

def solution(n) :
    wm = ''
    for i in range(n) :
        if i % 2 == 0 :
            wm += '수'
        else :
            wm += '박'
    return print(wm)


if __name__ == '__main__' :
    solution(n=4)