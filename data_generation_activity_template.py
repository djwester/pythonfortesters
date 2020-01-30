naughty_string_list = ['!@#$%^&*()','1;DROP TABLE users']
dangerous_float_list = [1.0,0.01]
interesting_int_list = [-1,0,1]
interesting_number_list = dangerous_float_list + interesting_int_list

type_of_data = input('What type of data would you like (string, float, integer or number)? \n>')

import random
if type_of_data == 'string':
    print (<pick an item from the string list>)
elif type_of_data == 'float': #repeat for each of the other data types
    
else:
    print ("could not recognize the data type %s. Please try again."%type_of_data)