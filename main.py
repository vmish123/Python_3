def main():
    seventh_task()


def first_task():
    numbers_list = [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10]
    print(f"{len(set(numbers_list))} различных чисел")


def second_task():
    numbers_list_1 = [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10]
    numbers_list_2 = [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10, 11, 11, 12, 13, 13, 13]
    print(f"{len(set(numbers_list_1 + numbers_list_2))} различных чисел")


def third_task():
    numbers_list_1 = [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10]
    numbers_list_2 = [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10, 11, 11, 12, 13, 13, 13]
    print(*sorted(set(numbers_list_1).intersection(set(numbers_list_2))))


def fourth_task():
    numbers = input().split()
    mentioned_numbers = set()

    for number in numbers:
        number = int(number)

        if number in mentioned_numbers:
            print("YES")
        else:
            print("NO")
            mentioned_numbers.add(number)


def fifth_task():
    string_number = int(input())
    unique_words = set()

    for _ in range(string_number):
        words = input().split()
        unique_words.update(words)

    print(len(unique_words))


def sixth_task():
    surnames_number = int(input())
    surnames_mentioned = set()
    duplicated_surnames = set()

    count = 0
    for _ in range(surnames_number):
        surname = input().lower()

        if surname in duplicated_surnames:
            count += 1

        elif surname in surnames_mentioned:
            duplicated_surnames.add(surname)
            count += 2

        else:
            surnames_mentioned.add(surname)

    print(count)


def seventh_task():
    words = input().lower().split()
    words_dictionary = {}

    for word in words:
        word = word.lower()

        current_count = words_dictionary.get(word, 0)
        print(current_count, end=" ")

        words_dictionary[word] = current_count + 1


main()
