#define a class with an initialize set of parameters

import sys

class Shape:
	#a class for geometric shapes
	def print(self):
		print("here is our shape!")
		print(f"number of sides = {self.num_sides}")
		print(f"length of sides = {self.side_length}")
		
	def __init__(self,nsides=3,length = 1.0):
		self.num_sides = nsides
		self.side_length = length
		
def main():
	#set default number or sides and length
	nsides = 3 
	length = 10.
	
	#if there are at least 2 command line argumenets, set nsides equal to the second
	if(len(sys.argv)>=2):
		nsides = int(sys.argv [1])
		
	#if there are 3 command line arguments set length equal to the third
	if(len(sys.argv)>=3):
		length = float(sys.argv[2])
		
	#initialize our shape
	our_shape = Shape(nsides=nsides, length=length)

		#Print out information about our shape
	our_shape.print()
		
#run our program
if __name__=="__main__":
	main()
	
