# >>>>>>>>>>>>  ENTER YOUR SETS HERE   <<<<<<<<<<<<<<<<< 

# creating an empty list
setOne = []
  
# number of elemetns as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    setOne.append(ele)
    
# creating an empty list
setTwo = []
  
# number of elemetns as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    setTwo.append(ele)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^






#----------------------------- Set Creation (method 1)  ------------------------------------------------
 
#	Uses an empty list to fill with the elements of myList so long as the elements
#	do not already exist in the newList.  This eliminates duplicates.

#-------------------------------------------------------------------------------------------------------
def make_set(myList):
	
	# Creates an empty list for us to place elements of myList in
	newList = []
	
	# For loop used to incrememnt through the elements in myList 
	for x in range(len(myList)):
		
		# if conditional used to determine if the element of myList already exists in the new List
		if myList[x] not in newList:
			
			# if true, we use append method to add the element to the newList List
			newList.append(myList[x])
			
			
	# Once the for loop has finished iterating through the elements, it returns newList		
	return newList
	
		
#-------------------------- Set Union (method 2)  -----------------------------------------------------
		
#	Uses an empty list to fill with the elements of a and b so long as the elements
#	do not already exist in the newList.  Meaning all unique numbers from the two
# 	lists will be stored in newList.

#-------------------------------------------------------------------------------------------------------
def union(a, b):
	
	# Creates an empty list for us to place elements of 'a' and 'b' in
	newList = []
	
	# For loop used to incrememnt through the elements in list 'a'
	for x in range(len(a)):
		
		# if conditional used to determine if the element of myList already exists in the new List
		if a[x] not in newList:
			
			# if true, we use append method to add the element to the newList List
			newList.append(a[x])
	
	# For loop used to incrememnt through the elements in list 'b'
	for y in range(len(b)):	
		
		# if conditional used to determine if the element of myList already exists in the new List
		if b[y] not in newList:
			
			# if true, we use append method to add the element to the newList List
			newList.append(b[y])
				
	# Once the for loop has finished iterating through the elements, it returns newList		
	return newList
		

#---------------------- Set Intersection (method 3)  --------------------------------------------------
		
#	Uses an the method make_set to eliminate all duplicates from the lists.  
#	Creates a new list to hold the common elements between the lists.
#	In order to prevent index out of bounds errors we find the lengths of the two lists
# 	and increment through the shorter list.  We compare all of the values of the shorter
# 	list to the values in the longer list.  If an element of the shorter list also exists
#	in the longer list, then we add it to newList.	

#-------------------------------------------------------------------------------------------------------
def intersect(a, b):
	
	# Eliminate the duplicates from each list
	a = make_set(a)
	b = make_set(b)	
	
	# Creates an empty list for us to place elements of 'a' and 'b' in
	newList = []
	
	# We need to know which list is larger in order to get the indexing correct
	if len(a) >= len(b):
		
		# Increment through the smaller list
		for x in range(len(b)):
			
			# Compare all the elements in the smaller list to the bigger list
			if b[x] in a:
				
				# If they are in the bigger list we will add them to newList 
				newList.append(b[x])
	
	# If the first case was false then this one will be true
	elif len(a) <= len(b):
		
			# Increment through the smaller list
			for y in range(len(a)):
				
				# Compare all the elements in the smaller list to the bigger list
				if a[y] in b:
					
					# If they are in the bigger list we will add them to newList 
					newList.append(a[x])
		
	# Once the for loop has finished iterating through the elements, it returns newList		
	return newList

		
#-------------------- Symetric Difference (method 4)  -------------------------------------------------
		
#	Uses an the method make_set to eliminate all duplicates from the lists.  
#	Creates a new list to hold the unique elements between the lists.
# 	We will find all of the elements of b which do not exist in a, then we will
#	find all of the elements of a which do not exist in b.

#-------------------------------------------------------------------------------------------------------
def symmetric_diff(a,b):	
	
	# Eliminate the duplicates from each list
	a = make_set(a)
	b = make_set(b)
		
	# Creates an empty list for us to place elements of 'a' and 'b' in
	newList = []
			
	# Increment through one list
	for x in range(len(b)):
		
		# Compare all the elements in the smaller list to the bigger list
		if b[x] not in a:
			
			# If the element of 'b' is not in list 'a', then we add it to newList
			newList.append(b[x])
			
	# Increment through the second list
	for y in range(len(a)):
		
		# Compares an element of list 'a' to all of list 'b'
		if a[y] not in b:
			
			# If the element of 'a' is not in list 'b', then we add it to newList
			newList.append(a[y])

	# Once iterating has completed, it returns newList		
	return newList

	
	
#-----------------------------  Main Exicutable  -----------------------------------------------------	
	
print("\n\nSet 1:  " + str(setOne))
print("Set 2:  " + str(setTwo) + "\n\n")



#------  MAKE A UNION  -------------------------------------------------------------------------------
print("\n\tUnion: " + str(union(setOne, setTwo)) + "\n")

#------  MAKE AN INTERSECTION  -----------------------------------------------------------------------
print("\n\tIntersection: " + str(intersect(setOne, setTwo)) + "\n")

#------  SYMETRIC DIFFERENCE  ------------------------------------------------------------------------
print("\n\tSymetric Difference:  " + str(symmetric_diff(setOne,setTwo)))