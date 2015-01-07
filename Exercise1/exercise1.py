a = int(raw_input("Please enter the first integer:"))
	while (not a.isdigit() ):
		a = raw_input(“That’s not a number. Try again:”)
b = int(raw_input("Please enter the second integer:"))
	while (not b.isdigit() ):
		b = raw_input(“That’s not a number. Try again:”)
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
print "The sum of %s and %s is: %s" % ( a, b, c)
print "The difference of %s and %s is: %s" % ( a, b, d)
print "The product of %s and %s is: %s" % ( a, b, e)
print "The quotient of %s and %s is: %s with remainder: %s" % ( a, b, f, g)