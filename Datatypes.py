# datatypes

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


