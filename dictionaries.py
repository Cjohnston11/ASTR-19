#define a dictionary data structures
#dictionaries have a key value for the elements
example_dict = {
	"class" : "ASTR19",
	"prof" : "brant",
	"awesomeness" : 10
}
print(type(example_dict))

#get a value via key
course = example_dict ["class"]
print(course)

#change a calue via key
example_dict["awesomeness"]+=1 #increase

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
	print(x,example_dict[x])
