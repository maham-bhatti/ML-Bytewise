def max_min(number_list):
    max_nm = max(number_list)
    min_nm = min(number_list)
    return max_nm, min_nm

def nums():
    number = []
    for i in range(5):
        numb = float(input("Enter number: " ))
        number.append(numb)
    return number

number = nums()
max_nm, min_nm = max_min(number)
print("The maximum number is:", max_nm)
print("The minimum number is:", min_nm)
