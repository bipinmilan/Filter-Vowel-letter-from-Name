# Filter-Vowel-letter-from-Name
name = str(input("Enter your name:\n\n"))
print()

print("Your name is:\n", ''.join(name))
print()

vowels = ['a', 'e', 'i', 'o', 'u']
print()

def filter_new(name):
    if name in vowels:
        return True
    else:
        return False


result = list(filter(filter_new, name))
if result:
    print("Vowel Letters found after Filtering:\n", result)
    print()
    print("Number of Vowel Letter in your Name:\n", len(result))
else:
    print("No Vowel Letters found in your name")
