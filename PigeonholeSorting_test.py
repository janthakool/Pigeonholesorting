import unittest
from PigeonholeSorting import Pigeonhole_sort
import random

def is_sorted(array):
	n = len(array)
	for i in range(1,n):
		if array[i] < array[i-1]:
			return False
	return True

class test_sorting(unittest.TestCase):
	def test_ipigeonhole_sort(self):
		max_size = 1500
		for size in range(1, max_size + 1):
			array = [random.randrange(20) for num in range(size)]
			sorted = Pigeonhole_sort(array)
			self.assertTrue(is_sorted(sorted))
			
			
			