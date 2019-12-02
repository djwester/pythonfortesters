#append 6 to the end of this list
list1 = [1,2,3,4,5]
list1.append(6)
print(list1)

#What is the index of the number 3 in List1?
print (list1.index(3))

#Sort this list
list2 = ['b','d','c','e','a']
list2.sort()
print(list2)

#Use slicing to get [2,3,4] out of this list 
list3 = [1,2,3,4,5]
my_slice = list3[1:4]
print(my_slice)
#find the sum of all items in list 3. (Hint: look up sum() in the python
# documentation)
print(sum(list3))

#what number is at index -1 in list3?
print(list3[-1])