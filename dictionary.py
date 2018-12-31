dict1={'1':'a','2':'b','3':('a','b')}
print(type(dict1),dict1,dict(enumerate(dict1)))
#dict1.clear()#clears all elements in dictionary
del dict1['1']
print(dict1)
#del dict1#throws exception when we print after del. as the object is deleted.
print(dict1)

dict2=dict1.copy()
print("new dictionary copied %s" % str(dict2))

a_dict={'a':'1'}
print(a_dict.get('a'))
a_dict['b'] = 2
print(a_dict.keys())
print(a_dict.values())
print(a_dict.items())


#a_dict.has_key('a')# print(a_dict.has_key('c'))throws exception;has_key is no longer used. Use IN operator
#a_dict.pop()
#a_dict.items() #Get List of all Key/Value Pairs in Dictionary
#a_dict.keys() #Get List of all Keys in Dictionary
#a_dict.values()#Get List of all Values in Dictionary
