# 출전자 중에서 완주하지 못한 사람을 출력
# 완주자 수는 출전자 수의 -1명임
# 동명이인이 있을 수 있음

import collections

def solution(p, c) :
    answer = collections.Counter(p) - collections.Counter(c)  # 다른 사람 코드임
    return print(list(answer.keys())[0])                      # 카운터 객체 끼리 뺄 수 있는걸 앎

if __name__ == '__main__' :
    solution(p=["leo", "kiki", "eden"], c=["eden", "kiki"])


 # Python/modules/Collection-Counter.py