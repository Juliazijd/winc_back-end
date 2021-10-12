from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'

# 1
countries_shortest_names = []
length = ''

def shortest_names(countries):
    length = len(min(countries, key=len))
    for country in countries:
        if len(country) == length:
          countries_shortest_names.append(country)  
    print(countries_shortest_names)
    return countries_shortest_names

# 2
countries_most_vowels = []
three_most_vowels_countries = []

def most_vowels(countries):
    for country in countries:
        counter = 0
        for letter in country:
            if letter in "aeiouAEIOU":
                counter += 1
        countries_most_vowels.append([country, counter])
    three_most_vowels_countries = sorted(countries_most_vowels, reverse=True,
                        key=lambda counter: counter[1])
    three_most_vowels_countries = three_most_vowels_countries[:3]
    three_most_vowels_countries = [x[0] for x in three_most_vowels_countries]
    print(three_most_vowels_countries)
    return three_most_vowels_countries

# 3
found_letters = []
countries_contain_alphabet = []

def alphabet_set(countries):
    for country in countries:
        for letter in country:
            if letter.lower() not in found_letters and letter.isalpha():
                found_letters.append(letter.lower())
        if country not in countries_contain_alphabet:
            countries_contain_alphabet.append(country)
        if len(found_letters) == 26:
            break
    print(countries_contain_alphabet)
    return countries_contain_alphabet

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

# shortest_names()
# most_vowels()
# alphabet_set()