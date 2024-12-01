# #Pangram Numbers
userInput = input()

numbers = {}

numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for i in userInput:
    if i in numberList:
        if i in numbers:
           numbers[i] += 1
        else:
            numbers[i] = 1
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
    