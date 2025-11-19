def odd_even(a):
    if a % 2 == 0:
        return 'Even Number'
    elif a % 2 == 1:
        return 'Odd Number'
    else:
        return 'Sth Else'
    
print(odd_even(45))