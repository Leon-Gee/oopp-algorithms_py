import random


def bubble_sort(elements):
    n = len(elements)

    for i in range(n):
        for j in range(0 , (n - i) - 1):
             if elements[j] > elements[j + 1]:
                    elements[j], elements[j + 1 ] = elements[j + 1], elements[j]
    
    return elements
                    


if __name__ == '__main__':
    list_size = int(input('how big is your list buddy? '))

    elements = [random.randint(0,100) for i in range(list_size)]

    print(elements)

    ordered_elements = bubble_sort(elements)
    
    print(ordered_elements)
