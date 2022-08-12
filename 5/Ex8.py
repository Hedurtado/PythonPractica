
word = input("Ingrese una palabra: ")
word_inverse = word[::-1]

if word == word_inverse:
    print(word.capitalize(), ' es un palindromo')
else:
    print(word.capitalize(), ' no es un palindromo')



