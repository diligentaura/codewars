# This is a Gamer Win
import os

word_list = []
number_of_times_ran = 0


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


while True:
    print("This Application Will Convert A Sentence or Word to Be Censored by Letter in Discord")
    word = input("To Start Enter Your Sentence or Word: ")

    for i in range(0, len(word)):
        word_list.append(word[i])
        i += 1

    for i in range(0, len(word_list)):
        censored = "||" + str(word_list[i]) + "|| "
        word_list[i] = censored

    for i in range(0, len(word_list)):

        if number_of_times_ran == 0:
            stored_censored_word = word_list[i]
            number_of_times_ran = 1

        else:
            stored_censored_word = stored_censored_word + word_list[i]

    stored_censored_word = (f'"{stored_censored_word}"')
    addToClipBoard(stored_censored_word)
    number_of_times_ran = 0
    word_list = []
