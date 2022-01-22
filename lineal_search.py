import random

def lineal_search(num_list, objective):

    match = False

    for element in num_list:
        if element == objective:
            match = True
            break
        else:
            continue

    return match


if __name__ == '__main__':
    
    list_size = int(input('how big is your list? ' ))

    objective = int(input('which number you wich to find? '))

    num_list = [random.randint(0,100) for i in range(list_size)]

    match = lineal_search(num_list, objective = objective)

    print(num_list)

    print(f'The element {objective} {" is " if match else " is not "} in the list')
