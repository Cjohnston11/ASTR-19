
			
class animal: #make a class
	def print(self):
		#print out members of class
		print(f"length of arms = {self.arms}") 
		print(f"length of legs = {self.legs}")
		print(f"number of eyes = {self.eyes}")
		print(f"tail = {self.tail}")
		print(f"furry = {self.furry}")
	
	def __init__(self, arms, legs, eyes, tail, furry): #initialize
		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.furry = furry
		
	
def main(): #main function
	#sets values of data
	arms = 0.0 
	legs = 4.0
	eyes = 2
	tail = True
	furry = True
	
	#initialize the animal 	
	my_animal = animal(arms=arms, legs = legs, eyes = eyes, tail = tail, furry = furry)

	my_animal.print()
	
	
if __name__=="__main__": #run
	main()
