print("Staircase!")

# Recursive Function takes in amount of steps as parameters 
# and returns number of ways to reach top
# Takes in storage param. to store results and 
# prevent redundant computation (Dynamic Programing)
def helper(steps, storage):

	# Exit code for recursive function
	# When 0-1 steps, only one way to reach top
	if (steps <= 1):
		return 1

	# If result was already found and stored,
	# no need to repeat computation
	if (storage[steps]):
		return storage[steps]

	# Initialize result variable
	# Ex: 3 steps equals answer to helper(2) +  answer to helper(1)
	# Much like the Fibbonacci sequence.
	result = helper(steps - 1, storage) + helper(steps - 2, storage)

	# Return answer
	return result

# Function calls and returns helper function so no need to pass in array
def stair_case(steps):
	return helper(steps, [None] * (steps + 1))


print(stair_case(0)) #1

print(stair_case(1)) #1

print(stair_case(2)) #2

print(stair_case(3)) #3

print(stair_case(4)) #5

print(stair_case(5)) #8

print(stair_case(6)) #13

print(stair_case(7)) #21