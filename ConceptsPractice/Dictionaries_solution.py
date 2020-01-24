#Assign the value 'hello' to the key 'beginning' in the following dictionary
messages = {}
messages['beginning'] = 'hello'

#Assign the value 'good-bye' to the key 'ending' in the same dictionary
messages['ending'] = 'good-bye'

#print the value of the key 'beginning' from the dictionary
print(messages['beginning'])

#print out the keys of the following dictionary (use a loop)
d = {1:'a',2:'b',3:'c'}

for key in d.keys():
    print (key)

#print out the values of the previous dictionary (using a loop)
for value in d.values():
    print (value)
    
#Further learning resources:
# https://realpython.com/python-dicts/
# https://www.dataquest.io/blog/python-dictionary-tutorial/
