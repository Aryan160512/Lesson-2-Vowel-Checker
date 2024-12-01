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

letters = {}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in userInput:
    if i in alphabet:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

print(letters)