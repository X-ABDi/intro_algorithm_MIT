def count_long_subarrays(t):
    max_length = 1
    temp_length = 1
    count = 1
    current_num = 0
    previous_num = None
    if len(t) == 0:
        return 0
    for i in t:
        current_num = i
        if previous_num == None:
            previous_num = i
            continue
        if current_num > previous_num:
            temp_length += 1
            if temp_length > max_length:
                max_length = temp_length
                count = 1
            elif temp_length == max_length:
                count += 1
        else:
            temp_length = 1    
        previous_num = current_num 
        
    return count               

def main ():
    t1 = (1, 2, 5, 2, 4, 5, 7, 8, 9, 3, 5, 6)
    t2 = (2, 5, 3, 6, 3, 7, 4, 8, 7, 9, 1, 3)
    count = count_long_subarrays(t2)
    print("count: ", count)

main ()