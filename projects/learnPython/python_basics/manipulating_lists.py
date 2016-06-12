# LIST MANIPULATION
# _________________
# CHANGING LISTS
# ADD LIST ELEMENTS
# REMOVE LIST ELEMENTS

fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]

# CHANGE DAD'S HEIGHT
fam[7] = 1.86
print(fam)

# REPLACE LIZ WITH LISA IN THE LIST
fam[0:2] = ['lisa', 1.74]
print(fam)

# ADDING TO THE LIST
fam += ['me', 1.68]
print(fam)

# USE del() TO DELETE FROM THE LIST
del(fam[8])  # DELETES 'ME' FROM LIST
print(fam)
del(fam[-1])  # DELETES THE HEIGHT ELEMENT FOR 'ME'
print(fam)

# THIS COPY OF FAM POINTS TO THE SAME SPOT IN MEMORY
# fam2 = fam

# TO AVOID ALTERING THE SAME LIST, COPY LIKE SO:
fam2 = list(fam)
print(fam2)

del(fam2[0])  # DELETES LISA
del(fam2[0])  # DELETES LISA'S HEIGHT

print(fam2)
print(fam)  # FAM WAS NOT ALTERED

# DELETE MOM FROM FAM LIST
del(fam[-4:-2])
print(fam)
