numbers =  [1,2,3,4]
print("check index in list:",list(enumerate(numbers)))

print(numbers[3])
#print(numbers[4]) -- raise exemption

#Append Method
ap_list = [('a','b'),1,2,3,'hello'] 
print(type(ap_list)) #list
print(id(ap_list))

ap_list.append(['c','d'])
print(ap_list)
print("check index in list:",list(enumerate(ap_list)))
print(ap_list[0][1])#b

print(ap_list.count(2))
print(ap_list.count(6))

var_a = ['hello',1,2,('a','b')]
var_b = [22,33,44]

var_a.extend(var_b)
print(var_a)

var_a.append(var_b)
print(var_a)

#print(min(var_a))#throws exception '<' not supported between int and str
print(min(var_b))

var_c = [0,1,2,2,2,3]
print(var_c.index(2))#2
#print(var_c.index(4))#throws exception with error values does not exist

ap_list.insert(3,'Jahnavi')
print(ap_list)

print(list(enumerate(ap_list)))
ap_list.pop(1)
print(list(enumerate(ap_list)))
ap_list.pop()
print(list(enumerate(ap_list)))
#print(ap_list.pop(5))# pop index out of range 
# difference between remove and pop ; remove() by element , pop() by index; remove has to search for value in list()

var_b.reverse()
ap_list.reverse()
print(var_b)
print(ap_list)
var_b.sort()
print(var_b)