#postive numbers in a list

#list1=[12,-7,5,64,-14]
#output:12,5,64

list1 = []

n = int(input("total number of list elements: "))
for k in range(n):
    m = int(input("enter the element: "))
    list1.append(m)
print("list1=", list1)
            
print("output: ")
a = list(filter(lambda x: x > 0, list1))
print(*a, sep = ", ")



#list2=[12,14,-95,3]
#output:[12,14,3]       

list2 = []

i = int(input('\n'"total number of list elements: "))
for j in range(i):
    q = int(input("enter the element: "))
    list2.append(q)
print("list2=", list2)
            
print("output: ")
b = list(filter(lambda y: y > 0, list2))
print(b)
        
