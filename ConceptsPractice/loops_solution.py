#Use a loop to make list2 have values that are one more than the
#values in list1 (i.e. list2 should be [2,3,4])
list1 = [1,2,3]
list2 = []
for item in list1:
    list2.append(item+1)

#use a loop to print out the numbers 1-5 multiplied by themselves
#(i.e. it should print out 1, 4, 9, 16, and 25)
for i in range(1,6):
    print (i*i)

#use list1 and list2 above and put the values of adding each of the 
#items in those list together into a third list (i.e. list3 should be [3,5,7]
# since 1+2=3, 2+3=5 and 3+4=7) - use a loop and the zip function.
list3 = []
for item1, item2 in zip(list1,list2):
    list3.append(item1+item2)

#Further learning resources:
#https://data36.com/python-for-loops-explained-data-science-basics-5/
#https://realpython.com/python-for-loop/