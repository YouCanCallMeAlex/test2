list  = [1,4,7,2,5,8,3,6,9,0]
def ins_sort(list):
    len_list = len(list)
    for i in range(1, len_list):
        ref_value = list[i]
        x = i
        while x>0 and list[x-1] > ref_value:
            list[x] = list[x-1]
            x -= 1 
        else:
            list[x] = ref_value
    return f'list sorted {list}'


print(ins_sort(list))