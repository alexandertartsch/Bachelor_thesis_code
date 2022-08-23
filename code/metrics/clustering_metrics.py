## This function returns the absolute of the time distance between two points.
# It is currently used to calculate the distance between an AP and a stimulus, but could generally also be used for any vector with time in its first component.
<<<<<<< HEAD
def time_dist_to_stimulus(x, y):
	time_diff = abs(x[0] - y[0])
	
	return time_diff

## Considers the absolute time and energy difference and weights the energy difference by an importance factor.
def time_dist_and_energy(x, y, energy_importance = 10e-7):
	time_diff = abs(x[0] - y[0])
	energy_diff = abs(x[1] - y[1])

	return time_diff + energy_importance * energy_diff
=======
def latency_difference(x, y):
    time_diff = abs(x[0] - y[0])
    
    return time_diff
>>>>>>> d9b68deaf6d8dd9f8ef1487207df0f1f5f80bb73
