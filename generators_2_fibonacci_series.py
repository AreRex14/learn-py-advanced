def fib():
	a, b = 1, 1
	while 1:
		yield a
		a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
	print("Good, The fib function is a generator.")

	counter = 0
	for n in fib():
		print(n)
		counter += 1
		if counter == 10:
			break

# outputs are below
# Good, The fib function is a generator.
#    1
#    1
#    2
#    3
#    5
#    8
#    13
#    21
#    34
#    55