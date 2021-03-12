from buckets import *
import unittest

class TestDistribution(unittest.TestCase):
	def test_buckets(self):
		self.assertListEqual(distribution([8,6,4,3],4,25),[8,6,4,3])
		self.assertListEqual(distribution([30,10,20],3,30),[10,10,10])
		self.assertListEqual(distribution([1000,5000,7000],3,8000),[1000,3500,3500])
		self.assertListEqual(distribution([0],1,0),[0])
		self.assertListEqual(distribution([100,0],2,100),[100,0])
		self.assertListEqual(distribution([100,0,0],3,0),[0,0,0])
		self.assertListEqual(distribution([50,50],2,95),[47.5,47.5])
		self.assertListEqual(distribution([15,15,15],3,36),[12,12,12])
		self.assertListEqual(distribution([10,10,10],3,4),[1.33,1.33,1.33])
		self.assertListEqual(distribution([10,3,8,6],4,20),[5.67,3,5.67,5.67])
		
				
		
if __name__ == "__main__":
       unittest.main()
