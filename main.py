def main():
    file_path = "books/frankestein.txt"
    file_contents = read_file(file_path)
    word_count = count_words(file_contents)
    letters_count = count_letters(file_contents)
    sorted_letters_list = convert_dict_to_dict_list(letters_count)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document \n")

    for record in sorted_letters_list:
        if record["letter"].isalpha():
            print(f"The '{record["letter"]}' character was found {record["value"]}")

    print("--- End report ---")


def convert_dict_to_dict_list(letters_dict):
    sorted_letters_list = [
        {"letter": key, "value": value} for key, value in letters_dict.items()
    ]
    sorted_letters_list.sort(reverse=True, key=lambda dict: dict["value"])
    return sorted_letters_list

def read_file(path):
    with open(path) as f:
        return f.read()


def count_words(file_content):
    words = file_content.split()
    return len(words)


def count_letters(words):
    letters_dict = {}
    for letter in words:
        lowered_letter = letter.lower()
        if lowered_letter in letters_dict:
            letters_dict[lowered_letter] += 1
        else:
            letters_dict[lowered_letter] = 1
    return letters_dict


main()
