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



