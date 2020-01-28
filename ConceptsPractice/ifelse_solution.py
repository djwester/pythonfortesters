#Set the value of my_boolean below so that the code below will print
#out the statement 'in if'
my_boolean = True
if my_boolean:
    print('in if')
else:
    print ('in else')

# repeat the above code, but this time set the value of my_boolean so 
#that it will print out the statement 'in else'
my_boolean = False
if my_boolean:
    print('in if')
else:
    print ('in else')

#Use an if statement to create a code branch that will only be 
#executed if a given variable value is greater than 1
if my_variable > 1:
    print ('hi!')

#Create code that will print out 'Greater than 1' if a given variable
#value is greater than one and that will print out 'Less than 1' if 
#the value is less than one and that will print out 'One!' if the value
#is equal to one
if my_variable > 1:
    print ('Greater than 1')
elif my_variable < 1:
    print ('Less than 1')
else:
    print ('One!')

#Create code that will only be executed if a given variable value is
#between 0 and 10
if my_variable > 0 and my_variable < 10:
    print ('between 0 and 10')

#create code that will only be executed if a given variable value is
#less than 0 or greater than 10
if my_variable < 0 or my_variable > 10:
    print ('not between 0 and 10')

#Further learning resources:
#https://realpython.com/python-conditional-statements/
#https://www.w3schools.com/python/python_conditions.asp
