print("Staircase!")

# Recursive Function takes in amount of steps as parameters 
# and returns number of ways to reach top
# Takes in storage param. to store results and 
# prevent redundant computation (Dynamic Programing)
def stair_case(steps, storage):

	# Exit code for recursive function
	# When 0-1 steps, only one way to reach top
	if (steps <= 1):
		return 1

	# If result was already found and stored,
	# no need to repeat computation
	if (storage[steps]):
		return storage[steps]

	# Initialize result variable
	# Ex: 3 steps equals answer to stair_case(2) +  answer to stair_case(1)
	# Much like the Fibbonacci sequence.
	result = stair_case(steps - 1, storage) + stair_case(steps - 2, storage)
		 	



