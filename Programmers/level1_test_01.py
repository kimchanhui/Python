# 문자열의 가운데 값 가져오기
# 짝수면 가운데 2개의 값 가져오기

def solution(s) :

    if len(s) % 2 == 1 :
        return print(s[len(s) // 2])
    else :
        return print(s[len(s) // 2 - 1 : len(s) // 2 + 1])
if __name__ == '__main__' :
    solution(str('abcdeg'))