def parts_sums(ls):
    result = []
    curent_sum = 0
    
    for i in reversed(ls):
        curent_sum += i
        result.append(curent_sum)
        
    result.append(0)
    result.reverse()
    return result