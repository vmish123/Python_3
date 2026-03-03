# Задание 1
def first_task():
    print(f"{len(set(input().split()))} различных чисел")


# Задание 2
def second_task():
    print(f"{len(set(input().split()) & set(input().split()))} различных чисел")


# Задание 3
def third_task():
    print(*sorted(set(map(int, input().split())).intersection(set(map(int, input().split())))))


# Задание 4
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


# Задание 5
def fifth_task():
    string_number = int(input())
    unique_words = set()

    for _ in range(string_number):
        words = input().split()
        unique_words.update(words)

    print(len(unique_words))


# Задание 6
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


# Задание 7
def seventh_task():
    words = input().lower().split()
    words_dictionary = {}

    for word in words:
        word = word.lower()

        current_count = words_dictionary.get(word, 0)
        print(current_count, end=" ")

        words_dictionary[word] = current_count + 1

    print()  # Перенос для корректной работы из main()


# Задание 8
def eighth_task():
    pairs_number = int(input())
    synonyms = {}

    for _ in range(pairs_number):
        word1, word2 = input().split()

        synonyms[word1] = word2
        synonyms[word2] = word1

    word = input()
    print(synonyms[word])


# Задание 9
def ninth_task():
    votes_number = int(input())
    candidates = {}

    for _ in range(votes_number):
        name, votes = input().split()
        votes = int(votes)

        candidates[name] = candidates.get(name, 0) + votes

    for candidate in sorted(candidates):
        print(candidate, candidates[candidate])


# Задание 10
def tenth_task():
    action_dictionary = {
        "read": "R",
        "write": "W",
        "execute": "X"
    }

    files_number = int(input())
    files = {}

    for _ in range(files_number):
        entered_string = input().split()
        file = entered_string[0]
        permissions = set(entered_string[1:])
        files[file] = permissions

    request_number = int(input())

    for _ in range(request_number):
        action, file = input().split()
        permission = action_dictionary[action]

        if file in files and permission in files[file]:
            print("OK")
        else:
            print("Access denied")


def main():
    print("Задание 1")
    first_task()
    print("Задание 2")
    second_task()
    print("Задание 3")
    third_task()
    print("Задание 4")
    fourth_task()
    print("Задание 5")
    fifth_task()
    print("Задание 6")
    sixth_task()
    print("Задание 7")
    seventh_task()
    print("Задание 8")
    eighth_task()
    print("Задание 9")
    ninth_task()
    print("Задание 10")
    tenth_task()


main()
