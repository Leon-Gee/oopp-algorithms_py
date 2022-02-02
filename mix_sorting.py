import random

def mix_sorting(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid]

        #recursive call in each half

        mix_sorting(left)
        mix_sorting(right)

        #iterators sublists
        #left
        i = 0
        #right
        j = 0
        
        #main list iterator

        k=0
    
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                nums[k] = left[i]
                i +=1

            else:
                nums[k] = right[j]
                j +=1
            
            k += 1
                

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    return nums


if __name__ == '__main__':
    list_size = int(input('How big is your list?'))

    nums = [random.randint(1,100) for i in range(list_size)]
    print(nums)
    print('-'*20)

    sorted_nums = mix_sorting(nums.copy())
    print(sorted_nums)
