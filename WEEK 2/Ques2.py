
def is_even_num(num):
    if num % 2 == 0:
        print('Entered num', num, 'is even.')
        return True    
    else:
        print('Entered num', num, 'is odd.')
        return False
        
result = is_even_num(7)
print(result)

result = is_even_num(2)
print(result)