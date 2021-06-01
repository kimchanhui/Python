# 평균 구하기

def solution(arr) :
    total = 0
    for i in range(len(arr)) :
        total += arr[i]
    print(total/len(arr))


if __name__ == '__main__' :
    solution(arr=[1,2,3,4])