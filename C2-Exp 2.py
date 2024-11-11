print("Name : Niranjana S Nair")
print("Admission no : A24MCA047")
print("Experiment no : 2")
def char_freq(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

string =input("Enter the string : ")
print(char_freq(string))
def modify_string(s):
    if s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'
print(modify_string(string))

def long_word(words):
    if not words:
        return 0
    return max(len(word) for word in words)

word_list = ["apple", "orange", "mango", "date"]
print(word_list)
print("Length of longest word in list : ",long_word(word_list))


