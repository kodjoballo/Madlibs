
# Madlibs game

"""
Game where there is a pre-story and we need to replace the string enclosed by <> in order to change the sens or to
have a sens to the story
"""

with open("madlibs_story.txt", 'r') as file:
    story = file.read()
    print("\n")

words = set()
word_start = "<"
word_end = ">"

starting_index = -1

for i, char in enumerate(story):

    if char == word_start:
        starting_index = i

    if char == word_end and starting_index != -1:
        word = story[starting_index: i+1]
        words.add(word)

print(words)

answers = {}

for word in words:
    answer = input("Enter a word for "+word+" :")
    answers[word] = answer
    print("")


    story = story.replace(word, answer)

print(story)

