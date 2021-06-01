import collections

def solution(p, c) :
    answer = collections.Counter(p) - collections.Counter(c)  # 다른 사람 코드임
    return print(list(answer.keys())[0])                      # 카운터 객체 끼리 뺄 수 있음

if __name__ == '__main__' :
    solution(p=["leo", "kiki", "eden"], c=["eden", "kiki"])