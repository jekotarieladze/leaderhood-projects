def divisible_by(numbers, divisor):
    answer = []
    
    for I in numbers:
        if I % divisor == 0:
            answer.append(I)
            
    return answer