def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return (a+b)
	
def subtract(a,b):
	print "SUBTRACTING %r - %r" % (a,b)
	return a - b
	
def multiply(a,b):
	print "MULTIPYLING %d * %d" % (a,b)
	return a*b
	
def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a/b
	
print "lets do some math functions!!!!!"

age = add(20,7)
height = subtract(9000,800)
weight = multiply(6,2)
iq = divide (100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "what becomes: ",what,"can you do it by hand?"
