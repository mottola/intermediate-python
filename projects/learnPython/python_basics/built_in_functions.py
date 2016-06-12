# FUNCTIONS AND PACKAGES IN PYTHON

# SOME BUILT-IN PYTHON FUNCTIONS
# ______________________________
# print(), type(), str(), bool(), and float()
# sorted(), max(), len()

# YOU CAN ALSO ASK PYTHON FOR HELP ABOUT A FUNCTION
# _________________________________________________
# TO ASK FOR HELP REGARDING THE max() FUNCTION:
# help(max)

# CREATE 2 LISTS
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# PASTE TOGETHER FIRST AND SECOND : FULL
full = first + second
print(full)

# USE sorted() WITH reverse = true TO CREATE A NEW SORTED LIST
# reverse = True will sort the list from highest to lowest
full_sorted = sorted(full, reverse=True)
print(full_sorted)

