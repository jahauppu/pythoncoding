tup1 = (1,2,['a','b'],(3,4),5)
print(type(tup1),tuple(enumerate(tup1)))

print(tup1[2][1])
print(tup1[3][0])
#print(tup1[5])#throws exception

print(list(tup1),type(tup1))#tuple
alist = [1,2,['a','b'],(3,4),5]
atuple=tuple(alist)#convert list to tuple
print(type(atuple),type(alist),alist)
a_list=list(tup1) #convert tuple to list
print(type(a_list),a_list)

#b.tuple = atuple.insert(3,3) # throws exception as no object insert 
ctuple = tup1 + atuple
print(ctuple)