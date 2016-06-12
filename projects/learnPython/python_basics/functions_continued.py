import random  # importing the random module


def hello(name):  # name is the parameter
    print('Hello ' + name)

hello('Anna')  # Anna is the argument

hello('Rick')  # Rick is the argument


def plusone(number):
    return number + 1

newNumber = plusone(5)
print(newNumber)


def randnum():
    print(random.randint(1, 9))  # printing a random number

randnum()

