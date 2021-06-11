from random import *

words = ['apple', 'banana', 'orange']

word = choice(words)

def word_check() :
    life = 10
    count = 0
    save = ''

    while life > 0 :
        TF_Check = False
        Clear = True
        count += 1
        print()

        answer = input('입력 : ')
        if answer not in save :
            save += answer

        for i in word:
            if i in save:
                print(i, end=' ')
                TF_Check = True
            else:
                print('_', end=' ')
                Clear = False

        if TF_Check == False:
            life -= 1

        print()
        print(f'\n시도 횟수 : {count} 번')
        print(f'라이프 : {life}')
        print('\n===============')

        if Clear :
            print('\n성공')
            break

        if life == 0 :
            print('\n실패')




def start() :
    print('<---게임 시작--->')
    print()
    word_len = len(word)
    print('_' * word_len, f'// {word_len}칸')
    print()
    print('===============')
    word_check()






if __name__ == '__main__':
    start()