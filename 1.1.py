list  = [1,8,13,15,27,33,37,45,60]
search = 3
f_ind = 0
l_ind = len(list) - 1

def bin_search(f_ind , l_ind , search , list ):
    if l_ind >= f_ind:
        mid_ind = (f_ind + l_ind )//2
        mid_num = list[mid_ind]
        if mid_num < search:
            return bin_search(mid_ind + 1 , l_ind , search , list )
        elif mid_num > search:
            return bin_search(f_ind , mid_ind - 1 , search , list )
        elif mid_num == search:
            return f"{mid_num} находится на позиции {mid_ind}"
    else:
        return f"{search} нет в списке"
print(bin_search(f_ind , l_ind , search , list ))