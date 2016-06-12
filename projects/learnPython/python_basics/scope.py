# local and global scope

spam = 42  # global


def eggs():
    spam = 21  # local
    print(spam)


eggs()  # prints the spam living in the eggs function
print(spam)  # prints the spam living in the global scope

# I can use the same names for variables
# as long as they live in different scopes
