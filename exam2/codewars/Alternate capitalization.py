def capitalize(s):
    even = []
    odd = []
    
    
    for i in range(len(s)):
        if i % 2 ==0:
            even.append(s[i].upper())
            odd.append(s[i])
            
        else:
            even.append(s[i])
            odd.append(s[i].upper())
            
            
    all_even = "".join(even)
    all_odd = "".join(odd)
    
    return [all_even,all_odd]