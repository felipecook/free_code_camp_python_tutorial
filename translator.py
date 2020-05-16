

# will translate any vowels into the letter g in a phrase that is prompted to the user
def translator(phrase):
    translated_phrase = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translated_phrase = translated_phrase + "g"
        else:
            translated_phrase = translated_phrase + letter
    return translated_phrase


print(translator(input("Enter a phrase to be translated: ")))

