#Write a function (call it my_sum) that takes in two arguments and returns the sum of them
def my_sum(number1, number2):
    return sum(number1,number2)

#Modify the above function to use named parameters for the input arguments
def my_sum (number1=0, number2=0):
    return sum(number1,number2)

#Write a function (call it my_square) that take in a number and squares it (i.e. returns number**2)
def my_square(number):
    return number**2

#Write a function called sum_of_squares that takes in two numbers and returns the sum 
#of their squares (i.e. squares the numbers and then adds those squares together). Use 
#the other two functions you have already created
def sum_of_squares(number1,number2):
    square1 = my_square(number1)
    square2 = my_square(number2)
    return my_sum(square1,square2)
    
#Further learning resources:
#https://www.learnpython.org/en/Functions
#https://www.w3schools.com/python/python_functions.asp
