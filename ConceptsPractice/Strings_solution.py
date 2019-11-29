#modify the following string variable to add a period to the end of it
string1 = 'The cow jumped over the moon'
string1 = string1 + '.'
print (string1)

#Set string2 to have the word cow # (Use slicing to get it out of string1).
string2 = string1[4:7]
print (string2)

#Set string3 to have the word moon # (Use slicing to get it out of string1).
string3 = string1[-5:-1]
print (string3)

#Create a list of words out of string1 (hint, see the split() method in the documentation)
list_of_words = string1.split()
print (list_of_words)

#Use .format() to fill in the missing values that it will take to make this print out the sentence
#'the cow jumped over the moon'
print('The {0} jumped over the {1}'.format('cow','moon'))

#Repeat the above, but this time use %s instead of .format()
print('The %s jumped over the %s'%('cow','moon'))

#set the string_count variable to count the number of characters in string1
#(find a built in string method to do this)
string_count = len(string1)