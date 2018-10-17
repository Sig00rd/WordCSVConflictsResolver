import os

import config


def split_writing_and_other_stuff(csv_line):
    return csv_line.split(field_separator, 1)


def build_words_dictionary(csv_lines):
    words_dictionary = {}
    for line in csv_lines:
        writing, other_stuff = split_writing_and_other_stuff(line)
        if writing in words_dictionary:
            words_dictionary[writing].append(other_stuff)
        else:
            words_dictionary[writing] = [other_stuff]

    return words_dictionary


def remove_excess_endings(words_dictionary):
    for word in words_dictionary:
        words_dictionary[word] = handle_endings(words_dictionary[word])


def handle_endings(possible_endings):
    if len(possible_endings) == 1:
        return possible_endings.pop()
    else:
        user_chosen_ending = get_user_to_choose_ending(possible_endings)
        return user_chosen_ending


def get_user_to_choose_ending(possible_endings):
    for i in range(len(possible_endings)):
        print("{:2}: {}".format(i + 1, possible_endings[i]))
    ending_to_save_number = int(input("Podaj numer zakończenia do zostawienia: ")) - 1
    return possible_endings[ending_to_save_number]


def open_csv_file():
    home_directory_path = os.path.expanduser("~")
    file_path = os.path.join(home_directory_path, config.CSV_FILE_PATH)
    file = open(file_path, "r+")
    return file


field_separator = ";"
file = open_csv_file()
lines = [line for line in file]

words = build_words_dictionary(lines)

# for word in words:
#     print(word)
#     endings = words[word]
#     for ending in endings:
#         print(ending)

remove_excess_endings(words)

for word in words:
    print(word+words[word])


file.close()