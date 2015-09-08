i = 0
numbers = []
gadget = 52

while i < gadget:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now:", numbers
	print "At the bottom i is %d" % i
	
print "The Numbers"

for num in numbers:
	print num
