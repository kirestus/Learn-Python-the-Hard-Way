#set the variable x and call for a number to be inserted that is 10
x = "there are %d types of people." % 10
#string variable for binary
binary = "binary"
#string variable for do_not
do_not = "don't"
#string varible that should say those who know binary and those who do not
y = "those who know %s and those who %s." %(binary, do_not)

#print x then y
print x
print y

print "I said: %r" %x
print "I also said %s" %y

hillarious = False
joke_evaluation = "Isn't that a funny joke?! %r" 
print joke_evaluation % hillarious

w = "this is the left side of a..."
e = "a string this is the right side."

print w+e