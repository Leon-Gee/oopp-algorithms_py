import time

def factorial(num):
    answer = 1

    while num > 1:
        answer *= num
        num -= 1
    
    return answer


def factorial_r(num):
    if num == 1:
        return 1

    return num * factorial(num-1)


if __name__ == '__main__':
    num = 1000

    start = time.time()
    
    factorial(num)
    
    final = time.time()

    print(final - start)

    start = time.time()

    factorial_r(num)

    final = time.time()

    print(final - start)

