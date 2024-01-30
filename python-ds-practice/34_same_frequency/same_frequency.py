def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str_num1 = str(num1)
    str_num2 = str(num2)

    
    if len(str_num1) != len(str_num2):
        return False

    
    freq_num1 = {}
    for digit in str_num1:
        freq_num1[digit] = freq_num1.get(digit, 0) + 1

    
    for digit in str_num2:
        if digit not in freq_num1 or freq_num1[digit] == 0:
            return False
        freq_num1[digit] -= 1

    return True