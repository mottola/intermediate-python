def div42by(divideby):  # USE THE TRY AND EXCEPT STATEMENTS TO LOG THE ERROR AND CONTINUE
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')
# IF TRY/EXCEPT WERE NOT USED THE PROGRAM WOULD CRASH WHEN DIVIDING BY ZERO

print(div42by(2))
print(div42by(12))
print(div42by(0))  # CAN NOT DIVIDE BY ZERO (ERROR THROWN)
print(div42by(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats!')
    elif int(numCats) < 0:
        print('I don\'t think you can have negative cats!')
    else:
        print('You should get more cats!')
except ValueError:
        print('You did not enter a number.')
