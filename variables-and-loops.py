import numpy as np #importing numpy

def main ():
	i=0 #integer
	n=10 #integer
	x=19.0 # decimal point makes it a floating point number
	
	#numpy declares array quickly
	y = np.zeros(n,dtype=float) #declares 10 zeroes as floats using np
	
	#for loops iterate a variable
	
	for i in range (n): #i in range [0,n-1]
		y[i]=2.0*float(i)+1. #set y = 2i+1 as floats #y=[0...19]
		
	#also iterate though a variable
	#printing elements of y
	for y_element in y:
		print(y_element)

#executes main function		
if __name__=="__main__":
	main()
