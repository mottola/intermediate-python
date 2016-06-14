# USING CONDITIONAL LOGIC IN PYTHON

# BOOLEANS IN PYTHON - True False
cat = True
dog = False

print(type(cat))
print(type(dog))

print(cat)
print(dog)

# BOOLEAN OPERATORS IN PYTHON
# ___________________________
#           ==
#           !=
#           >
#           <
#           >=
#           <=

print(8 == 8)
print(8 != 8)
print(8 == 10)
print(8 != 10)

list = [
    "The Hitchhiker's Guide to the Galaxy",
    "The Restaurant at the End of the Universe",
    "Life, the Universe and Everything",
    "So Long, and Thanks for All the Fish",
    "Mostly Harmless"
]

# PRINTS THE INDEX(i) AND THE ELEMENT(el) IN LIST
# ENUMERATE ADDS A COUNTER TO THE VARIABLE i 
# i WILL START AT 0 UNLESS AN OTHERWISE STARTING INDEX IS PASSED IN WITH list

for i, el in enumerate(list):
  print(i, el)

for i, el in enumerate(list, 10):
   print(i, el)

for item in list:
  print(item)


# BOOLEAN LOGIC AND CONDITIONAL STATEMENTS
sample_rate = 749
greater = (sample_rate > 5)  # greater is assigned the True boolean
if greater:
  print(sample_rate)

t = True
f = False 

if t:
  print('Now you see me')
if f:
  print('Now you don\'t')

# NESTING if STATEMENTS
value = 5000

if value > 500:
  if value > 2500:
    print('This number is quite large!')

# IF STATEMENTS AND FOR LOOPS
cities = ['Seattle', 'Boulder', 'Austin', 'San Francisco', 'Washington']
counter = 0  # TRACKS HOW MANY ITEMS ARE IN THE LIST
index = 0  # TRACKS THE INDEX THAT AUSTIN WILL BE FOUND AT
found = False 
for city in cities:
  if city == 'Austin':
    index = counter
  counter += 1
print(index)
print(counter)

