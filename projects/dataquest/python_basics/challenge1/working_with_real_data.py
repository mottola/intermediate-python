# ASSUME WE HAVE A FILE WITH POPULAR UNISEX NAMES IN THE US
# WE NEED TO open() THE FILE AS READABLE WITH r 
# WE THEN USE read() TO CONVERT THE FILE INTO A PYTHON STRING
# THEN USE split() ON EACH \n TO CONVERT THE DATA INTO A list

# OPEN FILE, STORING TO f
f = open('unisex_names_table_copy.csv', 'r')

# READ FILE, STORING INTO data AS STRING
data = f.read()

# TRANSFORM DATA INTO A LIST ON EACH \n
data_list = data.split('\n')

# DECLARE EMPTY LIST TO HOLD STRING DATA
string_data = []

# LOOP THROUGH EACH ELEMENT IN THE data_list AND SPLIT INTO LIST OF LISTS
for el in data_list:
    comma_list = el.split(',')
    # APPEND LIST OF LISTS TO string_data
    string_data.append(comma_list)
filtered_data = []
count = 1
for el in string_data[1:51]:
    names = string_data[count][1]
    total = float(string_data[count][2])
    count += 1
    new_data = [names, total]
    #print(new_data)
    filtered_data.append(new_data)

for el in filtered_data:
    el[0].strip('""')

# PRINT OUT THE TOP 50 UNISEX NAMES IN THE UNITED STATES
print(filtered_data)