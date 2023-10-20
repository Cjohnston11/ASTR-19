import numpy as np
def main():
	x=9
	result = cubedplus8(x)
	if result > 27:
		print ("YAY!")
	print (result)
	
	
def cubedplus8(x):
	return x**3 + 8
		
if __name__=="__main__":
	main()
