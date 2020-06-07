#ASSIGNING ELEMENTS TO DIFFERENT LISTS

#1.using append
list1 = [1,2,3]
list2 = ['python', 'learn']
list1.append(4)
print(list1)
list2.append(list1)
print(list2)

#2.using extend
list3 = ['a', 'b', 'c']
list4 = ['d', 'e']
list3.extend(list4)
print(list3)

#3.using sort
list5 = [4, 2, 6]
list5.sort()
print(list5)


#ACCESSING ELEMENTS FROM A TUPLE

tup1 = ('hello', 'world', 'welcome', 'to', 'python')
tup2 = (1, 2, 3, 5, 7, 9, 11)

#1.indexing
print(tup1[1], tup2[2])

#2.negative indexing
print(tup1[-2], tup2[-2])

#3.slicing
print(tup1[:3], tup2[2:5])


#DELETING DIFFERENT DICTIONARY ELEMENTS

dictionary1 = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
#1.using del
remove = ['one', 'three']
for i in remove:
    del dictionary1[i]
    print(dictionary1)

#2.using pop
dictionary1.pop('five')
print(dictionary1)
