my_st = {1,2,3,4,5,6,6,6} 
yr_st = {2,3,4,5, 10, 12}

# union operator | 
print(my_st | yr_st) # returns a new set with all the elements from both sets

# intersection operator &
print(my_st & yr_st) # returns a new set with only the elements that the sets have in common

# Difference operator - 
print(my_st - yr_st) # returns only set A (my_st) elements 

# The symmetric difference operator ^ 
print(my_st ^ yr_st) # returns a new set with the elements that are either in the first or the second set, but not both
