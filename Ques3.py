def convert_temperature():
    temp = float(input('Enter temperature: '))
    scale = input('Enter desired scale in Celsius (C) or Fahrenheit (F): ')
    
    if scale.upper() == 'C':
        temp_converted = (temp - 32) * 5.0 / 9.0
        print('Temperature in Celsius is:', temp_converted )
    elif scale.upper() == 'F':
        temp_converted  = (temp * 9.0 / 5.0) + 32
        print('Temperature in Fahrenheit is:', temp_converted )
    else:
        print("Invalid format for temperature scale.")
        return None
    
    return converted_temp

converted_temp = convert_temperature()
