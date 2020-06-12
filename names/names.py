import time
from binary_search_tree import BSTNode 

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# this takes about 3 seconds, O(n)
# I'm iterating over 2 lists, a condition, and adding a name to the list
# so the complexity is O(n) where n is the the size of shortest list

duplicates = [name_1 for name_1 in names_1 for name_2 in names_2 if name_1 == name_2]  # Return the list of duplicates in this data structure
# name_1 for name_1 in names_1 for name_2 in names_2 if name_1 == name_2

# Replace the nested for loops below with your improvements
# this takes close to 10 seconds or more on my machine 
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
