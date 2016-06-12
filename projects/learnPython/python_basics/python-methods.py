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


# INDEX METHOD
print(fam.index('mom'))  # WHERE IS 'mom' IN THE LIST?
print(fam.index('dad'))  # WHERE IS 'dad' IN THE LIST?

# COUNT METHOD
print(fam.count(1.73))  # HOW MANY TIMES DOES 1.73 OCCUR IN THE LIST?
print(fam.count('mom'))  # HOW MANY TIMES DOES 'mom' OCCUR IN THE LIST?

# APPEND METHOD
fam.append('me')  # ADD 'me' TO THE END OF THE LIST
fam.append(1.71)  # ADD 1.71 TO THE END OF THE LIST
print(fam)


# STRING METHODS
# _______________

sister = 'liz'


# CAPITALIZE METHOD
print(sister.capitalize())  # RETURNS STRING WITH FIRST LETTER CAPITALIZED

# REPLACE METHOD
print(sister.replace('z', 'sa').capitalize())  # REPLACE 'z' WITH 'sa'


