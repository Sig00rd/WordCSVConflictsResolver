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


field_separator = ";"
lines = ["虚空;こくう;pusta przestrzeń, puste niebo;",
         "既存;きそん;istnienie, egzystowanie, bytowanie;",
         "虚空;こくう;pusta przestrzeń;",
         "帰す;きす;zbliżać się do (końca), kończyć się, przypisywać;",
         "銀河;ぎんが;Droga Mleczna;",
         "銀河;ぎんが;galaktyka;"]

words = build_words_dictionary(lines)

# for word in words:
#     print(word)
#     endings = words[word]
#     for ending in endings:
#         print(ending)

remove_excess_endings(words)

for word in words:
    print(word)
    print(words[word])
