def dig_pow(n, p):
    
    num = 0
    for num in str(n):
        num += int(num) ** p
        p += 1
    
    if num % n == 0:
        return int(num % n)
    else:
        return -1
    