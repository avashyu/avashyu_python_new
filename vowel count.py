word='wardrobe'

vowel='aeiou'

count=0

for letter in word:
    if letter in vowel:
        count+=1

print(f'{count} vowels are in {word}')
