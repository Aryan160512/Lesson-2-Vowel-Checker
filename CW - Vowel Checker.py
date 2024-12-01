userInput = input().lower()

vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

for i in userInput:
    print(i)
    
    if i in vowels:
        vowels[i] += 1

print(vowels)

vowels = {}

letter = ['a', 'e', 'i', 'o', 'u']

for i in userInput:
    if i in letter:
        if i in vowels:
            vowels[i] += 1
        else:
            vowels[i] = 1

print(vowels)

#Pangrams
userInput = input().lower()

letters = {'a': 0,
           'b': 0,
           'c': 0,
           'd': 0,
           'e': 0,
           'f': 0,
           'g': 0,
           'h': 0,
           'i': 0,
           'j': 0,
           'k': 0,
           'l': 0,
           'm': 0,
           'o': 0,
           'p': 0,
           'q': 0,
           'r': 0,
           's': 0,
           't': 0,
           'u': 0,
           'v': 0,
           'w': 0,
           'x': 0,
           'y': 0,
           'z': 0}
isPangram = True

for i in userInput:
    letters[i] += 1
for j in letters:
    if letters[j] < 1:
        isPangram = False

if isPangram == True:
    print('It is a Pangram')
else:
    print('It is not a Pangram')
print(letters)