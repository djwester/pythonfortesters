def printWelcomeString(name = '', greeting = '', title = ''):
    '''prints out a personalized welcome that includes
    the user's full name and a greeting message. 
    
    There is a logic error in here. You may want to add print statements
    to help figure out what is going on'''
    
    #name and greeting are optional.
    #Set defaults in case the caller doesn't enter them 
    if not greeting:
        greeting = 'Hi'
    else:
        name = 'Anonymous'
    welcome_string = '%s %s %s!'%(greeting, title, name)

    print(welcome_string)

#should print out "Hello Mrs. Janet Jackson!", but it does not. 
printWelcomeString(name = 'Janet Jackson', greeting = 'Hello', title = 'Mrs.')