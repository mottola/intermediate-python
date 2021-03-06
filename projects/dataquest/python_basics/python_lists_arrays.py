# LISTS(ARRAYS) IN PYTHON
# _______________________
# NAME A COLLECTION OF VALUES
# MAY CONTAIN ANY DATA TYPE
# MAY CONTAIN A MIX OF DATA TYPES (COMPOUND DATA TYPE)
# LISTS CAN ALSO CONTAIN MORE LISTS

fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
print(fam)

# PRINT LIZ'S NAME AND HEIGHT
print(fam[0] + ' : ' + str(fam[1]))


# BETTER WAY TO STORE THE INFO IS WITH SUB-LISTS
fam2 = [['liz', 1.73],
        ['emma', 1.68],
        ['mom', 1.71],
        ['dad', 1.89]]
print(fam2)
print(fam2[0])

# USE type() TO PROVE THEY ARE LISTS
print(type(fam))
print(type(fam2))

print(fam[-1])  # PRINTS LAST ITEM OF LIST (DAD'S HEIGHT)

# SLICING LETS YOU SELECT ELEMENTS OF A LIST TO CREATE A NEW LIST
print(fam[4:8])  # SLICES FROM 4 UP TO BUT NOT INCLUDING 8
print(fam[4:6])  # SLICES AND RETURNS MOM AND MOM'S HEIGHT

# NOT SPECIFYING A BEGIN WILL ASSUME YOU WANT TO START AT THE FIRST ELEMENT
# NOT SPECIFYING AN END WILL ASSUME YOU WANT TO START AT THE LAST ELEMENT

fam3 = fam2[:2]  # SLICES OUT LIZ AND EMMA AND THEIR HEIGHTS
print(fam3)
