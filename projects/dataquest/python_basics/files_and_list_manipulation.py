# USING PYTHON TO OPEN FILES

# THE open() FUNCTION IS USED TO OPEN FILES

# open() TAKES TWO ARGUMENTS ('FILENAME, MODE')

# FOR EXAMPLE: open(hello.txt, r) r means 'read'

# THE FILE OBJECT ALSO HAS A read() method

f = open('hello.py', 'r')
g = f.read()

# THE READ METHOD WILL RETURN THE CONTENTS OF f AS A STRING
# TO MAKE THE DATA MORE USEFUL, WE USE SPLITING TO CONVERT IT INTO A list

sample = 'john,plastic,joe'
split_list = sample.split(',')  # SPLITS AT EACH COMMA
print(split_list)

string_two = 'How much wood\ncan a woodchuck chuck\nif a woodchuck\ncan chuck wood?'
split_string_two = string_two.split('\n')  # SPLITS AT EACH \n
print(split_string_two)

# USING LOOPS TO split() DATA
cities = ['Boulder', 'Austin', 'San Francisco', 'Seattle', 'Vancouver']

# TO LOOP THROUGH THE LIST:
for city in cities:
   print(city)

# LIST OF LISTS
three_rows = ['Albuquerque, 749', 'Anaheim, 371', 'Anchorage, 828']
final_data = []

# THIS LOOP WILL SEPARATE OUR SINGLE LIST INTO A LIST OF 3 LISTS
for row in three_rows:
   split = row.split(',') # TURNS LIST INTO LIST OF THREE LISTS
   final_data.append(split)
print(final_data)  # SINCE ONLY INDENTED LINES ARE EXECUTED IN THE LOOP, print(final_list) WILL ONLY OCCUR ONCE

# THE MANUAL WAY OF ACCESSING DATA IN A LIST OF LISTS

# RETURNS THE FIRST LIST'S FIRST ELEMENT: 'Albuquerque'
first_list_first_value = final_data[0][0]
print(first_list_first_value)

# USING A FOR LOOP TO ACCESS LISTS
crime_rates = []

for row in final_data:
   crime_rate = row[1]
   crime_rates.append(crime_rate)
print(crime_rates)

# CONVERT CRIME RATES TO INTEGER VALUES
int_crime_rates = []
for row in three_rows:
    split = row.split(',')
    crime_rate = int(split[1])
    int_crime_rates.append(crime_rate)
print(int_crime_rates)