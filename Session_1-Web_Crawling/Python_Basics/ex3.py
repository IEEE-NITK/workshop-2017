#Objective 4 - Control Flow

# If - Else if - Else
buses = 10
cars = 5
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
# That's too many buses.

# Lists and For loops
# Any type of data type can be present
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for i in change:
	print "I got %r" % i

# Building a list
elements = []
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
print elements

# While Loops
i = 0
numbers = []
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	i = i + 1
print "Numbers now: ", numbers
print "The fourth number is %d" % numbers[3]

# Dictionaries
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print stuff['name']