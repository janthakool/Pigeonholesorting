def Pigeonhole_sort(array):
	min_arr = min(array)
	size = max(array) - min_arr + 1
	holes = [0] * size
	for i in array:
		holes[i - min_arr] += 1
	i_array = 0
	for count in range(size):
		while holes[count] > 0:
			array[i_array] = count + min_arr
			holes[count] -= 1
			i_array += 1
	return array
	
# array = [1,3,10,1,1]
# Pigeonhole_sort(array)
# n = len(array)
# print ("Sorted array is")
# for i in range(n):
   # print ("%d" %array[i])
