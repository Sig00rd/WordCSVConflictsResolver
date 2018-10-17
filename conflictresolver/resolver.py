def split_writing_and_other_stuff(csv_line):
    return csv_line.split(field_separator, 1)


def build_words_dictionary(csv_lines):
    words = {}
    for line in csv_lines:
        writing, other_stuff = split_writing_and_other_stuff(line)
        if writing in words:
            words[writing].append(other_stuff)
        else:
            words[writing] = [other_stuff]

    return words


field_separator = ";"
lines = ["虚空;こくう;pusta przestrzeń, puste niebo;",
         "既存;きそん;istnienie, egzystowanie, bytowanie;",
         "虚空;こくう;pusta przestrzeń;",
         "帰す;きす;zbliżać się do (końca), kończyć się, przypisywać;",
         "銀河;ぎんが;Droga Mleczna;",
         "銀河;ぎんが;galaktyka;"]

words = build_words_dictionary(lines)

for word in words:
    print(word)
    endings = words[word]
    for ending in endings:
        print(ending)
