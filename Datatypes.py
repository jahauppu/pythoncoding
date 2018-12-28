# datatypes
'''
var1 = "Jahnavi"
var2 = 1988

print("%s was born in Rajahmundry on %d " % ("Jahnavi",1988))
print("%s was born in Rajahmundry on %d " % (var1,var2))
#print("%s was born in Rajahmundry on %d " % (nam1=1988,nam2="Jahnavi"))
print("{} was born in Rajahmundry on {} " .format(var1,var2))
print("{1} was born in Rajahmundry on {0} " .format(var1,var2))
print("{1} was born in Rajahmundry on {0} " .format(1988,"Jahnavi"))
print("{nam2} was born in Rajahmundry on {nam1} " .format(nam1=1988,nam2="Jahnavi"))

print("%e exponentil notation of %d" % (2,3))
print("%g exponentil notation of %e" % (2.541,3))


'''

#String Methods 

str1 = "jahnavi is working in IBM"
print(str1.capitalize())
cost = "153"
print(len(cost))
print(cost.center(5,"$")) 

str = "method 1 must 1 have a parameter 1 'self'"
substr = str
print(substr.count('1',0,len(substr)))

print(substr.endswith(r"self",0,len(substr)))
str2 = "must"
str3 = "hi"
print(substr.find(str2,0,len(substr)))
print(substr.find(str2))

print(substr.index(str2))
print(substr.find(str3)) #returns -1
#print(substr.index(str3)) -- raises exception 


str4 = "this is string example....wow!!!";

print (str4.ljust(50, '0'))
print (str4.rjust(50, '0'))


str5 = "this is string example....wow!!!";
str6 = "is";

print (str5.rindex(str6))
print (str5.index(str6))


