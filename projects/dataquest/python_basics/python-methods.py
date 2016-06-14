# OBJECT METHODS IN PYTHON (METHODS CALL FUNCTIONS ON OBJECTS)

# OBJECT str
# _______________________
# capitalize(), replace()

# OBJECT float
# _________________________
# bit_length(), conjugate()

# OBJECT list
# ________________
# index(), count()


# LIST METHODS
# ______________

fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
deposits = [174, 29, 314, 47, 162, 96, 287]


# INDEX METHOD
print(fam.index('mom'))  # WHERE IS 'mom' IN THE LIST?
print(fam.index('dad'))  # WHERE IS 'dad' IN THE LIST?
print(deposits.index(47))  # WHERE IS 47 IN THE LIST?

# COUNT METHOD
print(fam.count(1.73))  # HOW MANY TIMES DOES 1.73 OCCUR IN THE LIST?
print(fam.count('mom'))  # HOW MANY TIMES DOES 'mom' OCCUR IN THE LIST?
print(deposits.count(29))  # HOW MANY 1'S ARE IN THE LIST

# APPEND METHOD
fam.append('me')  # ADD 'me' TO THE END OF THE LIST
fam.append(1.71)  # ADD 1.71 TO THE END OF THE LIST
deposits.append(65)  # ADD 65 TO THE END OF THE LIST
print(deposits)

# SORT METHOD
deposits.sort()  # SORT THE LIST FROM LEAST TO GREATEST
print(deposits)

# REVERSE METHOD
deposits.reverse()  # REVERSE THE ORDER OF THE LIST

print(fam)
print(deposits)

# REVERSE METHOD

# STRING METHODS
# _______________
# USE help(str) TO VIEW STRING METHODS

sister = 'liz'


# CAPITALIZE METHOD
sister_cap = sister.capitalize()  # RETURNS STRING WITH FIRST LETTER CAPITALIZED
print(sister_cap)

# REPLACE METHOD
sister_rep = sister.replace('z', 'sa').capitalize()  # REPLACE 'z' WITH 'sa' AND CAPITALIZE
print(sister_rep)

# COUNT METHOD
print(sister.count('s'))


