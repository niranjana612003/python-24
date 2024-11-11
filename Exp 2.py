print("Niranjana S Nair")
print("Admission No: A24MCA047")
print("swapped the word Experiment: 2")
from collections import Counter
text=input("enter the line of text")
words = text.lower().split()
wordcount = Counter(words)
for word,count in wordcount.items():
    print(f"{word} appears {count} times")

first_word = words[0]
if len(first_word) > 1:
    first_word = first_word[-1] + first_word[1:-1] + first_word[0]
    print(f"swapped word : {first_word}")
else:
    print("cannot swap the first word")