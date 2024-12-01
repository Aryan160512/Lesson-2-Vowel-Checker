#Pangram Numbers
userInput = input()

numbers = {'1': 0,
           '2': 0,
           '3': 0,
           '4': 0,
           '5': 0,
           '6': 0,
           '7': 0,
           '8': 0,
           '9': 0,
           '0': 0}

isPangram = True

for i in userInput:
    numbers[i] += 1
for j in numbers:
    if numbers[j] < 1:
        isPangram = False

if isPangram == True:
    print('It is a number Pangram')
else:
    print('It is not a number Pangram')

print(numbers) 

#Merging Dictionaries

dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

dict2 = {
    'd': 4,
    'e': 5,
    'f': 6
}

dict1.update(dict2)

print(dict1)
    