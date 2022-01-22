import random

def binary_search(elements, start, final,objective):
    
    if start > final:
        return False

    mid = (start + final) // 2
    
    if elements[mid] == objective:
        return True
    elif elements[mid] < objective:
        return binary_search(elements, mid + 1, final, objective)
    else:
       return binary_search(elements, start, mid, objective)
        


if __name__ == '__main__':
    
    list_size = int(input('how big is your list? ' ))

    objective = int(input('which number you wich to find? '))

    num_list = sorted([random.randint(0,list_size) for i in range(list_size)])

    match = binary_search(num_list, 0, len(num_list), objective)

    print(num_list)

    print(f'The element {objective} {" is " if match else " is not "} in the list')
