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
        words_dictionary[word] = handle_endings(words_dictionary[word], word)


def handle_endings(possible_endings, word):
    if len(possible_endings) == 1 or endings_are_identical(possible_endings):
        return possible_endings.pop()
    else:
        user_chosen_ending = get_user_to_choose_ending(possible_endings, word)
        return user_chosen_ending


# some sorcery I copy-pasted from stack
def endings_are_identical(endings):
    return endings[1:] == endings[:-1]


def get_user_to_choose_ending(possible_endings, word):
    print("Dla słowa: " + word)
    for i in range(len(possible_endings)):
        print("{:2}: {}".format(i + 1, possible_endings[i]))
    ending_to_save_number = int(input("Podaj numer zakończenia do zostawienia: ")) - 1
    return possible_endings[ending_to_save_number]


def open_csv_file(mode):
    home_directory_path = os.path.expanduser("~")
    file_path = os.path.join(home_directory_path, config.CSV_FILE_PATH)
    file = open(file_path, mode)
    return file


def open_csv_file_for_reading():
    return open_csv_file("r")


def open_csv_file_for_writing():
    return open_csv_file("w")


def get_lines_from_file():
    file = open_csv_file_for_reading()
    lines = [line for line in file]
    file.close()
    return lines


def write_words_to_file(words_dictionary):
    file = open_csv_file_for_writing()
    for word in words_dictionary:
        file.write(word + config.FIELD_SEPARATOR + words_dictionary[word])
    file.close()


field_separator = config.FIELD_SEPARATOR
lines = get_lines_from_file()
words = build_words_dictionary(lines)

remove_excess_endings(words)

write_words_to_file(words)
