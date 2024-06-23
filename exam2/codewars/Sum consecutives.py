def sum_consecutives(lst):
    result = []
    C_sum = lst[0]
    L_num = lst[0]
    
    for i in lst[1:]:
        if i == L_num:
            C_sum += i
            
        else:
            result.append(C_sum)
            L_num = i
            C_sum = i
        
    result.append(C_sum)
    return result