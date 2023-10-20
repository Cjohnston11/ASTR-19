import numpy as np


def main(): # main function
	x = np.linspace(0.0, 2*np.pi, num=1000) #for the x side of table 1000 values between 0 and 2pi
	sinx = np.sin(x) # for y side of table sinx
	print ("   x   | sin(x)") #print table
	print ("---------------")
	
	for i in range(len(x)): #iterator in length of x
		print (f" {x[i]:.3f} | {sinx[i]:.3f}") #print x{i} (x0, x1,x2...) .3 f how many decimal points


if __name__=="__main__": # run main
	main()
	







#print(list(range(10)))

#for i in range (10):
	#print (i)
	#y[i]=2*float(i)

#a = "banana"
#for char in a:
	#print(char)
	
#i is iterater, i is each number as progresses i becomes 1,2,3,4, etc


