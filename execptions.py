#python exeptions let you deal with unexpected results

try:
	print (a) #this will thorw an exeption since a is not defined
except:
	print("a is not defined!")
	
#there are specific errors to help with cases
try:
	print(a)
except NameError:
	print ("a is still not defined!")
except:
	print ("something else went wrong")
	
	
#this will break our program since a is not defined
print (a)
