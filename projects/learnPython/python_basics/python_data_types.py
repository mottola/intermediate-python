# PYTHON WAS CREATED BY GUIDO VAN ROSSUM
# PYTHON IS GENERAL PURPOSE: BUILD ANYTHING!
# PYTHON IS OPEN SOURCE AND FREE!
# PYTHON HAS MANY PACKAGES FOR MANY DIFFERENT APPLICATIONS/FIELDS


print(4 + 5)  # PRINTS 9

# CALCULATE BMI WEIGHT/(HEIGHTsquared)

height = 1.68  # HEIGHT IN METERS
weight = 71.21  # WEIGHT IN KG
tall = False
bmi = weight / height ** 2
notFat = True
print(bmi)


# DATA TYPES IN PYTHON
# ----------------------
# float - real numbers - 1.78
# int - integer numbers - 7
# str - string, text - 'hello'
# bool - True or False



# TO CHECK THE VALUE TYPE IN PYTHON, WRAP IN TYPE
print(type(bmi))

# USE str(), int(), float(), and bool() to convert

# CONVERTING BMI FROM FLOAT TO STRING
string_bmi = str(bmi)
print(string_bmi)
print(type(string_bmi))

