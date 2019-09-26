import random
#Test data types
strings = ['a','b']
integers = [1,2]
floats = [0.1,0.2]
numbers = integers + floats

#ask the user for the type of input they want
input_type = input("What type of data do you want (string, integer, float or number)?\n>")

if  input_type == 'string':
    #get a random item from the list
    print (random.choice(strings))
elif input_type == 'integer':
    print (random.choice(integers))
elif input_type == 'float':
    print (random.choice(floats))
elif input_type =='number':
    print (random.choice(numbers))
else:
    print("Did not recognize that data type. Rerun the program to try again.")

