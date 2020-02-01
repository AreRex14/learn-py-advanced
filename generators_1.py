import random

def lottery():
	# return 6 numbers between 1 and 40
	for i in range(6):
		yield random.randint(1, 40)

		# returns a 7th number between 1 and 15
		yield random.randint(1, 15)

for random_number in lottery():
	print("And the next number is... %d!" %(random_number))

# outputs are below
# And the next number is... 32!
# And the next number is... 17!
# And the next number is... 5!
# And the next number is... 32!
# And the next number is... 39!
# And the next number is... 24!
# And the next number is... 12!