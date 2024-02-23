def dayxahoi(lst):
    for i in range(1,n+1):
        lst.append(i)
def selection_sort(nums):  
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[lowest_value_index] < nums[j]  :
                j = lowest_value_index
        nums[lowest_value_index], nums[i] = nums[i], nums[lowest_value_index]
n = int(input())
lst = [] 
if __name__ == "__main__":
    print(dayxahoi(lst))
