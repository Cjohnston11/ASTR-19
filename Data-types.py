import numpy as np

#integers
i=10 #integer
print(type(i)) #print out the data type of i 

a_i = np.zeros(i,dtype=int) # declares an array of integers
print(type(a_i)) # will return nd array 
print(type(a_i[0])) # will return int64


#floats 
x = 19.0 #floating point number
print(type(x)) #frint out the dat type of x

y = 1.9e2 #float 190 in scientific notation
print(type(y)) #print out the data type of x

z = np.zeros(i,dtype=float) # declare array of floats
print(type(z)) # will return nd array
print(type(z[0])) #will return float64


#string
s="i am a string."
print(type(s))


#Boolean
yes = True  #boolean true
print(type(yes))

no = False #boolean false
print(type(no))


#List ordered and changeable
alpha_list = ["a", "b", "c"] #list initalization
print(type(alpha_list)) #will say list
print(type(alpha_list[0])) #Will say string
alpha_list.append("d") #will add "d" to list end
print(alpha_list) #will print list


#tuple
alpha_tuple = ("a", "b", "c") # tuple initialization
print(type(alpha_tuple)) #will say tuple 

try: #attempt following line
	alpha_tuple[2]="d" #add d to list
except TypeError: #when get error 
	print("We cant add elements to tuples") #print this message
print(alpha_tuple) #print tuple 


