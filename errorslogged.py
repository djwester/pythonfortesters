def addTwoNumbersTwice(num1,num2):
    '''This method adds two numbers together. 
    It then adds those two numbers together again and 
    then returns the sum of those sums.
    
    There is an error in the logic'''
    firstSum = num1 + num2
    secondSum = num1 + num1
    return firstSum + secondSum

addedNumbers = addTwoNumbersTwice(1,2)

#should equal 6
print (addedNumbers)