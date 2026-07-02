my_st = {1,2,3,4,5,6,6,6} # Doesn't take duplicates data 
print(my_st) # 1,2,3,4,5,6
yr_st = {2,3,4,5}

# some_functions used in sets 
print(yr_st.issubset(my_st)) #True cuz all the elements of yr_st are in my_st 
print(yr_st.issuperset(my_st)) #False yr_st is not a super set of my_st 
print(yr_st.isdisjoint(my_st)) #False cuz there are similar data between the two sets so they are not disJoint