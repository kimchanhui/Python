
    # 딕셔너리를 이용한 카운팅

def countLetters(word) :
    counter = {}
    for letter in word:
        if letter not in counter :
            counter[letter] = 0
        counter[letter] += 1
    return counter

countLetters('hello world')

    # collections모듈의 Counter클래스 사용
from collections import Counter

Counter('hello world')




