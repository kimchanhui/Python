def multiple() :
    print()

def divisor(num1, num2) :
    if num1 < num2 :
        min = num1
    else:
        min = num2

    for i in range(min + 1, 1, -1) :
        if num1 % i == 0 and num2 % i == 0 :
            res = i
            break
            return res









if __name__ == '__main__':
    input(divisor(num1 = int(input('숫자1 : ')), num2 = int(input('숫자1 : '))))