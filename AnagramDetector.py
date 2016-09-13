# JRIngram 2016-09-13
# Calculates if two alphabetical strings are anagrams of each other.

# Assigns each letter a unique prime number value
prime_letters = {
    'a': 2,
    'b': 3,
    'c': 5,
    'd': 7,
    'e': 11,
    'f': 13,
    'g': 17,
    'h': 19,
    'i': 23,
    'j': 29,
    'k': 31,
    'l': 37,
    'm': 41,
    'n': 43,
    'o': 47,
    'p': 53,
    'q': 59,
    'r': 61,
    's': 67,
    't': 71,
    'u': 73,
    'v': 79,
    'w': 83,
    'x': 89,
    'y': 97,
    'z': 101
}

def calculate_anagram(possible_anagrams):
    string_one_value = 0
    string_two_value = 0
    correct_input = True
    strings = possible_anagrams.split("?")
    original_string_1 = strings[0]
    original_string_2 = strings[1]
    strings[0] = strings[0].replace('"', '').lower().replace("'","")
    strings[1] = strings[1].replace('"', '').lower().replace("'","")
    if possible_anagrams.__contains__('?') == False:
        print ('Parameters must contain ? between the two parameters!')
        correct_input = False
    if strings[0].replace(' ','').isalpha() == False or strings[0].replace(' ','').isalpha() == False:
        print ('Parameters must only contain spaces and letters!')
        correct_input = False
    if correct_input is True:
        for i in range(0, len(strings[0].replace(' ', ''))):
            string_one_value += prime_letters[strings[0].replace(' ', '')[i]]
        for i in range(0, len(strings[1].replace(' ', ''))):
            string_two_value += prime_letters[strings[1].replace(' ', '')[i]]

        if string_one_value == string_two_value:
            print ('%sis an anagram of%s' % (original_string_1, original_string_2))
        else:
            print ('%sis NOT an anagram of%s'% (original_string_1, original_string_2))

calculate_anagram('"wisdom" ? "mid sow"')
calculate_anagram('"Seth Rogan" ? "Gathers No"')
calculate_anagram('"Reddit" ? "Eat Dirt"')
calculate_anagram('"Schoolmaster" ? "The classroom"')
calculate_anagram('"Astronomers" ? "Moon starer"')
calculate_anagram('"Vacation Times" ? "I\'m Not as Active"')
calculate_anagram('"Dormitory" ? "Dirty Rooms"')
